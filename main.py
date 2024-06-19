from waFuCo2 import WaFuCo
import time

if __name__ == '__main__':
    waFuCo = WaFuCo(48, 64, 6 ,6)

    waFuCo.printTileMap()

    while True:
        waFuCo.handle_events()
        waFuCo.processVisuals()

