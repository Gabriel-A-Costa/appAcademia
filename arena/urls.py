from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('academia-admin/', admin.site.urls),
    path('', include('academia.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/<int:pk>/', user_views.profile, name='profile'),
    path('profile-list/', user_views.profile_list, name='profile_list'),
    path('edit-profile/', user_views.edit_profile, name='edit_profile'),
    path('edit-password/', user_views.edit_password, name='edit_password'),
    path('profile-edit-user-image/<int:pk>', user_views.edit_user_image, name='edit_user_image'),

    path('new-anamnese/<int:pk>/', user_views.new_anamnese, name='new-anamnese'),
    path('edit-anamnese/<int:pk>/<int:ak>', user_views.edit_anamnese, name='edit_anamnese'),
    path('delete-anamnese/<int:pk>/', user_views.delete_anamnese, name='delete_anamnese'),


    path('new-antropometria/<int:pk>/', user_views.new_antropometria, name='new-antropometria'),
    path('edit-antropometria/<int:pk>/<int:ak>', user_views.edit_antropometria, name='edit_antropometria'),
    path('delete-antropometria/<int:pk>', user_views.delete_antropometria, name='delete_antropometria'),

    
    # section 9 lecture 47
    path('login/', user_views.login_user, name='login'),
    path('logout/', user_views.logout_user, name='logout'),
]

handler404 = "academia.views.handler404"
handler500 = "academia.views.handler500"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

