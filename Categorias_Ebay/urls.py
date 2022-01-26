from django.urls import include, re_path
from Categorias_Ebay import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^categories$',views.categoryApi),
    re_path(r'^categories/([0-9]+)$',views.categoryApi)]

