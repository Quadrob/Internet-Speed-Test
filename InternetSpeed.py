#import modules and save an instance of it
import speedtest   
st = speedtest.Speedtest() 

#import time to wait after completion of
import time

#function to conver bytes to mega-bytes
def bytesToMegabytes(number):
    mb = number*0.000001
    return mb
#inform user
print("\nChecking your internet speed please wait...\n\n")

#display speeds
print("Your Download speed is :", bytesToMegabytes(st.download()), "mb")
print("Your Upload speed is :", bytesToMegabytes(st.upload()), "mb")

#get a server and test ping
st.get_servers([])
print("Your Ping is :", st.results.ping) 

#wait 15 secs before closing
time.sleep(15)