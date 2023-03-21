from django.shortcuts import render, get_object_or_404
from .models import Gallery, About, Edication, Exper, Cantact
from .forms import CantactForm

def product_list(request, category_slug=None):
    category = None
    categories = Gallery.objects.all()

    if category_slug:
        category = get_object_or_404(Gallery, slug=category_slug)
        products = products.filter(category=category)


    form = CantactForm()
    context = {'form': form}

    context = {
        'category': category,
        'categories': categories, 
        'rasmlar': Gallery.objects.all().order_by('-id')[:6],
        "about": About.objects.all()[:1],
        'education': Edication.objects.all().order_by('-id')[:1],
        'exsper': Exper.objects.all().order_by('-id')[:1],
        'form': form,
    }

    return render(request, 'temp/index.html', context)
