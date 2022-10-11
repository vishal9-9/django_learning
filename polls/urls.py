from polls import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='polls_index'),
    path('<int:id>',views.detail),
    path('blogs/',views.project_details_all),
    path('blogs/<int:id>',views.project_details)
]
 