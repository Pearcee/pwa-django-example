from django.conf.urls import url
from django.urls import path
from django.http import HttpResponse
from . import views

from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('base_layout', views.base_layout, name='base_layout'),
    path(r'getdata',views.getdata,name='getdata')
]

urlpatterns += [
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nallow: /", ) ),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),

]