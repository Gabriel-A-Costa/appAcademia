from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models import Q
from django.shortcuts import redirect, render
from .decorators import admin_only, allowed_users, unauthenticated_user 
from .forms import RegisterForm, RememberMeForm, UpdateUserForm, ChangePasswordForm, ProfileImageForm, FormAnamnese, FormAntropometria
from .models import Profile, Training, Anamnese, Antropometria

# teste

# Create your views here.

# ----------------LOGIN/LOGOUT---------------------
@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        form = RememberMeForm(request, data=request.POST)

        if form.is_valid():
            remember_me = form.cleaned_data.get('remember_me')

            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if not remember_me:
                    request.session.set_expiry(0)  # Configura a expiração da sessão para fechar quando o navegador for fechado

                messages.success(request, f"You have been logged in as {username}")
                return redirect('academia:index')
    else:
        form = RememberMeForm()
    page = 'login'
    return render(request, 'users/login.html', {'form': form, 'page':page})


def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Logged Out..."))
    return redirect('academia:index')


# -----------------REGISTER/PROFILE-----------------------------
@login_required(login_url='login')
@admin_only
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = request.POST.get('username').lower()
            user.save()
            # Esse merda faz o update do campo telefone que tem no Profile, que é criado nessa def
            phone_number = request.POST.get('phone_number')
            Profile.objects.update_or_create(user=user, defaults={'phone_number': phone_number})

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, f'Welcome {user.username}, Your Account Is Created!')
            return redirect('profile_list')
        
    else:
        form = RegisterForm()
        
    page = 'profile_list'        
    context = {
        'form':form,
        'page':page,    
    }
    return render(request, 'users/register.html', context)


@login_required(login_url='login')
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        is_admin = request.user.groups.filter(name='admin').exists()

# ------------Confuso mais, isso é para ver quais os treinos u usuario tem cadastrado
        trainings = Training.objects.filter(user_id=pk)
        processed_types = set()

        unique_training = []
        for training in trainings:
            if training.type.exercicio_type not in processed_types:
                unique_training.append(training)
                processed_types.add(training.type.exercicio_type)
        
# --------------------------------------------------------------------------
        anamneses = Anamnese.objects.filter(user__id=pk)
        antropometrias = Antropometria.objects.filter(user__id=pk).order_by('-data_antropometria')

# --------------------------------------------------------------------------
        page = 'profile'        
        context = {
            'profile': profile,
            'trainings': trainings,
            'training_types': unique_training,
            'is_admin': is_admin,
            'page': page,
            'anamneses': anamneses,
            'antropometrias': antropometrias,
        }
        if profile.user.id == request.user.id or is_admin:
            return render(request, 'users/profile.html', context)
        else:
            messages.success(request, ("You Not Have Permission..."))
            return redirect('academia:index')  
    else:
        messages.success(request, ("You Must Be Logged In To This Page..."))
        return redirect('academia:index')    




@login_required(login_url='login')
@admin_only
def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.all()
        trainings = Training.objects.all()
        page = 'profile_list'

        # Search name of user
        profile_name = request.GET.get("user_name")
        if profile_name == '' or profile_name is not None:
            names = profile_name.split()
            first_name = names[0]
            last_name = names[-1]
            # filter for full name
            if len(names) > 1:
                profiles = profiles.filter(Q(user__first_name__icontains=first_name) & Q(user__last_name__icontains=last_name))
            else:
                # filter for first name or last name
                profiles = profiles.filter(Q(user__first_name__icontains=first_name) | Q(user__last_name__icontains=last_name))


        context = {
            'profiles':profiles,
            'trainings':trainings,
            'page':page,
        }
        return render(request, 'users/profile-list.html', context)


@login_required(login_url='login')
def edit_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST or None, instance=current_user)
        if form.is_valid():
            phone_number = request.POST.get('phone_number')
            Profile.objects.update_or_create(user=current_user, defaults={'phone_number': phone_number})
            form.save()

            login(request, current_user)
            messages.success(request, ("You Profile Has Been Updated!"))
            return redirect('profile', pk=request.user.id)
        
        page = 'profile'        
        context = {
            'form':form,
            'page':page,
        }

        return render(request, 'users/edit-profile.html', context)
    else:
        messages.error(request, ("You Must Be Logged In To View That Page..."))
        return redirect('academia:index')
    
@login_required(login_url='login')
def edit_user_image(request, pk):
    if request.method == 'POST':
        profile = Profile.objects.get(user_id=pk)
        form = ProfileImageForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=request.user.id)
        
    profile = Profile.objects.get(user_id=pk)
    form = ProfileImageForm(instance=profile)

    page = 'profile'        
    context = {
        'form':form,
        'page':page,
    }
    return render(request, 'users/edit-user-image.html', context)   

@login_required
def edit_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, ("You Password Has Been Updated, Please Log In Again..."))
                login(request, current_user)
                return redirect('edit_profile')   
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('edit_password') 
            
        else:
            form = ChangePasswordForm(current_user)
            page = 'profile'        

            context = {
                'form':form,
                'page':page,
            }
            return render(request, 'users/edit-password.html', context)
    else:
        messages.error(request, ("You Must Be Logged In To View That Page..."))
        return redirect('academia:index')
# --------------------------------Anamnese----------------------------------------
@login_required(login_url='login')
@admin_only 
def new_anamnese(request, pk):
    user = Profile.objects.get(user__id=pk)

    if request.method == 'POST':
        form = FormAnamnese(request.POST, user=user)
        if form.is_valid():
            anamnese = form.save(commit=False)
            anamnese.user = user.user
            anamnese.save()
            return redirect('profile', pk=user.id)
        else:
            print(form.errors)  # Adicione esta linha para depurar erros
    else:
        form = FormAnamnese(user=user)

    page = 'profile'
    context = {
        'page': page,
        'form': form,
        'meta_choices': Anamnese.META,
        'coluna_choices': Anamnese.COLUNA,
        'pressao_choices': Anamnese.PRESSAO,
        'opcoes_choices': Anamnese.OPCOES,
    }
    return render(request, 'users/new-anamnese.html', context)


@login_required(login_url='login')
@admin_only 
def edit_anamnese(request, pk, ak):
    anamnese = Anamnese.objects.get(id=ak)
    form = FormAnamnese(request.POST or None, instance=anamnese)

    if form.is_valid():
        form.save()
        messages.success(request, 'Anamnese successfully edited!')
        return redirect('profile', pk=pk)
    
    page = 'profile'
    context = {
        'form': form,
        'page': page,
        'meta_choices': Anamnese.META,
        'coluna_choices': Anamnese.COLUNA,
        'pressao_choices': Anamnese.PRESSAO,
        'opcoes_choices': Anamnese.OPCOES,
    }
    return render(request, 'users/edit-anamnese.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_anamnese(request, pk):
    anamnese = Anamnese.objects.get(id=pk) 
    user = anamnese.user_id
    anamnese.delete()
    messages.success(request, ("The anamnese was successfully deleted!"))
    return redirect('profile', pk=user)

# --------------------------------Antropometria----------------------------------------

@login_required(login_url='login')
@admin_only 
def new_antropometria(request, pk):
    user = Profile.objects.get(user__id=pk)

    if request.method == 'POST':
        form = FormAntropometria(request.POST, user=user)
        if form.is_valid():
            antropometria = form.save(commit=False)
            antropometria.user = user.user
            antropometria.save()
            return redirect('profile', pk=user.id)
        else:
            print(form.errors)
    else:
        form = FormAntropometria(user=user)

    page = 'profile'    
    context = {
        'page': page,
        'form': form,
        'avaliados': Antropometria.AVALIADO
    }
    return render(request, 'users/new-antropometria.html', context)

@login_required(login_url='login')
@admin_only 
def edit_antropometria(request, pk, ak):
    antropometria = Antropometria.objects.get(id=ak)
    form = FormAntropometria(request.POST or None, instance=antropometria)

    if form.is_valid():
        form.save()
        messages.success(request, 'Antropometria successfully edited!')
        return redirect('profile', pk=pk)
    
    page = 'profile'
    context = {
        'form': form,
        'page': page,
        'avaliados': Antropometria.AVALIADO,
    }
    return render(request, 'users/edit-antropometria.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_antropometria(request, pk):
    antropometria = Antropometria.objects.get(id=pk) 
    user = antropometria.user_id
    antropometria.delete()
    messages.success(request, ("The antropometria was successfully deleted!"))
    return redirect('profile', pk=user)