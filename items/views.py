from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import  Item, Wishlist
from .forms import ItemForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ItemsListView(ListView):
    model = Item
    paginate_by = 6
    queryset = Item.objects.order_by('-created_at')[:30]

@method_decorator(login_required, name='dispatch')
class ItemsByCategoryListView(ListView):
    model = Item
    template_name = 'items/item_by_category.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super(ItemsByCategoryListView, self).get_queryset()
        return queryset.filter(category=self.kwargs['pk'])
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['name']
        return context

@method_decorator(login_required, name='dispatch')
class ItemDetailView(DetailView):
    model = Item

@method_decorator(login_required, name='dispatch')
class ItemCreateView(CreateView):
    form_class = ItemForm
    template_name = 'items/create.html'
    success_url = reverse_lazy('items:items')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.state == '':
            return redirect(reverse_lazy('profile') + '?complete_profile')
        return super(ItemCreateView, self).dispatch(request, *args, **kwargs)
    
@method_decorator(login_required, name='dispatch')
class ItemUpdateView(UpdateView):
    form_class = ItemForm
    template_name = 'items/update.html'

    def get_object(self):
        obj = get_object_or_404(Item, created_by=self.request.user, pk=self.kwargs['pk'])
        return obj
    
    def get_success_url(self):
        return reverse_lazy('items:update', args=[self.object.id]) + '?ok'

@method_decorator(login_required, name='dispatch')  
class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('items:items')

    def get_object(self):
        obj = get_object_or_404(Item, created_by=self.request.user, pk=self.kwargs['pk'])
        return obj

@method_decorator(login_required, name='dispatch')    
class SearchItemView(ListView):
    model = Item
    template_name = 'items/item_search.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super(SearchItemView, self).get_queryset()
        search = self.request.GET.get('search')
        return queryset.filter(Q(name__icontains=search) | Q(description__icontains=search))
    
@method_decorator(login_required, name='dispatch')    
class SearchItemByStateView(ListView):
    model = Item
    template_name = 'items/item_search.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        state = self.kwargs.get('state')
        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(description__icontains=search))
        if state:
            queryset = queryset.filter(created_by__profile__state=state)
        return queryset

@login_required   
def add_to_wishlist(request, id):
    item = get_object_or_404(Item, id=id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.items.add(item)
    return redirect(reverse_lazy('items:detail', args=[item.pk]))

@login_required   
def remove_from_wishlist(request, id):
    item = get_object_or_404(Item, id=id)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.items.remove(item)
    return redirect(reverse_lazy('items:detail', args=[item.pk]))

class WishlistView(TemplateView):
    template_name = 'items/wishlist.html'
