import logging
import os
from datetime import datetime

#
#how should my logfile will be
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#path of my logfile
"""
   os.getcwd()-->current working directory
   evey file will start with logs
"""
logs_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
#Below code says even their is log file its going on appending
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
#if you want to create we need to set it
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO

)



