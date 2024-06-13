from django.shortcuts import render, get_object_or_404
from registration.models import Profile
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])