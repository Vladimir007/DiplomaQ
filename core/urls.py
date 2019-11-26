from django.urls import path
from core import views, api

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('student/<int:student_id>/', views.StudentView.as_view(), name='student'),

    path('download/<int:pk>/', views.DonwloadFileView.as_view(), name='download'),

    path('api/upload/', api.UploadFileView.as_view(), name='api-upload-file'),
    path('api/comment/<int:diploma_id>/', api.ChangeCommentView.as_view(), name='api-comment'),
    path('api/remove-file/<int:diploma_id>/', api.RemoveDiplomaFileView.as_view(), name='api-remove-file'),
]
