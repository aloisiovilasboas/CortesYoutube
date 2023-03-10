import yt_dlp
import subprocess

# Defina as opções de download
ydl_opts = {
    'outtmpl': 'video.mp4', # nome do arquivo de saída
}

# Defina o início e fim do clipe a ser baixado (em segundos)
start_time = 30
end_time = 60

# Obtenha a URL do vídeo
video_url = 'https://www.youtube.com/watch?v=zcrUT4GJAx8'

# Crie um objeto YoutubeDL e inicie o download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

# Use o FFmpeg para cortar o clipe desejado
# subprocess.run(['ffmpeg', '-i', 'video.mp4', '-ss', str(start_time), '-to', str(end_time), '-c', 'copy', 'clip.mp4'], check=True, shell=True)

# Remova o arquivo completo de vídeo (opcional)
# subprocess.run(['rm', 'video.mp4'], check=True)
