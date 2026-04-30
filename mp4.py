import os
import yt_dlp

def descargar_video(url, carpeta="wallpapers"):
    # Crear carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    opciones = {
        'outtmpl': f'{carpeta}/%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4',
        'quiet': False
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("Video listo para usar ")
    except Exception as e:
        print(f" Error: {e}")


if __name__ == "__main__":
    url = input("URL de YouTube: ")
    descargar_video(url)