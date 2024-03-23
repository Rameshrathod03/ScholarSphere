from django.contrib import admin
from django.urls import path
from faculty import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('optimizing-your-resume/', views.blog1, name='optimizing-your-resume'),
    path('sample-cover-letter/', views.blog2, name="sample-cover-letter"),
    path('search/', views.search, name='search'),
    path('professor/<slug:professor_name>/', views.professor, name='professor'),
] 

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
