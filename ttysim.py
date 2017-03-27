import os
import pty
import time
import select

m1, s1 = pty.openpty()
m_name1, s_name1 = os.ttyname(m1), os.ttyname(s1)

m2, s2 = pty.openpty()
m_name2, s_name2 = os.ttyname(m2), os.ttyname(s2)

print('{} -> {}'.format(s_name1, s_name2))

while 1:
    ready, _, _ = select.select([m1, m2], [], [])
    for device in ready:
        if device == m1:
            data = os.read(m1, 1024)
            os.write(m2, data)
        else:
            data = os.read(m2, 1024)
            os.write(m1, data)
    time.sleep(0.1)
