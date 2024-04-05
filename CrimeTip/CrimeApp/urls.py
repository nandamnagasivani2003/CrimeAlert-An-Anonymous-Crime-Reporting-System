from django.urls import path

from . import views

urlpatterns = [
    path("index.html", views.index, name="index"),
    path("AuthorityLogin.html", views.AuthorityLogin, name="AuthorityLogin"),
    path("AuthorityLoginAction", views.AuthorityLoginAction, name="AuthorityLoginAction"),
    path("UserLogin.html", views.UserLogin, name="UserLogin"),
    path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),
    path("Register.html", views.Register, name="Register"),
    path("RegisterAction", views.RegisterAction, name="RegisterAction"),
    path("SubmitTip.html", views.SubmitTip, name="SubmitTip"),
    path("SubmitTipAction", views.SubmitTipAction, name="SubmitTipAction"),
    path("ViewTip", views.ViewTip, name="ViewTip"),
    path("TrainML", views.TrainML, name="TrainML"),
    path("ViewReports", views.ViewReports, name="ViewReports"),
    path("ViewUsers", views.ViewUsers, name="ViewUsers"),
    path("feedback", views.feedback, name="feedback"),
    path("ViewallFeedbacks",views.ViewallFeedbacks,name="ViewallFeedbacks"),
]
