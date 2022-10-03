from datetime import datetime
import pytz


bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogota: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

py_timezone = pytz.timezone("America/Asuncion")
py_date = datetime.now(py_timezone)
print("PY: ", py_date.strftime("%d/%m/%Y, %H:%M:%S"))