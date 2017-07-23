import datetime, psutil

class SysCollector:
    def __init__(self):
        self.snap = 'SNAPSHOT {}'.format(counter + 1)
        self.date = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        self.cpu = psutil.cpu_percent(interval=1)
        self.vm_avail = psutil.virtual_memory().available // 1024 // 1024
        self.vm_used = psutil.virtual_memory().used // 1024 // 1024
        self.vm_total = psutil.virtual_memory().total // 1024 // 1024
        self.io_read = psutil.disk_io_counters().read_bytes // 1024 // 1024
        self.io_write = psutil.disk_io_counters().write_bytes // 1024 // 1024
        self.net_get = psutil.net_io_counters(pernic=True)['en1'].bytes_recv // 1024 // 1024
        self.net_sent = psutil.net_io_counters(pernic=True)['en1'].bytes_sent // 1024 // 1024

class parser:
    def __init__(self,filename):
        self.filename = filename
        self.config = configparser.ConfigParser()
        self.config.read(self.filename)

    def config(self):
        self.type = str(self.config['common']['output'])
        self.min = int(self.config['common']['interval'])
        return self.type, self.min

pars = parser('config')
param = pars.config()
if param[0] == 'json':
    while True:
            obj = CollectorJson.CollectorJson()
            obj.write()
            time.sleep(param[1] * 60)
elif param[0] == 'plain':
        while True:
            obj = writerPlain.WriterPlain()
            obj.write()
            time.sleep(param[1] * 60)

class CollectorJson(SysCollector.SysCollector):
    def write(self):
        self.file = open("logging.json", "a+")
        self.file.seek(0, 0)
        self.counter = len(self.file.readlines())
        if self.counter == 0:
            self.snap = 'SNAPSHOT {}'.format(1)
            self.pythonDictionary = {
            self.snap: {'Timestamp': self.date, 'CPU load %': self.cpu, 'VM available': self.vm_avail,
            'VM used': self.vm_used, 'VM total': self.vm_total, 'Disk IO read': self.io_read,
            'Disk IO write': self.io_write, 'Sent (mb)': self.net_sent, 'Get (mb)': self.net_get}}
            json.dump(self.pythonDictionary, self.fo, indent=4)

        else:
            with open('logging.json') as f:
                self.data = json.load(f)
                self.snap = 'SNAPSHOT {}'.format(len(self.data) + 1)
                self.pythonDictionary = {
                self.snap: {'Timestamp': self.date, 'CPU load %': self.cpu, 'VM available': self.vm_avail,
                'VM used': self.vm_used, 'VM total': self.vm_total, 'Disk IO read': self.io_read,
                'Disk IO write': self.io_write, 'Sent (mb)': self.net_sent, 'Get (mb)': self.net_get}}
                self.data.update(self.pythonDictionary)

            with open('stat.json', 'w') as f:
                json.dump(self.data, f, indent=4)

        self.file.close()


 class CollectorTXT(SysCollector.Syscollector):
    def write(self):
        file = open("stat.file", "a+")
        file.seek(0, 0)
        counter = len(file.readlines())
        col = ''
        col += 'SNAPSHOT {}: '.format (counter + 1) + str (datetime.datetime.now ().strftime ('%m/%d/%Y %H:%M:%S'))
        col += " - CPU usage (%): {} ".format (psutil.cpu_percent (interval=1))
        col += "| VirtMemAvailable(MB): {} ".format (psutil.virtual_memory ().available // 1024 // 1024)
        col += "| VirtMemUsed (MB): {} ".format (psutil.virtual_memory ().used // 1024 // 1024)
        col += "| VirtMemTotal (MB): {} ".format (psutil.virtual_memory ().total // 1024 // 1024)
        col += "| Disk: Read (MB): {} ".format (psutil.disk_io_counters ().read_bytes // 1024 // 1024)
        col += "| Disk: Write (MB): {} ".format (psutil.disk_io_counters ().write_bytes // 1024 // 1024)
        col += "| Network: Sent(MB): {} ".format (psutil.net_io_counters (pernic=True)['en1'].bytes_sent // 1024 // 1024)
        col += "| Network: Recieved(MB): {}\n".format (psutil.net_io_counters (pernic=True)['en1'].bytes_recv // 1024 // 1024)
        file.write (col)
        file.close ()