# this is a code to test script run
from datetime import datetime

# get current date
datetime_object = datetime.now()
print("You have successfully tested the script on", datetime_object.day, "of", datetime_object.strftime("%B"), datetime_object.year, "with exact timestamp of", datetime_object)
