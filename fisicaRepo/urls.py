"""fisicaRepo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sem1/', views.sem1, name='sem1'),
    path('sem2/', views.sem2, name='sem2'),
    path('sem3/', views.sem3, name='sem3'),
    path('sem4/', views.sem4, name='sem4'),
    path('sem5/', views.sem5, name='sem5'),
    path('sem6/', views.sem6, name='sem6'),
    
    # materias de los semestres
    path('sem1_1/',views.sem1_1, name='sem1_1'),
    path('sem1_2/',views.sem1_2, name='sem1_2'),
    path('sem1_3/',views.sem1_3, name='sem1_3'),
    path('sem1_4/',views.sem1_4, name='sem1_4'),
    path('sem1_5/',views.sem1_5, name='sem1_5'),
    path('sem2_1/',views.sem2_1, name='sem2_1'),
    path('sem2_2/',views.sem2_2, name='sem2_2'),
    path('sem2_3/',views.sem2_3, name='sem2_3'),
    path('sem2_4/',views.sem2_4, name='sem2_4'),
    path('sem3_1/',views.sem3_1, name='sem3_1'),
    path('sem3_2/',views.sem3_2, name='sem3_2'),
    path('sem3_3/',views.sem3_3, name='sem3_3'),
    path('sem3_4/',views.sem3_4, name='sem3_4'),
    path('sem4_1/',views.sem4_1, name='sem4_1'),
    path('sem4_2/',views.sem4_2, name='sem4_2'),
    path('sem4_3/',views.sem4_3, name='sem4_3'),
    path('sem4_4/',views.sem4_4, name='sem4_4'),
    path('sem4_5/',views.sem4_5, name='sem4_5'),
    path('sem5_1/',views.sem5_1, name='sem5_1'),
    path('sem5_2/',views.sem5_2, name='sem5_2'),
    path('sem5_3/',views.sem5_3, name='sem5_3'),
    path('sem5_4/',views.sem5_4, name='sem5_4'),
    path('sem5_5/',views.sem5_5, name='sem5_5'),
    path('sem6_1/',views.sem6_1, name='sem6_1'),
    path('sem6_2/',views.sem6_2, name='sem6_2'),
    path('sem6_3/',views.sem6_3, name='sem6_3'),
    path('sem6_4/',views.sem6_4, name='sem6_4'),
    path('sem6_5/',views.sem6_5, name='sem6_5'),

]

