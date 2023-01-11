from django.shortcuts import render
# Importo Firebase Admin SDK 
import firebase_admin
 
# Hacemos uso de credenciales que nos permitirán usar Firebase Admin SDK 
from firebase_admin import credentials
 
# Importo el Servicio Firebase Realtime Database 
from firebase_admin import db
 

 
def index(request):
    return render(request, 'index.html', {})

def sem1(request):
    return render(request, 'cards/sem1.html', {})

def sem2(request):
    return render(request, 'cards/sem2.html', {})

def sem3(request):
    return render(request, 'cards/sem3.html', {})

def sem4(request):
    return render(request, 'cards/sem4.html', {})

def sem5(request):
    return render(request, 'cards/sem5.html', {})

def sem6(request):
    return render(request, 'cards/sem6.html', {})


# materias

def sem1_1(request):
    return render(request, 'subCards/sem1_1.html', {})
def sem1_2(request):
    return render(request, 'subCards/sem1_2.html', {})
def sem1_3(request):
    return render(request, 'subCards/sem1_3.html', {})
def sem1_4(request):
    return render(request, 'subCards/sem1_4.html', {})
def sem1_5(request):
    return render(request, 'subCards/sem1_5.html', {})
def sem2_1(request):
    return render(request, 'subCards/sem2_1.html', {})
def sem2_2(request):
    return render(request, 'subCards/sem2_2.html', {})
def sem2_3(request):
    return render(request, 'subCards/sem2_3.html', {})
def sem2_4(request):
    return render(request, 'subCards/sem2_4.html', {})
def sem3_1(request):
    return render(request, 'subCards/sem3_1.html', {})
def sem3_2(request):
    return render(request, 'subCards/sem3_2.html', {})
def sem3_3(request):
    return render(request, 'subCards/sem3_3.html', {})
def sem3_4(request):
    return render(request, 'subCards/sem3_4.html', {})
def sem4_1(request):
    return render(request, 'subCards/sem4_1.html', {})
def sem4_2(request):
    return render(request, 'subCards/sem4_2.html', {})
def sem4_3(request):
    return render(request, 'subCards/sem4_3.html', {})
def sem4_4(request):
    return render(request, 'subCards/sem4_4.html', {})
def sem4_5(request):
    return render(request, 'subCards/sem4_5.html', {})
def sem5_1(request):
    return render(request, 'subCards/sem5_1.html', {})
def sem5_2(request):
    return render(request, 'subCards/sem5_2.html', {})
def sem5_3(request):
    return render(request, 'subCards/sem5_3.html', {})
def sem5_4(request):
    return render(request, 'subCards/sem5_4.html', {})
def sem5_5(request):
    return render(request, 'subCards/sem5_5.html', {})
def sem6_1(request):
    return render(request, 'subCards/sem6_1.html', {})
def sem6_2(request):
    return render(request, 'subCards/sem6_2.html', {})
def sem6_3(request):
    return render(request, 'subCards/sem6_3.html', {})
def sem6_4(request):
    return render(request, 'subCards/sem6_4.html', {})
def sem6_5(request):
    return render(request, 'subCards/sem6_5.html', {})
