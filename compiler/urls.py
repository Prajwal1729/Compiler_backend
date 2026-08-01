from django.urls import path
from . views import signUp,login,languagesList,runCode

urlpatterns = [
    # path('test', test_code) for testing purpose 
    path('signup/', signUp),
    path('login/', login),
    path('languages/', languagesList),
    path('run/', runCode)
]

