from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_funcionarios, name='listar_funcionarios'),
    path('novo/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('editar/<int:id>/', views.atualizar_funcionario, name='atualizar_funcionario'),
    path('deletar/<int:id>/', views.deletar_funcionario, name='deletar_funcionario'),
]
