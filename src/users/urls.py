from django.urls import path

from src.users.views import UsersListAPIView, UserRetrieveAPIView, UserPasswordAPIView

urlpatterns = [
    path('', UsersListAPIView.as_view()),
    path('change_password/', UserPasswordAPIView.as_view()),
    path('<str:username>/', UserRetrieveAPIView.as_view()),

]
