from MACHINE_DETAILS import CLIENT_IP
from MACHINE_DETAILS import CLIENT_PORT
from MACHINE_DETAILS import PATTERN
from MACHINE_DETAILS import PROTOCOL
from vidgear.gears import NetGear
import cv2.cv2 as cv2

client = NetGear(
    address=CLIENT_IP,
    port=CLIENT_PORT,
    protocol=PROTOCOL,
    pattern=PATTERN,
    receive_mode=True
)
while True:
    # receive network frames
    frame = client.recv()
    if frame is None:
        break

    # do something with frame

    # show output window
    cv2.imshow("output frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
client.close()
