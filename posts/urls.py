from django.conf.urls import url
from django.urls import path
from . import views

from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('base_layout', views.base_layout, name='base_layout'),
    path(r'getdata',views.getdata,name='getdata')
]

urlpatterns += [
    url(r'^robots\.txt$', TemplateView.as_view(template_name="blog/robots.txt", content_type='text/plain')),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),

]