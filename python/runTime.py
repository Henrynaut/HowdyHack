import subprocess
import youtube_dl

def runTime(weblink='https://www.youtube.com/watch?v=dQw4w9WgXcQ'):
    video_url = input("please enter URL:")
    video_info  = youtube_dl.YoutubeDL().extract_info(
        url = video_url, download = False
    )
    filename = f"{video_info['title']}"
    options = {
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmp1': filename,
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'wav', #switch file type here
            'preferredquality':'192',
        }]
    } 
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    subprocess.call(["open",filename])
    
    return f"{video_info['title']}"