from items.models import Category

def ctx_dict(request):
    categories = Category.objects.all()
    ctx = {'categories': categories}
    return ctx