class Computer:
    def set_spec(self,cpu,ram,vga,ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))

desktop = Computer()
desktop.set_spec('i7','16gb','gtx1060','512gb')
desktop.hardware_info()

notebook = Computer()
notebook.set_spec('i5','8gb','mx300','256gb')
notebook.hardware_info()
