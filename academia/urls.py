from django.urls import path
from users import views as user_views
from . import views

app_name = 'academia'
urlpatterns = [
    path('', views.index, name='index'),
    path('room-form/<int:pk>/', views.room, name='aviso'),
    path('delete-aviso/<int:pk>/', views.delete_aviso, name='delete_aviso'),
    path('edit-aviso/<int:pk>/', views.edit_aviso, name='edit_aviso'),
# ---------------------------------da pra deixar mais clean--------------------------------
    path('treinos/', views.treinos, name='treinos'),

    path('aparelhos/', views.aparelhos, name='aparelhos'),
    path('exercicios/', views.exercicios, name='exercicios'),
    path('training-planning/<int:pk>/', views.training_planning, name='training_planning'),
# -----------------------------------------------------------------------------------------
    path('edit-training/<int:pk>/<int:ek>', views.edit_training, name='edit_training'),
    path('delete-training/<int:pk>/', views.delete_training, name='delete_training'),

    path('delete-aparelho/<int:pk>/', views.delete_aparelho, name='delete_aparelho'),
    path('delete-exercicio/<int:pk>/', views.delete_exercicio, name='delete_exercicio'),
    path('delete-treino/<int:pk>/', views.delete_treino, name='delete_treino'),
# -----------------------------------------------------------------------------------------
    path('training/<int:pk>/<int:ek>', views.training, name='training'),
    path('warnings/', views.warnings, name='warnings'),
]