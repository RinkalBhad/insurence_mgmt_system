from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path("",views.index),
    path("customerclick/",views.customerclick),
    path("customersignup/",views.customersignup,name='customersignup'),
    path("aboutus/",views.aboutus),
    path("contactus/",views.contactus),
    path("customerlogin/",views.customerlogin,name="login"),
    path("customer_dashboard/",views.customer_dashboard,name="customer_dashboard"),
    path("question_history/",views.question_history,name="quesion_history"),
    path("ask_question/",views.ask_question),
    path("history/<int:id>",views.history,name="history"),
   # path("histry/",views.history,name="histry"),
    path("apply_policy/",views.apply_policy,name='apply'),
    path("userlogout/",views.userlogout),
    path("customerbase/",views.customerbase),
    path("another/",views.another),
    path("forget/",views.forget,name='forget'),
]
