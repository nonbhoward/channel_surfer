from vidgear.gears import NetGear
import cv2.cv2 as cv2

client = NetGear(receive_mode=True)
while True:
    frame = client.recv()
    if frame is None:
        break
    # do something with frame
    cv2.imshow("output frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
client.close()
