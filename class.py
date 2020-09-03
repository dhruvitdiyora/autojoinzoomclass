import schedule
import time
import webbrowser

def openRHC():
    webbrowser.open('https://us04web.zoom.us/j/5050947651?pwd=UEY3aUMxK1ZvNkIvTUcxVFFTa1VCUT09',new=2)
def openSKM():
    webbrowser.open('https://us04web.zoom.us/j/4879377543?pwd=bUx3cGtrOFlJVUFjNjU3Sld4dHZKQT09',new=2)
def openANP():
    webbrowser.open('https://zoom.us/j/7134521253?pwd=REJlYW5hZFd0dEY4bEZNSTFHNWg3dz09',new=2)
def openJAK():
    webbrowser.open('https://zoom.us/j/3263890862?pwd=ay9OVWloUVFzTWVhWWhWeHBzUWI0UT09',new=2)

print("script started running")
#monday
schedule.every().monday.at('09:15').do(openSKM)
schedule.every().monday.at('10:09').do(openRHC)
schedule.every().monday.at('13:50').do(openRHC)
#tuesday
schedule.every().tuesday.at('09:15').do(openANP)
schedule.every().tuesday.at('12:55').do(openRHC)
schedule.every().tuesday.at('13:50').do(openSKM)
#wednesday
schedule.every().wednesday.at('09:15').do(openJAK)
schedule.every().wednesday.at('10:10').do(openANP)
schedule.every().wednesday.at('11:05').do(openRHC)
schedule.every().wednesday.at('13:50').do(openANP)
#thursday
schedule.every().thursday.at('09:15').do(openJAK)
schedule.every().thursday.at('12:55').do(openSKM)
schedule.every().thursday.at('13:50').do(openJAK)
#friday
schedule.every().friday.at('12:55').do(openANP)
while True:
    schedule.run_pending()
    time.sleep(1)
