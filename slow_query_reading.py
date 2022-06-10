import mmap

with open("/var/log/postgresql/postgresql-14-main.log") as f:
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if s.find(b'duration'):
        i = s.find(b'duration')
        f.seek(i)
        print(f.read())
    # print(s)
