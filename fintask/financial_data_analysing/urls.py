from django import urls
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'financial_data_analysing'

urlpatterns = [
    path('base/', views.base_page_view, name="base-page-view"),
    # path('plot/', )
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


