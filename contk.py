from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def descargar_video(url, ruta_descarga='./'):
    try:
        # Crear un objeto YouTube
        video = YouTube(url)

        # Obtener la mejor resolución disponible
        stream = video.streams.get_highest_resolution()

        # Descargar el video
        print(f'Descargando video: {video.title}...')
        stream.download(output_path=ruta_descarga)
        print('Descarga de video completada.')

    except Exception as e:
        print(f'Ocurrió un error al descargar el video: {str(e)}')

def descargar_audio(url, ruta_descarga='./'):
    try:
        # Crear un objeto YouTube
        video = YouTube(url)

        # Obtener la mejor resolución del audio disponible
        stream = video.streams.filter(only_audio=True).first()

        # Descargar el audio
        print(f'Descargando audio de {video.title}...')
        stream.download(output_path=ruta_descarga, filename_prefix='audio')
        print('Descarga de audio completada.')

    except Exception as e:
        print(f'Ocurrió un error al descargar el audio: {str(e)}')

def seleccionar_ruta():
    ruta_descarga = filedialog.askdirectory()
    entry_ruta.delete(0, tk.END)
    entry_ruta.insert(0, ruta_descarga)

def iniciar_descarga():
    urls = entry_urls.get("1.0", tk.END).splitlines()
    ruta_descarga = entry_ruta.get()

    if not urls:
        print("No se proporcionaron URLs. Saliendo del programa.")
        return

    if not ruta_descarga:
        print("La ruta de descarga no puede estar vacía.")
        return

    opcion = var_opcion.get()

    for url in urls:
        if opcion == 1:
            descargar_video(url, ruta_descarga)
        elif opcion == 2:
            descargar_audio(url, ruta_descarga)

# Crear ventana principal
root = tk.Tk()
root.title("Descargador de YouTube")

# Crear elementos en la interfaz
label_urls = tk.Label(root, text="Ingresa las URLs de YouTube (una por línea):")
label_urls.pack()

entry_urls = tk.Text(root, height=5, width=50)
entry_urls.pack()

label_ruta = tk.Label(root, text="Selecciona la carpeta de descarga:")
label_ruta.pack()

entry_ruta = tk.Entry(root, width=40)
entry_ruta.pack()

button_seleccionar_ruta = tk.Button(root, text="Seleccionar Ruta", command=seleccionar_ruta)
button_seleccionar_ruta.pack()

label_opcion = tk.Label(root, text="Selecciona una opción:")
label_opcion.pack()

var_opcion = tk.IntVar()
radio_video = tk.Radiobutton(root, text="Descargar Videos", variable=var_opcion, value=1)
radio_video.pack()

radio_audio = tk.Radiobutton(root, text="Descargar Audios", variable=var_opcion, value=2)
radio_audio.pack()

button_descargar = tk.Button(root, text="Iniciar Descarga", command=iniciar_descarga)
button_descargar.pack()

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
