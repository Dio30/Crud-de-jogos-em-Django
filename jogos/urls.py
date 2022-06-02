from django.urls import path
from .views import JogosList, JogosNew, JogosUpdate, JogosDelete

urlpatterns = [
    path('lista/', JogosList.as_view(), name='lista'),
    path('novo/', JogosNew.as_view(), name = 'novo'),
    path('editar/<int:pk>/', JogosUpdate.as_view(), name ='editar'),
    path('deletar/<int:pk>/', JogosDelete.as_view(), name ='delete'),
]