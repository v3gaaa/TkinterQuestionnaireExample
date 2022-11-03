from tkinter import *
from tkinter import ttk
from decisionlibros import determgroup,dbcall,dbcallnombres,determbookchoice,bookfromdb

#Clase del cuestionario1
class Cuestionario:
    def __init__(self,root,index,value,questions,respuestas,instrucciones,cuest):
        self.questions = questions
        self.instrucciones = instrucciones
        self.cuest = cuest
        self.index = index
        self.value = value
        self.root = root
        self.respuestas = respuestas
        self.framec1 = Frame(self.root)
        self.framec1.place(height=300, width=700)
        self.framec1.place(x=0, y=0)
        self.instrucciones = ttk.Label(self.framec1,
                                        text=instrucciones[cuest],font=("Times", 12, "italic"))
        self.instrucciones.place(x=5,y=70)
        
        # Botón Sig. Pregunta
        self.siguiente = Button(root, 
            text="Siguiente Pregunta",
            font="Arial 17",
            fg="black",
            command=self.siguiente
            )
        self.siguiente.place(x=250,y=500)
   
    def agregar1(self):
        self.value = 1
        self.currentval.delete(0, END)
        self.currentval.insert(0, self.value)
        self.value = self.currentval.get()

    def agregar2(self):
        self.value = 2
        self.currentval.delete(0, END)
        self.currentval.insert(0, self.value)
        self.value = self.currentval.get()
        
    def agregar3(self):
        self.value = 3
        self.currentval.delete(0, END)
        self.currentval.insert(0, self.value)
        self.value = self.currentval.get()
        
    def agregar4(self):
        self.value = 4
        self.currentval.delete(0, END)
        self.currentval.insert(0, self.value)
        self.value = self.currentval.get()
        
    def agregar5(self):
        self.value = 5
        self.currentval.delete(0, END)
        self.currentval.insert(0, self.value)
        self.value = self.currentval.get()
        
    def siguiente(self):
        if self.value == None:
            pass
        else:
            self.value = int(self.value)
            self.respuestas.append(self.value)
        
        if self.value or self.index ==0:
            if self.index < len(self.questions[self.cuest]):
                self.index+=1
                self.framec1.destroy()
                self.framec1 = Frame(self.root)
                self.framec1.place(height=300, width=700)
                self.framec1.place(x=0, y=0)
                #Question Label
                self.question_label = ttk.Label(self.framec1,
                                        text=self.questions[self.cuest][self.index-1],font=("Times",14))
                self.question_label.place(x=150,y=40)
                
                self.currentval = ttk.Entry(self.framec1, width=25)
                self.currentval.place(x=275,y=100)
                
                
                #Botones del 1-5
                self.one = Button(self.framec1, 
                    text="1",
                    font="Arial 17",
                    fg="black",
                    command= self.agregar1
                    )
                self.one.place(x=125,y=200)

                self.two = Button(self.framec1, 
                    text="2",
                    font="Arial 17",
                    fg="black",
                    command= self.agregar2
                    )
                self.two.place(x=225,y=200)

                self.three = Button(self.framec1, 
                    text="3",
                    font="Arial 17",
                    fg="black",
                    command= self.agregar3
                    )
                self.three.place(x=325,y=200)

                self.four = Button(self.framec1, 
                    text="4",
                    font="Arial 17",
                    fg="black",
                    command= self.agregar4
                    )
                self.four.place(x=425,y=200)

                self.five = Button(self.framec1, 
                    text="5",
                    font="Arial 17",
                    fg="black",
                    command= self.agregar5
                    )
                self.five.place(x=525,y=200)
                self.value = None
            else:
                self.framec1.destroy()
                self.framec1 = Frame(self.root)
                self.framec1.place(height=700, width=700)
                self.framec1.place(x=0, y=0)
                # Botón Salir
                self.salir = Button(self.root, 
                    text="Siguiente ventana",
                    font="Arial 17", 
                    fg="black",
                    bg="white",
                    command=self.root.destroy
                    )
                self.salir.place(x=500,y=500)
                self.obtener_respuestas()
            
    def obtener_respuestas(self):
        global respuestas
        respuestas = self.respuestas
        return respuestas
    
def plant_cuest(questions,instrucciones,cuest):
    root = Tk()
    root.geometry('700x600')
    root.resizable(False, False)
    root.title('Programa de Mejora: PISA')
    respuestas = []
    index = 0
    value = None
    cuestionario = Cuestionario(root,index,value,questions,respuestas,instrucciones,cuest)
    root.mainloop()
    respuestascuest = respuestas
    del cuestionario
    return respuestascuest

def plant_menuinicio(nombres):
    root = Tk()
    root.geometry('700x600')
    root.resizable(False, False)
    root.title('Programa de Mejora: PISA')
    menuinicio = Menuinicio(root,nombres)
    root.mainloop()
    usuariof = usuario
    del menuinicio
    return usuariof
    
def separar_lista(respuestas2):
    mate= []
    ciencia=[]
    drama=[]
    for i in range(0,len(respuestas2)+1,3):
        if i == len(respuestas2):
            pass
        else:
            mate.append(respuestas2[i])
    for i in range(0,len(respuestas2)+1,3):
        if i == len(respuestas2):
            pass
        else:
            ciencia.append(respuestas2[i+1])
    for i in range(0,len(respuestas2)+1,3):
        if i == len(respuestas2):
            pass
        else:
            drama.append(respuestas2[i+2])
    return mate,ciencia,drama
          
def fin():
    quit()       
            
def guilibros_final(booklistdone,usuariof):
    root = Tk()
    root.geometry('700x600')
    root.resizable(False, False)
    root.title('Programa de Mejora: PISA')
    strbooklist = ",\n".join(booklistdone)
    mensaje_final = ttk.Label(root,
                                        text="Despues de analizar tus gustos y necesidades encontramos estos 3 libros para ti\n¡ojala los disfrutes!",
                                        font=("Times",14))
    mensaje_final.place(x=20,y=100)
    
    mensaje_final2 = ttk.Label(root,
                                        text="Quedaste registrado con el usuario: "+usuariof,
                                        font=("Times",14))
    mensaje_final2.place(x=20,y=150)
    
    libros_final = ttk.Label(root,
                                        text=strbooklist,font=("Times",13))
    libros_final.place(x=180,y=200)
    
    salir = Button(root, 
                    text="Salir",
                    font="Arial 17", 
                    fg="black",
                    bg="white",
                    command=fin
                    )
    salir.place(x=500,y=500)
    
    principal= Button(root, 
                    text="Menu Principal",
                    font="Arial 17", 
                    fg="black",
                    bg="white",
                    command=root.destroy
                    )
    principal.place(x=300,y=500)
    
    root.mainloop()
    
class Menuinicio:
    def __init__(self,root,nombres):
        self.nombres = nombres
        self.usuario = 0
        self.root = root
        self.text = "Iniciar Cuestionario"
        self.framec2 = Frame(self.root)
        self.framec2.place(height=700, width=700)
        self.framec2.place(x=0, y=0)
        self.inicio = ttk.Label(self.framec2,
                                            text="PROGRAMA DE MEJORA PISA",font=("Times", 15, "italic"))
        self.inicio.place(x=300,y=70)
        self.new_user = Button(self.framec2, 
                        text="Iniciar Cuestionario",
                        font="Arial 17", 
                        fg="black",
                        bg="white",
                        command= self.registronombre
                        )
        self.new_user.place(x=400,y=500)
        
        self.old_user = Button(self.framec2, 
                        text="Consultar libros",
                        font="Arial 17", 
                        fg="black",
                        bg="white",
                        command= self.consultarregistro)
        self.old_user.place(x=200,y=500)
        
        self.salir = Button(self.framec2, 
                        text="Salir",
                        font="Arial 17", 
                        fg="black",
                        bg="white",
                        command= fin)
        self.salir.place(x=100,y=500)
        
        
    def consultarregistro(self):
        self.framec2.destroy
        self.framec2 = Frame(self.root)
        self.framec2.place(height=700, width=700)
        self.framec2.place(x=0, y=0)
        self.registro = ttk.Label(self.framec2,
                        text="INGRESA TU USUARIO",font=("Times", 15, "italic"))
        self.registro.place(x=300,y=70)
        self.user = ttk.Entry(self.framec2, width=25)
        self.user.place(x=300,y=100)
    
        self.salir = Button(self.framec2, 
                text="Continuar",
                font="Arial 17", 
                fg="black",
                bg="white",
                command=self.destroyconsultar
                )
        self.salir.place(x=500,y=500)
    
    def destroyconsultar(self):
        self.usuario = self.user.get()
        if self.usuario and self.usuario in self.nombres.Usuarios.values:
            self.enseñarlibros()
        elif not self.usuario:
            self.framec2.destroy
            self.framec2 = Frame(self.root)
            self.framec2.place(height=700, width=700)
            self.framec2.place(x=0, y=0)
            self.registro = ttk.Label(self.framec2,
                            text="INGRESA TU USUARIO",font=("Times", 15, "italic"))
            self.registro.place(x=300,y=70)
            self.user = ttk.Entry(self.framec2, width=25)
            self.user.place(x=300,y=100)
            self.alerta = ttk.Label(self.framec2,
                            text="Ingrese un usuario antes de continuar",font=("Times",12))
            self.alerta.place(x=300,y=130)
        
            self.salir = Button(self.framec2, 
                    text="Continuar",
                    font="Arial 17", 
                    fg="black",
                    bg="white",
                    command=self.destroyconsultar
                    )
            self.salir.place(x=500,y=500)
        elif self.usuario not in self.nombres.Usuarios.values:
            self.framec2.destroy
            self.framec2 = Frame(self.root)
            self.framec2.place(height=700, width=700)
            self.framec2.place(x=0, y=0)
            self.registro = ttk.Label(self.framec2,
                            text="INGRESA TU USUARIO",font=("Times", 15, "italic"))
            self.registro.place(x=300,y=70)
            self.user = ttk.Entry(self.framec2, width=25)
            self.user.place(x=300,y=100)
            self.alerta = ttk.Label(self.framec2,
                            text="Este ustuario no existe",font=("Times",12))
            self.alerta.place(x=300,y=130)
        
            self.salir = Button(self.framec2, 
                    text="Continuar",
                    font="Arial 17", 
                    fg="black",
                    bg="white",
                    command=self.destroyconsultar
                    )
            self.salir.place(x=500,y=500)
        else:
            pass
   
    def enseñarlibros(self):
        self.framec2.destroy
        self.framec2 = Frame(self.root)
        self.framec2.place(height=700, width=700)
        self.framec2.place(x=0, y=0)
        self.inicio = ttk.Label(self.framec2,
                                            text="Los libros del usuario "+self.usuario+" son:",font=("Times", 15, "italic"))
        self.inicio.place(x=200,y=70)
        
        
        self.libros1 = ttk.Label(self.framec2,
                                            text=self.nombres["Libro1"][self.usuario],
                                            font=("Times", 12))
        self.libros1.place(x=200,y=130)
        self.libros2 = ttk.Label(self.framec2,
                                            text=self.nombres["Libro2"][self.usuario],
                                            font=("Times", 12))
        self.libros2.place(x=200,y=170)
        self.libros3 = ttk.Label(self.framec2,
                                            text=self.nombres["Libro3"][self.usuario],
                                            font=("Times", 12))
        self.libros3.place(x=200,y=210)
        
        self.new_user = Button(self.framec2, 
                        text="Salir",
                        font="Arial 17", 
                        fg="black",
                        bg="white",
                        command=fin
                        )
        self.new_user.place(x=500,y=500)
        
        self.principal= Button(self.framec2, 
                    text="Menu Principal",
                    font="Arial 17", 
                    fg="black",
                    bg="white",
                    command=self.root.destroy
                    )
        self.principal.place(x=300,y=500)
    
        
        self.obtener_usuario()
        
    def registronombre(self):
        self.framec2.destroy
        self.framec2 = Frame(self.root)
        self.framec2.place(height=700, width=700)
        self.framec2.place(x=0, y=0)
        self.registro = ttk.Label(self.framec2,
                        text="Registro",font=("Times", 15, "italic"))
        self.registro.place(x=300,y=70)
        self.user = ttk.Entry(self.framec2, width=25)
        self.user.place(x=300,y=100)
    
        self.salir = Button(self.framec2, 
                text="Continuar",
                font="Arial 17", 
                fg="black",
                bg="white",
                command=self.destroyrootregistro
                )
        self.salir.place(x=500,y=500)
            
    def destroyrootregistro(self):
        import pandas
        self.usuario = self.user.get()
        if self.usuario and self.usuario not in self.nombres.Usuarios.values:
            self.root.destroy()
            self.obtener_usuario()
        elif self.usuario in self.nombres.Usuarios.values:
            self.framec2.destroy
            self.framec2 = Frame(self.root)
            self.framec2.place(height=700, width=700)
            self.framec2.place(x=0, y=0)
            self.registro = ttk.Label(self.framec2,
                            text="Registro",font=("Times", 15, "italic"))
            self.registro.place(x=300,y=70)
            self.user = ttk.Entry(self.framec2, width=25)
            self.user.place(x=300,y=100)
            self.alerta = ttk.Label(self.framec2,
                            text="Este ustuario ya esta registrado",font=("Times",12))
            self.alerta.place(x=300,y=130)
        
            self.salir = Button(self.framec2, 
                    text="Continuar",
                    font="Arial 17", 
                    fg="black",
                    bg="white",
                    command=self.destroyrootregistro
                    )
            self.salir.place(x=500,y=500)
        elif not self.usuario:
            self.framec2.destroy
            self.framec2 = Frame(self.root)
            self.framec2.place(height=700, width=700)
            self.framec2.place(x=0, y=0)
            self.registro = ttk.Label(self.framec2,
                            text="Registro",font=("Times", 15, "italic"))
            self.registro.place(x=300,y=70)
            self.user = ttk.Entry(self.framec2, width=25)
            self.user.place(x=300,y=100)
            self.alerta = ttk.Label(self.framec2,
                            text="Ingrese un usuario antes de continuar",font=("Times",12))
            self.alerta.place(x=300,y=130)
        
            self.salir = Button(self.framec2, 
                    text="Continuar",
                    font="Arial 17", 
                    fg="black",
                    bg="white",
                    command=self.destroyrootregistro
                    )
            self.salir.place(x=500,y=500)
        else:
            pass
    
    def obtener_usuario(self):
        global usuario
        usuario = self.usuario
        return usuario
  
def registrolibros(nombres,booklistdone,usuariof):
    import pandas as pd
    libro1=booklistdone[0]
    libro2=booklistdone[1]
    libro3=booklistdone[2]
    d1 = {"Usuarios": [usuariof], "Libro1": [libro1], "Libro2":[libro2], "Libro3":[libro3]}
    df1 = pd.DataFrame(d1)
    nombres = pd.concat([nombres, df1],ignore_index=True)
    nombres.to_excel("DBnombres.xlsx",index = False)
    
def main():
    
    while True:
        nombres = dbcallnombres()
        usuariof = plant_menuinicio(nombres)
        if usuariof not in nombres.Usuarios.values:
            questions = [["Que tanto has leido durante tu vida?","Que tan frecuente es que personas de tu circulo cercano lean?" ,
                    "Cuanto crees que un libro es mejor a una pelicula?","Cada cuanto te llama la atencion un libro?"],
                    ["¿Que tan frecuente es que obtengas malas calificaciones en Matematicas?", "¿Que tan seguido pasas imaginandote historias en tu cabeza?",
                    "¿Con que frecuencia haces preguntas sobre el mundo que te rodea?","¿Con que frecuencia usas mas la intuicion que la logica?",
                    "¿Con que frecuencia has pensado convertirte en director/actor de cine?","¿Con que frecuencia has hecho experimentos durante tu vida?",
                    "¿Con que frecuencia te cuesta identificar patrones en las cosas?","¿Que tan seguido te cuesta trabajo encontrar la idea principal de un texto?",
                    "¿Que tan seguido ves documentales en Nat Geo/Discovery Channel?","¿Con que frecuencia piensas en clase de matematicas\n(¿Esto de que me va a servir?)",
                    "¿Que tanto crees que usas un vocabulario *Amplio*?","¿Con que frecuencia obtienes malas calificaciones en\n(Biologia/Quimica/Fisica)?"]]
        
            instrucciones = ["\n------PRIMER CUESTIONARIO------"
                        "\nEste primer cuestionario es para determinar tu nivel de lectura."
                        "\nContesta las siguientes preguntas con un numero del 1 al 5 dependiendo la frecuencia con la que las hagas"
                        "\nSiendo 5=MUY FRECUENTE Y 1=NUNCA\n","\n-----SEGUNDO CUESTIONARIO-----"
                        "\nEl siguiente cuestionario es para determinar tus gustos y/o necesidades"
                        "\nContesta las siguientes preguntas con un numero del 1 al 5 dependiendo la frecuencia con la que las hagas"
                        "\nSiendo 5=MUY FRECUENTE Y 1=NUNCA\n"]
        
            respuestas1 = plant_cuest(questions,instrucciones,0)
            respuestas2 = plant_cuest(questions,instrucciones,1)
            mate,drama,ciencia = separar_lista(respuestas2)
            mate = sum(mate)
            ciencia = sum(ciencia)
            drama = sum(drama)
            booklistnums = determbookchoice(mate,drama,ciencia)
            grupo = determgroup(sum(respuestas1))
            libros = dbcall()
            booklistdone = bookfromdb(libros,booklistnums,grupo)
            guilibros_final(booklistdone,usuariof)
            registrolibros(nombres,booklistdone,usuariof)
            
        else:
            pass
    
    
    
main()