from django.urls import path
from users import views, api

urlpatterns = [
    path('signin/', views.DiplomaLoginView.as_view(), name='login'),
    path('signout/', views.DiplomaLogoutView.as_view(), name='logout'),

    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit/', views.EditProfileView.as_view(), name='edit-profile'),

    path('api/free-students/', api.GetAvailableUsers.as_view(), name='api-free-students'),
    path('api/add-student/', api.NewStudentAPIView.as_view(), name='api-add-student'),
]
