from django.urls import path
from Signup import views
urlpatterns = [
   path('',views.Signup,name="Signup"),
   path('insert',views.insertData,name="insertData"),
   path('update/<email>',views.updateData,name="updateData"),
   path('delete/<email>',views.deleteData,name="deleteData"),

]
