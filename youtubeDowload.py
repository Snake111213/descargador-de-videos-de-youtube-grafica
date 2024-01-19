from pytube import YouTube

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

if __name__ == "__main__":
    # URL del video de YouTube que deseas descargar
    url_youtube = input("Ingresa la URL de YouTube: ")

    # Menú de opciones
    print("Selecciona una opción:")
    print("1. Descargar Video")
    print("2. Descargar Audio")

    opcion = input()

    if opcion == '1':
        ruta_descarga = input("Ingresa la ruta de descarga para el video (deja en blanco para la carpeta actual): ").strip() or './'
        descargar_video(url_youtube, ruta_descarga)

    elif opcion == '2':
        ruta_descarga = input("Ingresa la ruta de descarga para el audio (deja en blanco para la carpeta actual): ").strip() or './'
        descargar_audio(url_youtube, ruta_descarga)

    else:
        print("Opción no válida. Selecciona 1 o 2.")
