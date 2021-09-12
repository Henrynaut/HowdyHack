import subprocess
import youtube_dl

def run():
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

    
if __name__ == '__main__':
    run()