import tkinter
import tkinter.filedialog
from tkinter.messagebox import showinfo
from clases import *

def graficos():
    global direccion
    direccion = "Ninguna"
    #*******************************************FUNCIONES*****************************************
    def eliminarFrame(frame):
        for frame in main_frame.winfo_children():
            frame.destroy()
    def Cerrar():
        exit()
    def mostrar_ventana_emergente():
        ventana_emergente = tkinter.Toplevel(main_frame)
        ventana_emergente.title("Ventana Emergente")
        etiqueta = tkinter.Label(ventana_emergente, text="¡Esta es una ventana emergente!")
        etiqueta.pack(padx=20, pady=10)
        boton_cerrar = tkinter.Button(ventana_emergente, text="Cerrar", command=ventana_emergente.destroy)
        boton_cerrar.pack(pady=10)
    def CrearArchivo(texto, filename):
        global direccion
        texto = filename + texto + ".txt"
        print(texto)
        if filename != "":
            archivo = open(texto, "w")
            archivo.writelines(
                "*Mi_Dinero\nReal: 0\nLiquido: 0\n*Debo\nTotal: 0\n*Me_Deben\nTotal: 0\n***Ahorros***\ncant_ahorros:0\n***Transacciones***")
            archivo.close()
            direccion = texto
            try:
                etiqueta_dir.configure(text="Directorio: " + direccion)
                dir = open("dir.txt", "w")
                dir.writelines(direccion)
                dir.close()
            except:
                AbrirAuto()
        else:
            mostrar_ventana_emergente()
        Home(main_frame)
    def ExaminarDireccion(texto_direccion):
        filename = tkinter.filedialog.askdirectory(initialdir="/", title="Seleccione la ubicación")
        texto = filename + "/"
        texto_direccion.insert(0, texto)
        print(texto)
    def AbirArchivo():
        global direccion
        filename = tkinter.filedialog.askopenfilename(initialdir="/", title="Seleccione la Cuenta",
                                                     filetypes=[("archivo txt", "*.txt")])
        if filename != "":
            direccion = filename
            etiqueta_dir.configure(text="Directorio: " + direccion)
            dir = open("dir.txt", "w")
            dir.writelines(direccion)
            dir.close()
            Home(main_frame)
    def AbrirAuto():        #TEST
        global direccion
        try:
            dir = open("dir.txt", "r")
            direccion = dir.readline()
            dir.close()
            archivo = open(direccion)
            archivo.close()
        except:
            dir = open("dir.txt", "w")
            direccion = "Ninguna"
            dir.writelines(direccion)
            dir.close()
        etiqueta_dir.configure(text="Directorio: " + direccion)
        Home(main_frame)
    def Entrar(E, entry):
        if(E.get() != ""):
            entry += int(E.get())
        E.delete(0, "end")
        E.insert(0, entry)
        return
    def EntradaTransaccion(entry_texto, entry_monto, cuadro):
        global direccion
        texto = entry_texto.get()
        monto = entry_monto.get()
        entry_texto.delete(0, "end")
        entry_monto.delete(0, "end")
        if(direccion != "Ninguna"):
            texto = "\n//" + texto + ":\t\t\t\t\t\t\t" + monto
            archivo = open(direccion, "r+")
            archivo.writelines(texto)
            archivo.readline()
            print(archivo.readline())
            archivo.close()
            entry_texto.config()
            leerDato(cuadro, 10, 1, 1)
    def leerDato(cuadro, desde, hasta, offset):
        archivo = open(direccion, "r")
        texto = ""
        if(offset != 0):
            hasta = len(archivo.readlines())-10
            archivo.close()
            archivo = open(direccion, "r")
        for I in range(desde):
            archivo.readline()
        for I in range(hasta):
            texto += archivo.readline()
        archivo.close()
        if(offset == 0):
            cuadro.config(text=texto)
        else:
            cuadro.configure(state='normal')
            cuadro.delete("1.0", "end")
            cuadro.insert("end", texto)
            cuadro.see("end")
            cuadro.configure(state='disabled')              
    def OpenFile():
        global direccion
        if (direccion != "Ninguna"):
            archivo = open(direccion, "r+")
            return archivo
    def NuevoDeudor(entry, lista):
        if (entry.get() == ""):
            showinfo('Completa', 'Complete el nombre del nuevo deudor')
        else:
            texto = '<Deudor_Nuevo>' + entry.get()
            entryAux = tkinter.Entry()
            entryAux.insert(0, texto)
            entry.delete(0, "end")
            entry.insert(0, 0)
            EntradaTransaccion(entryAux,entry,tkinter.Text())
            Listar(lista, 2, 0, "<Deudor_Nuevo>", 0, 0)
            VerCuenta(main_frame)
    def EliminarDeudor(indice, lista):
        if(indice == ()):
            showinfo('Selección', 'Seleccione un deudor')
        else:
            Deudor = "<Deudor_Nuevo>" + lista.get(indice)
            try:
                with open(direccion, 'r') as fr:
                    lines = fr.readlines()

                    with open(direccion, 'w') as fw:
                        for line in lines:
                            if line.find(Deudor) == -1:
                                fw.write(line)
                print("Deleted")
                Listar(lista, 2, 0, "<Deudor_Nuevo>", 0, 0)
                VerCuenta(main_frame)
            except:
                print("Oops! something error")
    def EliminarDeuda(indice, lista, lista_Deudores):
        if(indice == ()):
            showinfo('Selección', 'Seleccione una deuda')
        else:
            Deuda = "<" + lista.get(indice) + ">"
            try:
                with open(direccion, 'r') as fr:
                    lines = fr.readlines()

                    with open(direccion, 'w') as fw:
                        for line in lines:
                            if line.find(Deuda) == -1:
                                fw.write(line)
                print("Deleted")
                Listar(lista, 2, 2, lista_Deudores, 1, indice)
                VerCuenta(main_frame)
            except:
                print("Oops! something error")
    def AggDeuda(entry_coment, entry_mont, lista, indice, lista_2):
        if (indice == ()):
            showinfo('Selección', 'Seleccione un deudor')
        elif (entry_mont.get() == ""):
            showinfo('Monto', 'Complete el monto')
        else:
            Deudor = "<" + lista.get(indice) + ">" + entry_coment.get()
            entry_coment.delete(0, "end")
            entry_coment.insert(0, Deudor)
            Cuadro = tkinter.Text()
            EntradaTransaccion(entry_coment, entry_mont, Cuadro)
            Listar(lista_2, 2, 2, lista, 1, lista.curselection())
            VerCuenta(main_frame)
    def Listar(lista, num_1, num_2, buscarL, offset, indice):
        if(indice == ()):
            showinfo('Selección', 'Seleccione un deudor')
        else:
            lista.delete(0, "end")
            archivo = OpenFile()
            deudaPerCapita = 0
            aux = "Vacío"
            if(offset == 0):
                buscar = buscarL
            else:
                buscar = '<' + buscarL.get(indice) + '>'
            while (aux != ""):
                aux = archivo.readline()
                if aux.find(buscar) != -1 and offset == 0:
                    lista.insert(0, aux.partition(buscar)[num_1].partition(":")[num_2])
                if aux.find(buscar) != -1 and offset == 1:                                                              #OPTIMIZABLE
                    insertar = aux.partition(buscar)[num_1]
                    deudaPerCapita += int(aux.partition(buscar)[num_1].partition(":")[num_2])
                    lista.insert(0, insertar)
            archivo.close()
            if(offset == 1):
                lista.insert("end", "Total: "+str(deudaPerCapita))
    def Calcular():
        suma = 0
        lista = tkinter.Listbox()
        Listar(lista, 2, 0, "<Deudor_Nuevo>", 0, 0)
        indice_max = lista.size()
        lista_2 = tkinter.Listbox()
        for I in range(indice_max):
            Listar(lista_2, 2, 2, lista, 1, I)
            indice_max_2 = lista_2.size()
            for J in range(indice_max_2):
                aux = lista_2.get(J)
                if(aux.find('Total:') != -1):
                    suma += int(aux.partition(':')[2])
        return suma
    #*********************************************************************************************

    #*******************************************VENTANA*******************************************
    ventana = tkinter.Tk()
    ventana.geometry("1015x450")
    ventana.title("Billetera")
    ventana.config(bg="#c3c3c3")
    ventana.resizable(0, 0)

    etiqueta_dir = tkinter.Label(ventana, text="Directorio: " + direccion, bg="#c3c3c3")
    etiqueta_dir.pack(side="bottom", anchor="w")

    main_frame = tkinter.Frame(ventana, bg="#c3c3c3")
    main_frame.pack()
    main_frame.pack_propagate(False)
    main_frame.configure(width=1015, height=450)

    photo1 = tkinter.PhotoImage(file="img1.GIF")
    photo2 = tkinter.PhotoImage(file="img2.GIF")
    photo3 = tkinter.PhotoImage(file="img3.GIF")

    #*********************************************************************************************

    #****************************************BARRA DE MENU****************************************
    barraMenu = tkinter.Menu(ventana)
    ventana.config(menu=barraMenu, width=300, height=300)  # Borrar width y height

    archivoMenu = tkinter.Menu(barraMenu, tearoff=0)
    archivoMenu.add_command(label="Nuevo", command=lambda: CrearCuenta(main_frame))
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Abrir", command=AbirArchivo)
    archivoMenu.add_command(label="Guardar como...")
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Cerrar", command=Cerrar)

    herramientasMenu = tkinter.Menu(barraMenu, tearoff=0)
    herramientasMenu.add_command(label="Crear Ahorro")
    herramientasMenu.add_command(label="Modificar Ahorro")
    herramientasMenu.add_command(label="Eliminar Ahorro")
    herramientasMenu.add_separator()
    herramientasMenu.add_command(label="Visualizar Cuentas")
    herramientasMenu.add_command(label="Emitir Informe")

    ayudaMenu = tkinter.Menu(barraMenu, tearoff=0)
    ayudaMenu.add_command(label="Acerca de...")

    barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
    barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
    barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
    #*********************************************************************************************

    #****************************************HOME*************************************************
    def Home(frame):
        eliminarFrame(frame)

        etiqueta = tkinter.Label(main_frame, text="Cuentas", bg="#800000", font="Courier 30 bold", fg="white", padx=500, pady=0)
        etiqueta.pack(fill=tkinter.X)
        etiqueta.place(x=-70, y=0)

        boton1 = tkinter.Button(main_frame, text="Nueva Cuenta", padx=40, pady=20, font="Courier 17 bold",
                                bg="#dcdce6", bd=0, command=lambda: CrearCuenta(main_frame))
        boton1.place(x=20, y=300)

        boton2 = tkinter.Button(main_frame, text="Ver Actual", padx=110, pady=20, font="Courier 17 bold", bg="#dcdce6",
                                bd=0, command=lambda: VerCuenta(main_frame))
        boton2.place(x=320, y=300)

        boton3 = tkinter.Button(main_frame, text="Abrir Cuenta", padx=40, pady=20, font="Courier 17 bold", bg="#dcdce6",
                                bd=0, command=AbirArchivo)
        boton3.place(x=730, y=300)

        if direccion == "Ninguna":
            boton2.config(state='disabled')

        i1 = tkinter.Label(main_frame, image=photo1).place(x=50, y=90)
        i2 = tkinter.Label(main_frame, image=photo2).place(x=415, y=90)
        i3 = tkinter.Label(main_frame, image=photo3).place(x=780, y=90)
    #*********************************************************************************************

    #****************************************CREAR AHORRO*****************************************
    def CrearAhorro(frame):
        eliminarFrame(frame)
        ca_frame = main_frame
        etiqueta = tkinter.Label(ca_frame, text="Crear Ahorro", bg="#800000", font="Courier 30 bold", fg="white", padx=500, pady=0)
        etiqueta.pack(fill=tkinter.X)
        etiqueta.place(x=-70, y=0)
        botonAtras = tkinter.Button(ca_frame, text="<", font="Helvetica", bd=0, padx=12, pady=12,
                                    command= lambda: Home(ca_frame), activebackground="light gray")
        botonAtras.pack()
        botonAtras.place(x=0, y=0)
        cuadro_estetico = tkinter.Label(ca_frame, padx=250, pady=60)
        cuadro_estetico.pack()
        cuadro_estetico.place(x=250, y=60)
        texto_etq = tkinter.Label(ca_frame, text="Nombre del Ahorro")
        texto_etq.pack()
        texto_etq.place(x=300, y=80)
        texto = tkinter.Entry(ca_frame, width=30, selectbackground='blue')
        texto.pack()
        texto.place(x=411, y=80)
        texto_etq2 = tkinter.Label(ca_frame, text="Cantidad de Ahorro")
        texto_etq2.pack()
        texto_etq2.place(x=300, y=110)
        texto2 = tkinter.Entry(ca_frame, width=30, selectbackground='blue')
        texto2.pack()
        texto2.place(x=411, y=110)
        boton_crearAhorro = tkinter.Button(ca_frame, text='Crear Ahorro')
        boton_crearAhorro.pack()
        boton_crearAhorro.place(x=411, y=140)
    #*********************************************************************************************

    #****************************************CREAR CUENTA*****************************************
    def CrearCuenta(frame):
        eliminarFrame(frame)
        etiqueta = tkinter.Label(main_frame, text="Crear Cuenta", bg="#800000", font="Courier 30 bold", fg="white", padx=500, pady=0)
        etiqueta.pack(fill=tkinter.X)
        etiqueta.place(x=-70, y=0)
        botonAtras = tkinter.Button(main_frame, text="<", font="Helvetica", bd=0, padx=12, pady=12,
                                    command=lambda: Home(main_frame), activebackground="light gray")
        botonAtras.pack()
        botonAtras.place(x=0, y=0)
        cuadro_nombreCuenta = tkinter.Label(main_frame, padx=250, pady=50)
        cuadro_nombreCuenta.pack()
        cuadro_nombreCuenta.place(x=250, y=60)
        label_nombreCuenta = tkinter.Label(main_frame, text="Nombre de la Cuenta")
        label_nombreCuenta.pack()
        label_nombreCuenta.place(x=300, y=80)
        texto_nombreCuenta = tkinter.Entry(main_frame, width=30, selectbackground='blue')
        texto_nombreCuenta.pack()
        texto_nombreCuenta.place(x=421, y=80)
        label_direccion = tkinter.Label(main_frame, text="Dirección")
        label_direccion.pack()
        label_direccion.place(x=300, y=110)
        texto_direccion = tkinter.Entry(main_frame, width=30, selectbackground="blue")
        texto_direccion.pack()
        texto_direccion.place(x=421, y=110)
        boton_examinar = tkinter.Button(main_frame, text="Examinar", command=lambda: ExaminarDireccion(texto_direccion))
        boton_examinar.pack()
        boton_examinar.place(x=619, y=105)
        boton_crearCuenta = tkinter.Button(main_frame, text='Crear Cuenta', command=lambda: CrearArchivo(texto_nombreCuenta.get(), texto_direccion.get()))
        boton_crearCuenta.pack()
        boton_crearCuenta.place(x=422, y=140)

    #*********************************************************************************************

    #****************************************VER_CUENTA*******************************************
    #Para evitar ERROR se debe evitar que se pueda acceder a esta ventana una vez se tenga la autorización de la dirección
    def VerCuenta(frame):
        Calcular()
        eliminarFrame(frame)
        etiqueta = tkinter.Label(main_frame, text="Ver Cuenta", bg="#800000", font="Courier 30 bold", fg="white", padx=500, pady=0)
        etiqueta.pack(fill=tkinter.X)
        etiqueta.place(x=-70, y=0)
        botonAtras = tkinter.Button(main_frame, text="<", font="Helvetica", bd=0, padx=12, pady=12,
                                    command=lambda: Home(main_frame), activebackground="light gray")
        botonAtras.pack()
        botonAtras.place(x=0, y=0)

        cuadrado_background = tkinter.Label(main_frame, width=86, height=20, bg="#8499ad", text="Agregar Transacción", font="Console 9 bold")
        cuadrado_background.place(x=200, y=100)
        cuadro_MiDinero = tkinter.Label(main_frame, width=20, height=3, bg="#dcdce6", text="Mi dinero:", font="Console 9 bold")
        cuadro_MiDinero.place(x=210, y=110)
        cuadro_MiDinero2 = tkinter.Label(main_frame, width=20, height=3, bg="#dcdce6", text="Real: 162.000\nLiquido: 172.000\n")
        cuadro_MiDinero2.place(x=210, y=155)
        leerDato(cuadro_MiDinero2, 1, 2, 0)
        cuadro_Debo = tkinter.Button(main_frame, width=20, height=3, bd=0, activebackground='#dcdce6', bg="#dcdce6",
                                     text="Debo:", font="Console 9 bold", command=Prestamos)
        cuadro_Debo.place(x=431, y=110)
        cuadro_Debo2 = tkinter.Button(main_frame, width=20, height=3, bd=0, activebackground='#dcdce6', bg="#dcdce6",
                                      text="Total: 20.000\n", command=Prestamos)
        cuadro_Debo2.place(x=431, y=155)
        leerDato(cuadro_Debo2, 4, 1, 0)
        cuadro_MeDeben = tkinter.Button(main_frame, width=20, height=3, bd=0, activebackground='#dcdce6', bg="#dcdce6",
                                        text="Me deben:", font="Console 9 bold", command=Prestamos)
        cuadro_MeDeben.place(x=652, y=110)
        cuadro_MeDeben2 = tkinter.Button(main_frame, width=20, height=3, bd=0, activebackground='#dcdce6', bg="#dcdce6",
                                         text="Total: 10.000\n", command=Prestamos)
        cuadro_MeDeben2.place(x=652, y=155)
        leerDato(cuadro_MeDeben2, 6, 1, 0)
        entrada_AggTransaccion = tkinter.Entry(main_frame, width=70, background="#dcdce6", bd=0, font="Courier 10")
        entrada_AggTransaccion.place(x=210, y=379)
        cuadro_Separador = tkinter.Label(main_frame, pady=1, bd=0)
        cuadro_Separador.place(x=630, y=379, height=17, width=34)
        entrada_AggMonto = tkinter.Entry(main_frame, width=13, background="#dcdce6", bd=0, font="Courier 10")
        entrada_AggMonto.place(x=664, y=379)
        def EnterAggtransaccion(event):
            EntradaTransaccion(entrada_AggTransaccion, entrada_AggMonto, cuadro_texto)
        entrada_AggTransaccion.bind('<Return>', EnterAggtransaccion)
        entrada_AggMonto.bind('<Return>', EnterAggtransaccion)
        boton_OK = tkinter.Button(main_frame, pady=1, bd=0, text="OK", activebackground="#dcdce6",
                                  command=lambda: EntradaTransaccion(entrada_AggTransaccion, entrada_AggMonto, cuadro_texto))
        boton_OK.place(x=742, y=379, height=18, width=55)
        deslizador = tkinter.Scrollbar(main_frame, orient='vertical')
        deslizador.place(x=779, y=270, height=102)
        cuadro_texto = tkinter.Text(main_frame, background="#dcdce6", bd=0, width=73, yscrollcommand=deslizador.set)
        cuadro_texto.place(x=210, y=270, height=102)
        deslizador.config(command=cuadro_texto.yview)
        deslizador.lift()
        leerDato(cuadro_texto, 10, 1, 1)
        cuadro_AhorroLb = tkinter.Label(main_frame, background="#8499ad", bd=0, width=27, text="Ahorros\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", font="Console 9 bold")
        cuadro_AhorroLb.place(x=5, y=100, height=306)
        cuadro_Ahorro = tkinter.Label(main_frame, bg="#dcdce6")
        cuadro_Ahorro.place(x=15, y=180, height=216, width=171)
        cuadro_DeudasLb = tkinter.Label(main_frame, background="#8499ad", bd=0, width=27, text="Deudas/Deudores\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", font="Console 9 bold")
        cuadro_DeudasLb.place(x=813, y=100, height=306)
        cuadro_Deudas = tkinter.Label(main_frame, bg="#dcdce6")
        cuadro_Deudas.place(x=823, y=180, height=216, width=171)
    #*********************************************************************************************

    #****************************************PRESTAMOS********************************************
    def Prestamos():
        win_1 = tkinter.Toplevel(ventana)
        win_1.geometry("225x450")
        win_1.title("Préstamos")
        win_1.config(bg="#8499ad")
        win_1.resizable(0, 0)
        win_1.grab_set()
        win_1.focus()

        #Ver deudores y deudas
        lista_Deudores = tkinter.Listbox(win_1)
        lista_Deudores.place(x=20, y=30, height=125, width=105)
        Listar(lista_Deudores, 2, 0, "<Deudor_Nuevo>", 0, 0)
        lista_Deudas = tkinter.Listbox(win_1)
        lista_Deudas.place(x=20, y=170, height=125, width=185)
        boton_ok = tkinter.Button(win_1, text=">>", font=("Courier"), bd=0, bg="#dcdce6",
                                  command=lambda:Listar(lista_Deudas, 2, 2, lista_Deudores, 1, lista_Deudores.curselection()))
        boton_ok.place(x=125, y=30, height=125, width=80)
        boton_eliminar_deudor = tkinter.Button(win_1,text="<<", bd=0, bg="gray", fg="white", font="Courier 8",
                                        command=lambda: EliminarDeudor(lista_Deudores.curselection(), lista_Deudores))
        boton_eliminar_deudor.place(x=104, y=30, height=125)

        #Agregar deuda
        entrada_deudaComent = tkinter.Entry(win_1, bd=0)
        entrada_deudaComent.place(x=20, y=320, width=185, height=21)
        tkinter.Label(win_1, text="   Comentario...", bg="#8499ad").place(x=10, y=295)
        entrada_deudaMont = tkinter.Entry(win_1, bd=0)
        entrada_deudaMont.place(x=20, y=368, width=156, height=21)
        boton_aggMont = tkinter.Button(win_1, text="Entrar", bd=0, font="Courier 8",
                                           command=lambda: AggDeuda(entrada_deudaComent, entrada_deudaMont, lista_Deudores, lista_Deudores.curselection(), lista_Deudas))
        boton_aggMont.place(x=156, y=368)
        tkinter.Label(win_1, text="   Monto...", bg="#8499ad").place(x=10, y=343)
        boton_eliminar_deuda = tkinter.Button(win_1, text="<<", bd=0, bg="gray", fg="white", font="Courier 8",
                                        command=lambda: EliminarDeuda(lista_Deudas.curselection(), lista_Deudas, lista_Deudores))
        boton_eliminar_deuda.place(x=184, y=170, height=125)

        #Nuevo Deudor
        def Mas(boton):
            if boton['text'] == '+':
                win_1.geometry("225x527")
                boton.config(text="-")
            else:
                win_1.geometry("225x450")
                boton.config(text="+")
        boton_Mas = tkinter.Button(win_1, text="+", font="Courier 18", bd=0)
        boton_Mas.place(x=95, y=410, height=30, width=30)
        boton_Mas.config(command=lambda: Mas(boton_Mas))
        tkinter.Label(win_1, text="   Agregar Nuevo Deudor...", bg="#8499ad").place(x=10, y=462)
        entrada_NuevoDeudor = tkinter.Entry(win_1, bd=0)
        entrada_NuevoDeudor.place(x=20, y=488, width=156, height=21)
        boton_aggNuevoDeudor = tkinter.Button(win_1, text="Entrar", bd=0, font="Courier 8",
                                       command=lambda: NuevoDeudor(entrada_NuevoDeudor, lista_Deudores))
        boton_aggNuevoDeudor.place(x=156, y=488)
    #*********************************************************************************************

    #****************************************INICIO***********************************************
    Home(main_frame)    #Abre la pantalla principal la primera vez
    AbrirAuto()         #TEST
    #*********************************************************************************************
    ventana.mainloop()
    #OBS: Para digitar código luego de mainloop, cambiar exit por ventana.destroy en Cerrar()
