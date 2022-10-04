from datetime import datetime, timezone

utc_now = datetime.now(timezone.utc)
local_now = datetime.now()

print("¿Vamos adelantados a UTC?", local_now > utc_now)
