#code 
from pytube import YouTube
from plyer import notification
import tkinter as tk
from tkinter import filedialog

#Function to select download path
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

#Function for progress bar in command prompt
def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = video.filesize
    size = contentsize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')


    
try:
    root = tk.Tk()
    root.withdraw()

    #taking link as input
    link = input("Enter YouTube video link : ")

    #setting download path
    download_path = open_file_dialog()

    if download_path:   

        #creating object of YouTube class
        yt=YouTube(link,on_progress_callback=progress)

        #Calculating file size
        File_size=yt.streams.get_highest_resolution().filesize_mb

        #Slicing video title into small title of length 50 for notification
        small_title = (yt.title)[:50] if (len(yt.title)>50) else yt.title

        #Notifing user
        notification.notify(
            title = f"Downloading {small_title}",
            message = f"File size : {File_size} mb",
            app_icon = "pythonlogoIco.ico",
            timeout = 2
        )

        #Getting highest resolution of video
        video=yt.streams.get_highest_resolution()

        #Downloading the video
        video.download(output_path=download_path)

        #Notifing user
        notification.notify(
            title = small_title,
            message = f"Download complete \n {download_path}",
            app_icon = "pythonlogoIco.ico",
            timeout = 3
        )

    else:
        print("Invalid download path")
    
except Exception as e:
    print(f"\n An error occured : {e}")
