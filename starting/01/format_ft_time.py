import time
from datetime import date

unix_time = time.time()
local_time = date.today().strftime("%B %d %Y")

print(f'Seconds since January 1, 1970: {unix_time:,.4f} or {unix_time:.2e} in scientific notation')
print(local_time)