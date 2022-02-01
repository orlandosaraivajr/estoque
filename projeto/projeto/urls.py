from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('produto', include('produto.urls')),
    # path('admin/', admin.site.urls),
]
