from django.urls import path
from projeto import views

app_name = 'projeto'

urlpatterns = [
    path('', views.PessoaList.as_view(), name='list')
]