from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, News, Recipe, Contact
from .forms import ContactForm

def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'lugis/menu_list.html', {'items': items})

def menu_detail(request, id):
    item = get_object_or_404(MenuItem, id=id)
    return render(request, 'lugis/menu_detail.html', {'item': item})

def news_list(request):
    news = News.objects.all()
    return render(request, 'lugis/news_list.html', {'news': news})
def news_detail(request, id):
    new = get_object_or_404(News, id=id)
    return render(request, 'lugis/news_detail.html', {'new': new})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'lugis/recipe_list.html', {'recipes': recipes})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'lugis/contact.html', {'form': form})
