from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
from .models import News, Category


def news_list_view(request):
    news_list_slide = News.published .all()
    latest_news_5 = News.published.all()[:5]
    jahon_news_one = News.published.filter(category__nomi='JAHON')[0]
    jahon_news_4 = News.published.filter(category__nomi='JAHON')[1:5]
    tasks_news = News.published.filter(category__nomi='SPORT')[:5]




    context = {
        'news_list' : news_list_slide,
        'latest_news_5' : latest_news_5,
        'jahon_news_one': jahon_news_one,
        'jahon_news_4': jahon_news_4,
        'tasks_news': tasks_news
    }

    return render(request, template_name='index.html', context=context)


def yangiliklar_batafsil_view(request, id):
    detail = News.objects.get(id = id)

    context = {
        'news' : detail

    }

    return render(request, 'news_site.html', context)
# Create your views here.

def contact_view(request):
    form = ContactForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        form.save()

        return HttpResponse("Xabaringiz yuborildi")


    context = {
        'form' : form
    }
    return render(request, template_name='contact.html', context=context )