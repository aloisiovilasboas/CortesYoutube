from moviepy.editor import *

def cortar_video_youtube(link, tempo_inicio, tempo_final):
    
    # carregar o vídeo do YouTube como um objeto VideoFileClip
    video = VideoFileClip(link)

    # cortar o vídeo do tempo de início ao tempo final
    print(f"Tamanho do vídeo: {video.size}")
    video_cortado = video.subclip(tempo_inicio, tempo_final)

    

    # retornar o vídeo cortado
    return video_cortado

# definir o link do vídeo, tempo de início e tempo final
link = "https://www.youtube.com/watch?v=HLogAbuG3wo"
tempo_inicio = 10  # segundos
tempo_final = 20  # segundos

# cortar o vídeo do YouTube
video_cortado = cortar_video_youtube(link, tempo_inicio, tempo_final)
txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
             .set_position('center')
             .set_duration(10) )

result = CompositeVideoClip([video_cortado, txt_clip]) # Overlay text on video

# salvar o vídeo cortado em um arquivo
result.write_videofile("myHolidays_edited.webm",fps=25)
