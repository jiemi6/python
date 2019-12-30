import schedule
import time
import subprocess

def job():
    realJob()

def realJob():
    print("start smzdm scrapy...")
    subprocess.Popen("scrapy crawl smzdm", shell=True)


print("I'm working...")
#schedule.every().hour.do(job)
# schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
realJob()


while True:
    schedule.run_pending()
    time.sleep(1)