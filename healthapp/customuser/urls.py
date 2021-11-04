

from django.urls import path
from .views import home, signup, logout

urlpatterns = [
    path('', home),
    path('signup/', signup),
    path('logout/', logout),
]