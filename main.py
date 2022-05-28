#DEBAJO TODO LO QUE VAMOS A IMPORTAR
#import os

  #SALE MENSAJE DE MENU 
print("{:^50}".format("***GESTOR DE BROADCAST***"))
while True:
  print("[1]"," ","Crear campaña")
  print("[2]"," ","Cargar Base de números")
  print("[3]"," ","Lanzar campaña")
  print("[4]"," ","Créditos")
  print("[5]"," ","Salir")
  elige = input("Ingrese una opción :")


  #---------------------------OPCION 1-----------------------------------
  if elige == "1":
    #-----------------para borrar el menu esperando que el profe suba ejemplo
    #cls = lambda:os.system('cls')
    #cls()
    #---------------------------------------------------
    print("{:^50}".format("Opción1. Crear campaña"))
    input("Ingrese nombre para la campaña: ")
    print("la variable es declarada entre []")
    print("Numero de variables máximo 2")
    #usamos variables??
    texto = input("Ingrese texto del SMS: ")

    #--------------------que alguien lo pase a funcion------------------
    x = texto.split( )
    #quitando []
    lst_str = str(x[1])[1:-1] 
    #pasando strig a lista
    aa= lst_str.split(',')
    #condiciones para pariables  
    if len(aa) == 1 :
      variable1 = aa[0]
      n_variab_uso = "1"
    elif len(aa) == 2:
      variable1 = aa[0]
      variable2 = aa[1]
      n_variab_uso = "2"  
    else:
      print("Recuerde numero máximo son 2 variables en el mensaje")
    #-----------------termina funcion------------------
       
    #Condición para validar SMS  y resultado de campaña creada
    print(" ")
    print(" ")
    if len(texto) <= 120 :
      print("Campaña creada.","  ", "id_creado" ,"  " , len(texto),"  " ,  n_variab_uso)
      
    #Yaaaap solo faltaria el "id_creado"... creo que se ebe guardar cada campaña 
      #ummh :"/"
      
    
  #-----------------Termina opción 1-----------------------------------  
    
  #-------------------------------OPCION2------------------------------------
  
  elif elige == "2":
    print("{:^50}".format("Opción2. Cargar Base de número"))
    base = input("Ingrese un nombre para la base de números:   ") 
    print("Recuerde número para finalizar es 666")
    numero = input("Ingrese número telefónico:  ") 
    variable1 = input("Ingrese variable1:")
    variable2 = input("Ingrese variable2:")
  
    while len(numero)== 9:
      numero = input("Ingrese número telefónico: ") 
      variable1 = input("Ingrese variable1:")
      variable2 = input("Ingrese variable2:")
      if numero == 666 :
        break
    print(numero, variable1 , variable2)




  #Falta como guardar en di

    
  #----------------------termina opción2----------------------------------    
  #---------------------------OPCIÓN3----------------------------------
  elif elige == "3":
    print("{:^50}".format("Opcion3. Crear base de números"))
    


     
  