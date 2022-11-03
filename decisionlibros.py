"""
    Autores: Sebastian Denhi Vega Saint Martin A01637397
    Fecha: 07/10/2022
    Descripcion: -----
"""
def dbcall():
    import pandas as pd
    libros = pd.read_excel('DBlibros.xlsx')
    return libros

def dbcallnombres():
    import pandas as pd
    nombres = pd.read_excel("DBnombres.xlsx").set_index('Usuarios',drop=False)
    return nombres

def bookfromdb(libros,booklist,grupo):
    from random import randint
    for i in range(len(booklist)):
                book = libros.at[libros.index[randint(0,8)],booklist[i]+grupo]
                while book == booklist[i-1] or book==booklist[i-2]:
                    book = libros.at[libros.index[randint(0,8)],booklist[i]+grupo]
                booklist.insert(i,book)
                booklist.pop(i+1)
    return booklist

def validansnum():
    while True:
        try:
            answer = int(input("Ingresa tu respuesta: "))
        except ValueError:
            print("Debes escribir un número del 1 al 5.")
            continue

        if answer not in range(1,6):
            print("Debes escribir un número del 1 al 5.")
            continue
        else:
            break
    return answer

def cuestionariolectura():
    contador = 0
    print("\n------PRIMER CUESTIONARIO------"
          "\nEste primer cuestionario es para determinar tu nivel de lectura."
          "\nContesta las siguientes preguntas con un numero del 1 al 5 dependiendo la frecuencia con la que las hagas"
          "\nSiendo 5=MUY FRECUENTE Y 1=NUNCA\n")
    
    print("Que tanto has leido durante tu vida?")
    contador += validansnum()
    print("\nQue tan frecuente es que personas de tu circulo cercano lean?")
    contador += validansnum()
    print("\nCuanto crees que un libro es mejor a una pelicula?")
    contador += validansnum()
    print("\nCada cuanto te llama la atencion un libro?")
    contador += validansnum()
    return contador

def cuestionariogustos():
    contadormate = 0
    contadordrama = 0
    contadorciencia = 0
    print("\n-----SEGUNDO CUESTIONARIO-----"
          "\nEl siguiente cuestionario es para determinar tus gustos y/o necesidades"
          "\nContesta las siguientes preguntas con un numero del 1 al 5 dependiendo la frecuencia con la que las hagas"
          "\nSiendo 5=MUY FRECUENTE Y 1=NUNCA\n")
    print("¿Que tan frecuente es que obtengas malas calificaciones en Matematicas?")
    contadormate += validansnum()
    print("¿Que tan seguido pasas imaginandote historias en tu cabeza?")
    contadordrama += validansnum()
    print("¿Con que frecuencia haces preguntas sobre el mundo que te rodea?")
    contadorciencia += validansnum()
    print("¿Con que frecuencia usas mas la intuicion que la logica?")
    contadormate += validansnum()
    print("¿Con que frecuencia has pensado convertirte en director/actor de cine?")
    contadordrama += validansnum()
    print("¿Con que frecuencia has hecho experimentos durante tu vida?")
    contadorciencia += validansnum()
    print("¿Con que frecuencia te cuesta identificar patrones en las cosas?")
    contadormate += validansnum()
    print("¿Que tan seguido te cuesta trabajo encontrar la idea principal de un texto?")
    contadordrama += validansnum()
    print("¿Que tan seguido ves documentales en Nat Geo/Discovery Channel?")
    contadorciencia += validansnum()
    print("¿Con que frecuencia piensas en clase de matematicas (¿Esto de que me va a servir?)")
    contadormate += validansnum()
    print("¿Que tanto crees que usas un vocabulario *Amplio*?")
    contadordrama += validansnum()
    print("¿Con que frecuencia obtienes malas calificaciones en (Biologia/Quimica/Fisica)?")
    contadorciencia += validansnum()
    
    return contadormate,contadordrama,contadorciencia
    
    
def determgroup(cuestionario1):
    if cuestionario1 in range(15, 21):
        grupo = "A"
    elif cuestionario1 in range(5,16):
        grupo = "I"
    else:
        grupo = "F"
    return grupo
        
def determbookchoice(mate,drama,ciencia):
    booklist = []
    from random import randint
    if mate in range(15, 21) and ciencia < 15 and drama < 15:
        booklist = ["Mate","Mate","Mate"]
    elif drama in range(15, 21) and ciencia < 15 and mate < 15:
        booklist = ["Drama","Drama","Drama"]
    elif ciencia in range(15, 21) and mate < 15 and drama < 15:
        booklist = ["Ciencia","Ciencia","Ciencia"]
        
    elif mate in range(5, 16) and ciencia < 5 and drama < 5:
        booklist = ["Mate","Mate","Mate"]
    elif drama in range(5, 16) and ciencia < 5 and mate < 5:
        booklist = ["Drama","Drama","Drama"]
    elif ciencia in range(5, 16) and mate < 5 and drama < 5:
        booklist = ["Ciencia","Ciencia","Ciencia"]
        
    elif mate in range(15, 21) and drama in range(15,21) and ciencia < 15:
        if mate > drama:
            booklist = ["Mate","Drama","Mate"]
        elif drama > mate:
            booklist = ["Mate","Drama","Drama"]
        else:
            randomnum = randint(1,2)
            if randomnum == 1:
                booklist = ["Mate","Drama","Mate"]
            else:
                booklist = ["Mate","Drama","Drama"]
    elif mate in range(15, 21) and ciencia in range(15,21) and drama < 15:
        if mate > ciencia:
            booklist = ["Mate","Ciencia","Mate"]
        elif ciencia > mate:
            booklist = ["Mate","Ciencia","Ciencia"]
        else:
            randomnum = randint(1,2)
            if randomnum == 1:
                booklist = ["Mate","Ciencia","Mate"]
            else:
                booklist = ["Mate","Ciencia","Ciencia"]
    elif drama in range(15, 21) and ciencia in range(15,21) and mate < 15:
        if drama > ciencia:
            booklist = ["Drama","Ciencia","Drama"]
        elif ciencia > drama:
            booklist = ["Drama","Ciencia","Ciencia"]
        else:
            randomnum = randint(1,2)
            if randomnum == 1:
                booklist = ["Drama","Ciencia","Drama"]
            else:
                booklist = ["Drama","Ciencia","Ciencia"]
    else:
        booklist = ["Mate","Ciencia","Drama"]
    
    return booklist
    
def printbooklist(booklistdone):
    for i in range(len(booklistdone)):
        print(booklistdone[i])
        

def main():
    libros = dbcall()
    cuestionario1 = cuestionariolectura()
    mate,drama,ciencia = cuestionariogustos()
    
    booklistnums = determbookchoice(mate,drama,ciencia)
    grupo = determgroup(cuestionario1)
    booklistdone = bookfromdb(libros,booklistnums,grupo)
    print("\nDespues de analizar tus gustos y necesidades encontramos estos 3 libros para ti, ojala los disfrutes")
    printbooklist(booklistdone)

