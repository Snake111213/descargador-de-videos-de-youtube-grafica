from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import threading

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

def descargar(opcion, url, ruta_descarga, progress_bar):
    try:
        def progress_callback(stream, chunk, bytes_remaining):
            progress = (stream.filesize - bytes_remaining) / stream.filesize * 100
            progress_bar["value"] = progress
            root.update_idletasks()

        # Crear un objeto YouTube
        video = YouTube(url, on_progress_callback=progress_callback)

        if opcion == 1:
            # Obtener la mejor resolución disponible para video
            stream = video.streams.get_highest_resolution()
        elif opcion == 2:
            # Obtener la mejor resolución del audio disponible
            stream = video.streams.filter(only_audio=True).first()

        # Descargar el video o audio
        stream.download(output_path=ruta_descarga)

        print(f'Descarga de {"video" if opcion == 1 else "audio"} completada.')

    except Exception as e:
        print(f'Ocurrió un error al descargar el {"video" if opcion == 1 else "audio"}: {str(e)}')

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

    progress_bar["value"] = 0.0

    # Crear y ejecutar un hilo para descargar
    thread_descarga = threading.Thread(target=descargar, args=(opcion, urls[0], ruta_descarga, progress_bar))
    thread_descarga.start()

# Crear ventana principal
root = tk.Tk()
root.title("Music")

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

# Barra de progreso
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack()

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
