import os
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import AparelhoForm, ExercicioForm, RoomForm, TreinoForm
from .models import Aparelho, Exercicio, Room, Treinos
from users.decorators import allowed_users
from users.forms import TrainingPlanning
from users.models import Profile, Training
# Create your views here.
def index(request):
    page = 'index'
    rooms = Room.objects.all().order_by('-update')  # Ordena os avisos pela data de atualização mais recente

    context = {
        'page':page,
        'rooms':rooms,
    }
    return render(request, 'academia/home.html', context)

@login_required(login_url='login')
def room(request, pk):
    usuario = Profile.objects.get(user_id=pk).user  # Obtém o objeto User associado ao Profile
    form = RoomForm(request.POST or None)

    if form.is_valid():
        aviso = form.save(commit=False)
        aviso.host = usuario
        aviso.save()
        return redirect('academia:index')  # Redirecione para a página de confirmação ou listagem
    
    page = 'aviso'
    context = {
        'form': form,
        'page': page,  # Passa os avisos para o contexto
    }
    return render(request, 'academia/room-form.html', context)

def handler404(request, exception=None):
    return render(request, 'academia/404.html', status=404)

def handler500(request, exception=None):
    return render(request, 'academia/500.html', status=500)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def treinos(request):
    form = TreinoForm(request.POST or None, request.FILES or None)
    treinos = Treinos.objects.all()

    if form.is_valid():
        form.save()
        return redirect('academia:treinos')
    
    page = 'treinos'
    context = {
        'form':form,
        'treinos':treinos,
        'page':page,
    }
    return render(request, 'academia/treinos-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def aparelhos(request):
    form = AparelhoForm(request.POST or None, request.FILES or None)
    aparelhos = Aparelho.objects.all()

    if form.is_valid():
        form.save()
        return redirect('academia:aparelhos')
    
    page = 'aparelhos'
    context = {
        'form':form,
        'aparelhos':aparelhos,
        'page':page,
    }
    return render(request, 'academia/aparelhos-form.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def exercicios(request):
    form = ExercicioForm(request.POST or None, request.FILES or None)
    exercicios = Exercicio.objects.all()

    if form.is_valid():
        form.save()
        return redirect('academia:exercicios')

    page = 'exercicios'
    context = {
        'form':form,
        'exercicios':exercicios,
        'page':page
    }
    return render(request, 'academia/exercicio-form.html', context)

# ERRO NOS EDITS, QUEM SABE UM DIA EU CORRIJA ESSA FUNCIONALIDADE

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def edit_aparelho(request, pk):
#     aparelho = Aparelho.objects.get(id=pk)
#     old_image_path = aparelho.aparelho_image.path if aparelho.aparelho_image else None  # Salva o caminho da imagem antiga, se existir
#     form = AparelhoForm(request.POST or None, request.FILES or None, instance=aparelho)
#     if form.is_valid():
#         new_image = form.cleaned_data.get('aparelho_image')  # Obtém a nova imagem do formulário
#         if not new_image:  # Se não houver uma nova imagem selecionada
#             aparelho.aparelho_image = 'aparelhos/default.jpg'  # Define a imagem padrão
#         form.save()
        
#         # Remove a imagem antiga da pasta de mídia, se existir e não é a imagem padrão
#         if old_image_path and str(aparelho.aparelho_image) != 'aparelhos/default.jpg' and os.path.isfile(old_image_path):
#             os.remove(old_image_path)
        
#         messages.success(request, "Device edited successfully!")
#         return redirect('academia:aparelhos')
    
#     page = 'aparelhos'
#     context = {
#         'form': form,
#         'page':page,
#     }
#     return render(request, 'academia/edit-aparelho.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def edit_exercicio(request, pk):
#     exercicio = Exercicio.objects.get(id=pk)
#     old_image_path = exercicio.exercicio_image.path if exercicio.exercicio_image else None  # Salva o caminho da imagem antiga, se existir
#     form = ExercicioForm(request.POST or None, request.FILES or None, instance=exercicio)
#     if form.is_valid():
#         new_image = form.cleaned_data.get('exercicio_image')  # Obtém a nova imagem do formulário
#         if not new_image:  # Se não houver uma nova imagem selecionada
#             exercicio.exercicio_image = 'exerciciorr/default.jpg'  # Define a imagem padrão
#         form.save()
        
#         # Remove a imagem antiga da pasta de mídia, se existir e não é a imagem padrão
#         if old_image_path and str(exercicio.exercicio_image) != 'exercicio/default.jpg' and os.path.isfile(old_image_path):
#             os.remove(old_image_path)
        
#         messages.success(request, "Device edited successfully!")
#         return redirect('academia:exercicios')

#     page = 'exercicios'
#     context = {
#         'form':form,
#         'page':page,
#     }
#     return render(request, 'academia/edit-exercicio.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def training_planning(request, pk):
    usuario = Profile.objects.get(user__id=pk)

    if request.method == 'POST':
        form = TrainingPlanning(request.POST, user=usuario)

        if form.is_valid():
            training = form.save(commit=False)
            training.user = usuario.user
            training.save()
            usuario.trainings.add(training)
            form.save()
            return redirect('academia:training_planning', pk=pk)
    else:
        form = TrainingPlanning(user=usuario)

    page = 'profile'
    exercicio_types = Exercicio.objects.values_list('id', 'exercicio_type')
    aparelhos = Aparelho.objects.values_list('id', 'aparelho_name')
    treinos = Treinos.objects.values_list('id', 'treino_name')
    context = {
        'form':form,
        'page':page,
        'exercicio_types':exercicio_types,
        'aparelhos':aparelhos,
        'treinos':treinos,
    }    
    return render(request, 'academia/training-planning.html', context)
    
@login_required(login_url='login')
def training(request, pk, ek):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        trainings = Training.objects.filter(type_id=ek , user_id=pk)
        # verificar se é o admin editanto pefil
        is_admin = request.user.groups.filter(name='admin').exists()

        page = 'profile'
        context = {
            'profile':profile,
            'trainings':trainings,
            'is_admin':is_admin,
            'page':page,
        }
        if profile.user.id == request.user.id or is_admin:
            return render(request, 'academia/training.html', context)
        else:
            messages.success(request, ("You Not Have Permission..."))
            return redirect('academia:index')
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def edit_training(request, pk, ek):
    training = Training.objects.get(id=ek)
    form = TrainingPlanning(request.POST or None, instance=training)
    exercicio_types = Exercicio.objects.values_list('id', 'exercicio_type')
    aparelhos = Aparelho.objects.values_list('id', 'aparelho_name')
    treinos = Treinos.objects.values_list('id', 'treino_name')

    if form.is_valid():
        form.save()
        messages.success(request, 'Training successfully edited!')
        return redirect('academia:training', pk=pk, ek=training.type_id)
    
    page = 'profile'
    context = {
        'form':form,
        'exercicio_types':exercicio_types,
        'aparelhos':aparelhos,
        'treinos':treinos,
        'page':page,
    }
    return render(request, 'academia/edit-training.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def edit_aviso(request, pk):
    aviso = Room.objects.get(id=pk)
    form = RoomForm(request.POST or None, request.FILES or None, instance=aviso)
    if form.is_valid():
        form.save()
    
        messages.success(request, "Aviso Editado Com Sucesso!")
        return redirect('academia:index')

    page = 'aviso'
    context = {
        'form':form,
        'page':page,
    }
    return render(request, 'academia/edit-aviso.html', context)

# ------------------Da pra deixar mais clean-------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_training(request, pk):
    training = Training.objects.get(id=pk) 
    user = training.user_id
    training.delete()
    messages.success(request, ("The training was successfully deleted!"))
    return redirect('academia:training', pk=user, ek=training.type_id)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_aparelho(request, pk):
    aparelho = Aparelho.objects.get(id=pk) 

    if aparelho.aparelho_image and str(aparelho.aparelho_image) != 'aparelhos/default.jpg':
        image_path = os.path.join(settings.MEDIA_ROOT, str(aparelho.aparelho_image))
        if os.path.exists(image_path):
            os.remove(image_path)

    aparelho.delete()
    messages.success(request, ("The device was successfully deleted!"))
    return redirect('academia:aparelhos')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_exercicio(request, pk):
    exercicio = Exercicio.objects.get(id=pk) 

    if exercicio.exercicio_image and str(exercicio.exercicio_image) != 'exercicio/default.jpg':
        image_path = os.path.join(settings.MEDIA_ROOT, str(exercicio.exercicio_image))
        if os.path.exists(image_path):
            os.remove(image_path)
            
    exercicio.delete()
    messages.success(request, ("The exercise was successfully deleted!"))
    return redirect('academia:exercicios')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_treino(request, pk):
    treino = Treinos.objects.get(id=pk) 

    if treino.treino_image and str(treino.treino_image) != 'treino/default.jpg':
        image_path = os.path.join(settings.MEDIA_ROOT, str(treino.treino_image))
        if os.path.exists(image_path):
            os.remove(image_path)
            
    treino.delete()
    messages.success(request, ("The trainig was successfully deleted!"))
    return redirect('academia:treinos')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_aviso(request, pk):
    aviso = Room.objects.get(id=pk) 
    aviso.delete()
    messages.success(request, ("O Aviso Foi Deletado Com Sucesso!"))
    return redirect('academia:index')

# ---------------------------------------------------------------------

def warnings(request):
    return HttpResponse("Billboard")
