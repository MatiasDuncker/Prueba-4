STOCK_LosFortificados=500
STOCK_LosIluminados=500
Lista_LosFortificados=[]
Lista_LosIluminados=[]

def Validacion_String(Mensaje:str):
    while True:
        String=input(Mensaje)
        String_Real=String.strip()
        if len(String_Real)==0:
            print("Error, no puede dejar el texto vacio")
            continue
        else:
            break
    return(String_Real)

def Validacion_NumerEntero(Mensaje:str):
    while True:
        try:
            entero=int(input(Mensaje))
            break
        except ValueError:
            print("Error, porfavor ingrese un numero entero mayor a 0")
            continue
    return(entero)

def compra_LosFortificados(Mensaje:str):
    print(Mensaje)

    while True:
        Repeticion=False
        Nombre_Comprador=Validacion_String("Ingrese un nombre")
        if Nombre_Comprador in Lista_LosFortificados:
            print("Error, no puede aver dos entradas con el mismo nombre")
            Repeticion=True
        if Repeticion==False:
            break

    while True:
        Tipo_Entrada=Validacion_String("Ingrese cual entrada quiere comprar (G/V)")
        if Tipo_Entrada.lower()!="g" and Tipo_Entrada.lower()!="v":
            print("Error, Debe ingresar si su entrada es G (Galeria) o V (VIP) para registrar que entrada quiere")
            continue
        else:
            break

    while True:
            Codigo=Validacion_String("Ingrese un codigo de confirmacion")
            if len(Codigo)!=6 or any(i.isupper() for i in Codigo)  == False or " " in Codigo:
                print("Error su codigo no es valido intente de nuevo")
                continue
            else: 
                break
            
     
    Lista_LosFortificados.append(Nombre_Comprador)
    return(print("Su entada a sido registrada con exitio para Los Fortificados"))
    
    
        
         
def compra_LosIluminados(Mensaje:str):
       while True:
        Repeticion=False
        Nombre_Comprador=Validacion_String("Ingrese un nombre")
        if Nombre_Comprador in Lista_LosFortificados:
            print("Error, no puede aver dos entradas con el mismo nombre")
            Repeticion=True
        if Repeticion==False:
            break

        while True:
            Tipo_Entrada=Validacion_String("Ingrese cual entrada quiere comprar (CV/PAL)")
            if Tipo_Entrada.lower()!= "cv" and Tipo_Entrada.lower()!="pal":
                print("Error, Debe ingresar si su entrada es CV (Cancha VIP) o PAL (Palco) para registrar que entrada quiere")
                continue
            else:
                break

        while True:
            Codigo=Validacion_String("Ingrese un codigo de confirmacion")
            if len(Codigo)!=5 or " " in Codigo:
                print("Error su codigo no es valido intente de nuevo")
                continue
            else:
                mayusculas=0
                for i in Codigo:
                    if i.isupper():
                        mayusculas+=1
                if mayusculas<3:
                        print("codigo invalido intente denuevo, su codigo deve tener 3 mayusculas")
                        continue
                else:
                    print("Codigo valido")
                    break
        
        Lista_LosIluminados.append(Nombre_Comprador)
        return(print("Su entrada a sido registrada con exito para Los Iluminados"))
       

def Inprimir_Entradas(Mensaje:str):
    print(Mensaje)
    print("entradas disponibles para: ",STOCK_LosFortificados)
    print("entradas disponibles para: ",STOCK_LosIluminados)

def Salir(Mensaje:str):
    print("Saliendo del programa")

while True:
    print("Vienvenidos al totem de autoservicio de rock an chile")
    print("1. - Comprar entradas a Los Fortificados")
    print("2. - Comprar entradas a Los Iluminados")
    print("3. - Stock entrada para ambos conciertos")
    print("4. - Salir")

    opcion=Validacion_NumerEntero("Ingrese una opcion")

    if opcion == 1:
        compra_LosFortificados("A selecionado comprar una entrada a los Fortificados")
    elif opcion == 2:
        compra_LosIluminados("A selecionado comprar entradas para los Iluminados")
    elif opcion == 3:
        Inprimir_Entradas("A selecionado revisar el stock")
    elif opcion == 4:
        Salir("Saliendo del programa")
        break