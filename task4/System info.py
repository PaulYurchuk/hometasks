import os
import datetime
import psutil
import json
import configparser


def get_host_cpu_stats():
    return str({
        'kernel(system)': int(psutil.cpu_times()[2]),
        'idle': int(psutil.cpu_times()[3]),
        'user': int(psutil.cpu_times()[0]),
        'iowait': int(psutil.cpu_times()[4]),
    })

print("CPU times:\n", get_host_cpu_stats(), "\n")

def get_host_cpu_times():
        return str({
        'cpu1': int(psutil.cpu_percent())
        })

print("CPU usage in % trace: ", get_host_cpu_times(), "\n")

def get_host_virt_memory():
    return str({
        'total': int(psutil.virtual_memory()[0]),
        'free': int(psutil.virtual_memory()[4]),
        'used': int(psutil.virtual_memory()[3]),
        'persent': int(psutil.virtual_memory()[2])
    })

print("Virtual memory usage: \n", str(get_host_virt_memory()), "\n")

def get_host_disk_partitions():
    disk = print("Partitions: \n", str(psutil.disk_partitions()), "\n")
    return disk

print("Disk usage: \n", psutil.disk_usage('/'), "\n")
print("Network information: \n", psutil.net_io_counters(pernic=True), "\n")

def ConfigSectionMap(section):
        dict1 = {}
        options = Config.options(section)
       for option in options:
           try:
                dict1[option] = Config.get(section, option)
               if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
        except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1
    config_name = ConfigSectionMap("common")['output']
    config_interval = ConfigSectionMap("common")['interval']

f = open('test.txt', 'w')
f.write("SNAPSHOT" "\n" "CPU times:\n".format(psutil.cpu_percent(interval=0.1) + "\n""\n"))
f.write("Virtual memory usage: \n" + get_host_virt_memory() + "\n""\n")
f.write("Partitions: \n" + str(get_host_disk_partitions() + "\n""\n")
f.write(str(get_host_cpu_times() + "\n""\n"))
f.close()