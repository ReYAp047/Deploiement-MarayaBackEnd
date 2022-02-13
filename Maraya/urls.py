"""Maraya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from Actions import views as actionViews
from aPropos import views as aProposViews
from Email import views as emailViews
from Facebook import views as facebookViews
from Localisation import views as localisationViews
from q_On_Fait import views as qOnFaitViews
from Messages import views as Message
from Historique import views as Historique

admin.site.site_header= "Administration | Maraya |"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Actions/', actionViews.actionsList.as_view()),
    path('Images/', actionViews.imagesList.as_view()),
    path('FontImages/', actionViews.fontImagesList.as_view()),
    path('Partonaires/', actionViews.partonairesList.as_view()),
    path('Videos/', actionViews.videosList.as_view()),
    path('aPropos/', aProposViews.aProposList.as_view()),
    path('Email/', emailViews.emailList.as_view()),
    path('Facebook/', facebookViews.facebookList.as_view()),
    path('Localisation/', localisationViews.localisationList.as_view()),
    path('q_On_Fait/', qOnFaitViews.qOnFaitList.as_view()),
    path('Messages/', Message.MessageList.as_view()),
    path('Historique/', Historique.HistoriqueList.as_view()),
]
