from django.contrib import admin
from django.urls import path
from authentication.views import LoginView, SignupView
from flux.views import flux

urlpatterns = [
    path('admin/', admin.site.urls),
    # Pages de connection et création de compte
    path('', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    #Utilisateur connecter
    path('flux/', flux, name='flux'),
]
