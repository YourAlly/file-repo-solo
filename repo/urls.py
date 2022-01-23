from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from fire import settings
from repo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),

    # Auth
    path('login', views.login_request, name='login'),
    path('register', views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),

    # File Repo
    path('repo/view', views.view_repo, name='view-repo'),
    path('repo/view/folder/<int:folder_id>', views.view_folder, name='view-folder'),
    path('repo/view/file/<int:file_id>', views.upload_file, name='view-file'),

    path('repo/create/folder', views.view_folder, name='create-folder'),
    path('repo/upload/file', views.upload_file, name='upload-file'),
    path('repo/download/file/<int:file_id>', views.download_file, name='download-file'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
