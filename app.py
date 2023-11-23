from pytube import Playlist
from moviepy.editor import AudioFileClip
import os

playlist = input("Enter the playlist URL: ")

p = Playlist(playlist)
numberOfProcess = 1

for video in p.videos:
    print("processing ", numberOfProcess, " of ", len(p.videos))
    numberOfProcess += 1
    audio_file = video.streams.filter(only_audio=True).first().download()
    clip = AudioFileClip(audio_file)
    clip.write_audiofile(audio_file.replace(".mp4", ".mp3"))
    clip.close()
    os.remove(audio_file)