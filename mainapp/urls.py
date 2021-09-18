from django.urls import path
import mainapp.views as mainapp
from django.conf import settings
from  django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
