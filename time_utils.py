async def get_seconds(time_string: str) -> int:
    """Convert strings like '30 s', '10 min', '1 hour', '2 day', '1 month', '1 year' to seconds."""
    time_string = str(time_string).strip()
    value = ""
    index = 0
    while index < len(time_string) and time_string[index].isdigit():
        value += time_string[index]
        index += 1
    unit = time_string[index:].strip().lower()
    value = int(value) if value else 0

    if unit in ("s", "sec", "secs", "second", "seconds"):
        return value
    elif unit in ("min", "mins", "minute", "minutes"):
        return value * 60
    elif unit in ("hour", "hours", "h"):
        return value * 3600
    elif unit in ("day", "days", "d"):
        return value * 86400
    elif unit in ("month", "months"):
        return value * 86400 * 30
    elif unit in ("year", "years"):
        return value * 86400 * 365
    return 0
