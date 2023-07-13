from django.urls import path
from .views import file_upload, file_list, download_file

urlpatterns = [
    path('upload/', file_upload, name='upload'),
    path('list/', file_list, name='list'),
    path('download/<int:file_id>/', download_file, name='download_file')
]
