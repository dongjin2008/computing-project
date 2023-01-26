from pytube import YouTube

class vid_installer:
    def __init__(self):
        self.link = ""
    
    def get_link(self):
        self.link = input("Enter the YouTube URL: ")
    
    def download_vid(self):
        vid = YouTube(self.link).streams.get_highest_resolution()
        print("Downloading...")
        vid.download()
        print("Your video is downloaded in current location!")
    
    def main(self):
        self.get_link()
        self.download_vid()

def VidDownloader():
    vid_installer().main()

        

