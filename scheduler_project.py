import os
import shutil
import logging
import schedule
logging.basicConfig(filename="logs.txt", level="INFO")
def check_disk():
    disk = shutil.disk_usage('/')
    per_used = (disk.total - disk.free)/disk.total*100
    if per_used > 15:
        logging.warning("disk is going high")
    elif per_used > 14:
        logging.info("it's okay you have more space now")

check_disk()
schedule.every(10).seconds.do(check_disk)
while True:
    schedule.run_pending()
    