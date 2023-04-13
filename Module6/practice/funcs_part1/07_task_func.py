def format_time(s):
    hh = s // (60 * 60) % 24
    mm = (s - hh * 60 * 60) // 60 % 60
    ss = (s - hh * 60 * 60 - mm * 60) % (24 * 60 * 60)
    return f"{hh:02}:{mm:02}:{ss:02}"


print(format_time(13))
print(format_time(130))
print(format_time(3601))
print(format_time(40271))
print(format_time(45296))
print(format_time(86399))
print(format_time(86400))
print(format_time(86401))
