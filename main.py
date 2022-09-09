from pytube import YouTube
import os
import sys


def main():
    link = sys.argv[1]
    try:
        yt = YouTube(link)
        video_type = yt.streams.get_highest_resolution()
        video_type.download(f"{os.curdir}/videos")
    except:
        sys.exit("Not a Valid Youtube URL, exiting...")


if __name__ == '__main__':
    main()