class USB:
    def __init__(self, capacity):
        self.capacity = capacity

    def info(self):
        print('{}GB USB'.format(self.capacity))

usb = USB(512)
usb.info()