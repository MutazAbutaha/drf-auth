from django.urls import path

from .views import MovielistView,MovieDetailView
urlpatterns = [
   
   path('',MovielistView.as_view(), name= 'thing_list'),
   path('<int:pk>/',MovieDetailView.as_view(), name= 'thing_detail')

]