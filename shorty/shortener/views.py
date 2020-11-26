from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import URLs
from django.views import generic
from django.apps import apps
from django.http import Http404
from shortener import models
import short_url
from . import schema
from .forms import In_Form
import itertools



def root(request, url_hash):
    url = get_object_or_404(URLs, url_hash=url_hash)
    url.clicked()

    return redirect(url.full_url)

def redirect_view(request, tiny):
    """
    Redirect to a given object from a short URL.
    """

    model = apps.get_model('shortener', 'URL')
    try:
        id = short_url.decode_url(tiny)
    except ValueError:
        raise Http404('Bad encoded ID.')

    obj = get_object_or_404(model, pk=id)
    return redirect(obj)

    def get_absolute_url(self):
        return reverse_lazy('blog_page', args=[self.slug])

class index(generic.TemplateView):
    template_name='short_url.html'


def home_view(request):
    context ={}
    urllistinquary =[]
    if request.method == 'POST':
        temp = In_Form(request.POST)#if request.POST:
        temp_addr = request.POST['url_input']
        ctx = {'message':  temp_addr,}
        ct = {'message':  "data submitted successfully",}
        ctnot = {'message':  "Link already exists! ==> ",}
        obj=URLs.objects.all().values()
        urllistinquary=list(obj)

        if temp.is_valid():
            if not  URLs.objects.filter(full_url=temp_addr):
                url_object = URLs.objects.create(full_url =temp_addr)
                hashed = url_object.url_hash
                addr_link = temp_addr+hashed
                out_short = hashed
                url_out = {'hasheds': hashed,
                 'reaf': addr_link, }

                return render(request, '1234.html', url_out)
            url_ot = URLs.objects.get(full_url =temp_addr)
            ha = url_ot.url_hash
            addr_l = temp_addr+ha
            ur_out = {'hasheds': ha,
             'reaf': addr_l, }
            return render(request, '1234.html', ur_out)

        else:
            form = In_Form(None)
    return render(request, 'home.html', {'form':In_Form})
