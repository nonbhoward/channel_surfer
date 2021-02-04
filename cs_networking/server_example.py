from vidgear.gears import NetGear
from vidgear.gears import VideoGear

stream = VideoGear(source="video_file.mp4").start()
server = NetGear()
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
