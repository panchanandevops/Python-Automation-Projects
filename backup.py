import os
import shutil
import datetime
import schedule
import time

# Configuration variables
SOURCE_DIR = "/home/panchanan/Pictures/IMG"
DESTINATION_DIR = "/home/panchanan/Pictures/Backups"
BACKUP_TIME = "02:46"  # Time to run the backup in HH:MM format

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Backup completed: {dest_dir}")
    except FileExistsError:
        pass  # Silent on folder exists
    except Exception as e:
        print(f"Error copying folder: {e}")

# Schedule the backup
schedule.every().day.at(BACKUP_TIME).do(lambda: copy_folder_to_directory(SOURCE_DIR, DESTINATION_DIR))

while True:
    schedule.run_pending()
    time.sleep(60)
