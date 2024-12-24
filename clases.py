import tkinter
import tkinter.filedialog


class Archivo():
    def __init__(self, filename, modo):
        self.filename = filename
        self.archivo = open(filename, modo)
    def crearArchivo(self, texto, etiqueta_dir, AbrirAuto):
        filename = tkinter.filedialog.askdirectory(initialdir="/", title="Seleccione la ubicación")
        texto = filename + "/" + texto + ".txt"
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