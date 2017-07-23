import psutil, json, datetime, time, configparser

config = configparser.ConfigParser()
config.read('config')
type = str(config['common']['output'])
min = int(config['common']['interval'])

if type == 'txt':
	while True:
		file = open("logging.txt", "a+")
		file.seek(0, 0)
		counter = len(file.readlines())

		col = ''
		col += 'SNAPSHOT {}: '.format(counter + 1) + str(datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S'))
		col += " - CPU usage (%): {} ".format(psutil.cpu_percent(interval=1))
		col += "| VirtMemAvailable(MB): {} ".format(psutil.virtual_memory().available // 1024 // 1024)
		col += "| VirtMemUsed (MB): {} ".format(psutil.virtual_memory().used // 1024 // 1024)
		col += "| VirtMemTotal (MB): {} ".format(psutil.virtual_memory().total // 1024 // 1024)
		col += "| Disk: Read (MB): {} ".format(psutil.disk_io_counters().read_bytes // 1024 // 1024)
		col += "| Disk: Write (MB): {} ".format(psutil.disk_io_counters().write_bytes // 1024 // 1024)
		col += "| Network: Sent(MB): {} ".format(psutil.net_io_counters(pernic=True)['enp0s25'].bytes_sent // 1024 // 1024)
		col += "| Network: Recieved(MB): {}\n".format(psutil.net_io_counters(pernic=True)['enp0s25'].bytes_recv // 1024 // 1024)
		file.write(col)
		file.close()

elif type == 'json':
	while True:
		file = open("logging.json", "a+")
		file.seek(0, 0)
		counter = len(file.readlines())
		if counter == 0:
			snap = 'SNAPSHOT {}'.format(counter + 1)
			dateVar = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
			cpuVar = psutil.cpu_percent(interval=1)
			memAvVar = psutil.virtual_memory().available // 1024 // 1024
			memUsVar = psutil.virtual_memory().used // 1024 // 1024
			memTotVar = psutil.virtual_memory().total // 1024 // 1024
			rDisk = psutil.disk_io_counters().read_bytes // 1024 // 1024
			wDisk = psutil.disk_io_counters().write_bytes // 1024 // 1024
			sNet = psutil.net_io_counters(pernic=True)['enp0s25'].bytes_sent // 1024 // 1024
			rNet = psutil.net_io_counters(pernic=True)['enp0s25'].bytes_recv // 1024 // 1024
			pythonDictionary = {
			snap: {'Timestamp': dateVar, 'CPU usage (%) ': cpuVar, 'VirtMemAvailable(MB) ': memAvVar,
					  'VirtMemUsed (MB): ': memUsVar, \
					  'VirtMemTotal (MB) ': memTotVar, 'Disk: Read (MB) ': rDisk, 'Disk: Write (MB) ': wDisk, \
					  'Network: Sent (MB) ': sNet, 'Network: Recieved (MB) ': rNet}}
			json.dump(pythonDictionary, file, indent=4)
		else:
			with open('logging.json') as f:
				data = json.load(f)

			snapVar = 'SNAPSHOT {}'.format(len(data) + 1)
			dateVar = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
			cpuVar = psutil.cpu_percent(interval=1)
			memAvVar = psutil.virtual_memory().available // 1024 // 1024
			memUsVar = psutil.virtual_memory().used // 1024 // 1024
			memTotVar = psutil.virtual_memory().total // 1024 // 1024
			rDisk = psutil.disk_io_counters().read_bytes // 1024 // 1024
			wDisk = psutil.disk_io_counters().write_bytes // 1024 // 1024
			sNet = psutil.net_io_counters(pernic=True)['enp0s25'].bytes_sent // 1024 // 1024
			rNet = psutil.net_io_counters(pernic=True)['enp0s25'].bytes_recv // 1024 // 1024
			pythonDictionary = {
			snapVar: {'Timestamp': dateVar, 'CPU usage (%) ': cpuVar, 'VirtMemAvailable(MB) ': memAvVar,\
			'VirtMemUsed (MB): ': memUsVar, 'VirtMemTotal (MB) ': memTotVar, 'Disk: Read (MB) ': rDisk, \
			'Disk: Write (MB) ': wDisk, 'Network: Sent (MB) ': sNet, 'Network: Recieved (MB) ': rNet}}
			data.update(pythonDictionary)

			with open('logging.json', 'w') as f:
				json.dump(data, f, indent=4)

file.close()
time.sleep(min*60)