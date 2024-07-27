from django.contrib import admin
from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.index, name="index"),
    path('<str:slug>', views.blog_detail, name= 'blog_detail'),
    path('<slug:slug>/add_comment/', views.add_comment, name='add_comment'),
    path('category/<str:slug>', views.category, name='category'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
