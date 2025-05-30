from django.urls import path
from .views import run_code,save_code,get_saved_codes

urlpatterns = [
     path('run/', run_code),
     path("save/", save_code),
     path("saved/", get_saved_codes),]


                 