from song import last_verse
from song import verse
from time import sleep


def main_loop():
    for i in range(9, 0, -1):
        singsong = verse if i > 1 else last_verse
        print(singsong.format(i, i, i-1))
        sleep(0.5)


main_loop()
