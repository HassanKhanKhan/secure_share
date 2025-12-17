from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.http import FileResponse, Http404
from .models import SecureFile
import os

class FileManagerView(LoginRequiredMixin, View):
    template_name = 'files/file_manager.html'

    def get(self, request):
        # List all files, latest first
        files = SecureFile.objects.all().order_by('-uploaded_at')
        return render(request, self.template_name, {'files': files})

    def post(self, request):
        # Handle file upload
        f = request.FILES.get('file')
        if f:
            SecureFile.objects.create(
                owner=request.user,
                file=f,
                size=f.size
            )
        return redirect('file_manager')


class DownloadView(LoginRequiredMixin, View):
    def get(self, request, file_id):
        try:
            file = SecureFile.objects.get(id=file_id)
        except SecureFile.DoesNotExist:
            raise Http404("File not found")
        return FileResponse(file.file.open('rb'), as_attachment=True)


class DeleteFileView(LoginRequiredMixin, View):
    def post(self, request, file_id):
        try:
            file = SecureFile.objects.get(id=file_id)
        except SecureFile.DoesNotExist:
            raise Http404("File not found")

        # Only uploader can delete
        if file.owner == request.user:
            # delete file from storage
            if os.path.exists(file.file.path):
                os.remove(file.file.path)
            file.delete()
        return redirect('file_manager')


class LogoutView(LoginRequiredMixin, View):
    def post(self, request):
        logout(request)
        return redirect('login')  # Redirect to login page

    def get(self, request):
        # Also handle GET requests
        logout(request)
        return redirect('login')
