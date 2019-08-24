from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from adoptions import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^adoptions/(\d+)/', views.pet_detail, name="pet_detail"),
] + static(settings.STATIC_URL, documen_root=settings.STATIC_ROOT)
