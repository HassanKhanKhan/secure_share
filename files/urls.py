from django.urls import path
from .views import FileManagerView, DownloadView, DeleteFileView, LogoutView

urlpatterns = [
    path('', FileManagerView.as_view(), name='file_manager'),
    path('download/<int:file_id>/', DownloadView.as_view(), name='download_file'),  # ✅ name must match template
    path('delete/<int:file_id>/', DeleteFileView.as_view(), name='delete_file'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

