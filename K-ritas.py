## menuRegistro
menuR = ""
menu=0

## Inicio de sesion 
inicioSesion = ""
administradores = {"nombre":"alejo", "nombre1": "camilo", "clave":1234, "clave1":4321, "codigo":1516, "codigo1":1416}


## Registro 
usuarioNuevo = {"nombre":"", "correo":"" ,"codigo":0 ,"contraseña":""}
datos = ""

print ("Bienvenido a K-ritas")
inicioSesion = input("Ya tiene un usuario registrado en K-ritas? (si), (no)")

    ## inicio de usuario
if inicioSesion == "si":
    name = input("Ingrese porfavor el nombre:  ")
    key = int(input("Ingrese porfavor la clave:  "))
    passw = int(input("Ingrese porfavor el codigo de seguridad:  "))

    if (name == administradores["nombre"] and key == administradores["clave"] and passw == administradores["codigo"]):
        print(f"Bienvenido {name} , Seras redireccionado al menu de inicio, espera porfavor ")
        while menu==1:
            menu=+1
            print("1)Inicio \n" "2)Categorias \n" "3)Notificaciones""\n4)Mi cuenta")
            opc=int(input("Ingrese la opcion a donde desea dirigirse "))
            if opc==1:
                print("1)Eventos")
                print("2)Carrito")
                print("3)Calendario")
                opc2=int(input("Ingrese el apartado al cual desea dirigirse  ")) 
                if opc2==2:  
                    n=1
                    n2=1
                    while n>0:
                        n2=1
                        print("Evento a guardar ")
              
                        respuesta=input(" ")
                        if respuesta=="si":
                            evento= input("ingrese el evento")
                        while n2>0:
                            print("desea guardar otro evento")    
                            print("si")
                            print("no")
                            respuesta2=input("Rta: ")
                            if respuesta2=="si":
                                n2=0
                            else:
                                n2=0
                                n=0 
            Adquirir=1
            while Adquirir==1:                   
                if opc2 == 1:
                    print("Fiestas para adultos")
                    print("Fiestas infantiles")
                    print("Fiestas de XV")
                    print("Primeras comuniones")
                    print("Bautizos")
                    print("Despedida de solteros")
                    opc3=input("Por favor ingrese el evento que desea adquirir ")
          
                    if opc3=="Fiesta para adultos":
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}
                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v))

                    if opc3=="Fiestas infantiles":
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}
                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v))

                    if opc3=="Fiestas de XV":
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}

                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v)) 

                    if opc3=="Primeras comuniones":
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}

                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v))

                    if opc3=="Bautizos":
                 
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}

                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v))

                    if opc3=="Despedida de solteros":
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}

                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v))   

                    Adquirir=int(input("Desea adquirir otro evento si:1,no:2 ? "))
                    if Adquirir==1:
                        n=+1
                    elif Adquirir==2:
                        menu=input("Desea volver al menu de inicio si, no?")
                        menu=1
                        menu=+1

                if opc2==3:
                    print("Enero")
                    print("Febrero")
                    print("Marzo")
                    print("Abril")
                    print("Mayo")
                    print("Junio")
                    print("Julio")
                    print("Agosto")
                    print("Septiembre")
                    print("Octubre")
                    print("Noviembre")
                    print("Diciembre")
                    Calendario=input("Ingrese el mes en el que desea el evento")



    elif (name == administradores["nombre1"] and key == administradores["clave1"] and passw == administradores["codigo1"]):
        print(f"Bienvenido {name} , Seras redireccionado al menu de inicio, Espera porfavor")
        while menu==1:
            menu=+1
            print("1)Inicio \n" "2)Categorias \n" "3)Notificaciones""\n4)Mi cuenta")
            opc=int(input("Ingrese la opcion a donde desea dirigirse "))
            if opc==1:
                print("1)Eventos")
                print("2)Carrito")
                print("3)Calendario")
                opc2=int(input("Ingrese el apartado al cual desea dirigirse  ")) 
                if opc2==2:  
                    n=1
                    n2=1
                    while n>0:
                        n2=1
                        print("Evento a guardar ")
              
                        respuesta=input(" ")
                        if respuesta=="si":
                            evento= input("ingrese el evento")
                        while n2>0:
                            print("desea guardar otro evento")    
                            print("si")
                            print("no")
                            respuesta2=input("Rta: ")
                            if respuesta2=="si":
                                n2=0
                            else:
                                n2=0
                                n=0 
            Adquirir=1
            while Adquirir==1:                   
                if opc2 == 1:
                    print("Fiestas para adultos")
                    print("Fiestas infantiles")
                    print("Fiestas de XV")
                    print("Primeras comuniones")
                    print("Bautizos")
                    print("Despedida de solteros")
                    opc3=input("Por favor ingrese el evento que desea adquirir ")
          
                    if opc3=="Fiesta para adultos":
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}
                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v))

                    if opc3=="Fiestas infantiles":
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}
                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v))

                    if opc3=="Fiestas de XV":
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}

                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v)) 

                    if opc3=="Primeras comuniones":
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}

                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v))

                    if opc3=="Bautizos":
                 
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}

                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v))

                    if opc3=="Despedida de solteros":
                        print("Costo Eventos: ")
                        direccion= input("Ingrese la direccion de su residencia ")
                        fecha=int(input("Ingrese la fecha "))
                        lugar=input("Ingrese el lugar a donde se llevara acabo el evento ")
                        pago=int(input("Por favor ingrese el total a pagar "))
                        AdquirirEvento={"direccion":direccion,"fecha":fecha,"lugar":lugar,"pago":pago}

                        for k,v in AdquirirEvento.items():
                            print(("%s = %s") %(k,v))   

                    Adquirir=int(input("Desea adquirir otro evento si:1,no:2 ? "))
                    if Adquirir==1:
                        n=+1
                    elif Adquirir==2:
                        menu=input("Desea volver al menu de inicio si, no?")
                        menu=1
                        menu=+1

                if opc2==3:
                    print("Enero")
                    print("Febrero")
                    print("Marzo")
                    print("Abril")
                    print("Mayo")
                    print("Junio")
                    print("Julio")
                    print("Agosto")
                    print("Septiembre")
                    print("Octubre")
                    print("Noviembre")
                    print("Diciembre")
                    Calendario=input("Ingrese el mes en el que desea el evento")


        if (menu == 1):
            menu =+ 1
        else:
            menu == 0

    else:
       print ("Los datos ingresados no son correctos")

    ## registro usuario
elif inicioSesion == "no":
        usuarioNuevo ["nombre"] = input("Bienvenido al registro de usuario, Ingrese porfavor su nombre:   ")
        usuarioNuevo ["correo"] = input("Bienvenido al registro de usuario, Ingrese porfavor un correo electronico:  ")
        usuarioNuevo ["contraseña"] = input("Ingrese porfavor una contraseña:  ")
        usuarioNuevo ["codigo"] = int(input("Ingrese un codigo de seguridad para la cuenta "))
        print (usuarioNuevo)
        datos = input("Los datos ingresados son correctos?: (si), (no)")
        if (datos == "si"):
            print ("En un momento seras redireccionado al menu de inicio, espera porfavor")

        elif (datos == "no"):
            usuarioNuevo ["nombre"] = input("Bienvenido al registro de usuario, Ingrese porfavor su nombre:   ")
            usuarioNuevo ["correo"] = input("Bienvenido al registro de usuario, Ingrese porfavor un correo electronico:  ")
            usuarioNuevo ["contraseña"] = input("Ingrese porfavor una contraseña:  ")
            usuarioNuevo ["codigo"] = int(input("Ingrese un codigo de seguridad para la cuenta "))
            print (usuarioNuevo)
            datos = input("Los datos ingresados son correctos?: (si), (no)")
            if (datos == "si"):
                print ("En un momento seras redireccionado al menu de inicio, espera porfavor")
                menuR = 0
            else :
                menuR = input("Vuelve a realizar el registro porfavor (si), (no)")
                menuR =+1 
