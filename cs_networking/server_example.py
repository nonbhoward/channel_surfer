from MACHINE_DETAILS import CLIENT_IP
from MACHINE_DETAILS import CLIENT_PORT
from MACHINE_DETAILS import PATTERN
from MACHINE_DETAILS import PROTOCOL
from vidgear.gears import NetGear
from vidgear.gears import VideoGear

stream = VideoGear(source="HDMI_Video.mpg").start()
server = NetGear(
    address=CLIENT_IP,
    port=CLIENT_PORT,
    protocol=PROTOCOL,
    pattern=PATTERN
)
while True:
    try:
        frame = stream.read()
        if frame is None:
            break
        server.send(frame)
    except KeyboardInterrupt:
        break
stream.stop()
server.close()
