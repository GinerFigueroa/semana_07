# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:02:59 2023

@author: Alumno
"""


import gestion_archivos

def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Crear Archivo")
    print("2. Eliminar Archivo")
    print("3. Agregar Contenido")
    print("4. Mostrar contenido del archivo")
    print("5. Salir")


def crear():
    print("-- Crear Archivo --")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion_archivos.crear_archivo(archivo, contenido)

def eliminar():    
    print("-- Eliminar Archivo")
    archivo = input("Archivo: ")
    gestion_archivos.eliminar_archivo(archivo)

def agregar():
    print("-- Agregar Datos a un Archivo --")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion_archivos.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print("-- Mostrar contenido de un archivo -- ")
    archivo = input("Archivo: ")
    print(gestion_archivos.leer_archivo(archivo))

def salir():
    print("Gracias por su visita....")

def error():
    print("Opción incorrecta")

opcion = 1
while opcion!=5:
    menu()
    opcion = int(input("opcion: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        salir()
    else:
        error()
        
