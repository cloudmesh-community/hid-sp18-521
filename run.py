# Scott Steinbruegge
# I524 - Spring 2018
# Create Eve REST Service Assignment

from eve import Eve
import platform
import subprocess
import psutil
from psutil import virtual_memory
from hurry.filesize import size
from hurry.filesize import alternative
import json
import getpass

app = Eve()


@app.route('/sys_info')


def sys_info():
    processor = (subprocess.check_output("cat /proc/cpuinfo | grep 'model name' | uniq", shell=True).strip()).decode()
    processor = processor.lstrip('model name\t: ')
    mem = virtual_memory()

    systeminfo_dict = {"os_type": platform.system(),
                       "os_version": platform.version(),
                       "host_name": platform.uname().node,
                       "user_name": getpass.getuser(),
                       "architecture": platform.architecture()[0],
                       "processor": processor,
                       "memory": size(mem.total, system=alternative),
                       "total_disk_size": size(psutil.disk_usage('/').total, system=alternative),
                       "total_disk_free": size(psutil.disk_usage('/').free, system=alternative),
                       "total_disk_used": size(psutil.disk_usage('/').used, system=alternative),
                       "percent_disk_used": psutil.disk_usage('/').percent}

    # TODO: Import data into MongoDB for API to pull directly from the database

    json_systeminfo = json.dumps(systeminfo_dict, indent=4)

    return json_systeminfo


@app.route('/cpu')


def cpu():
    cpu_model = (subprocess.check_output("cat /proc/cpuinfo | grep 'model name' | uniq", shell=True).strip()).decode()
    cpu_model = cpu_model.lstrip('model name\t: ')

    cpu_dict = {"cpu_name": cpu_model,
                "cpu_cores": psutil.cpu_count(),
                "cpu_perc_used": psutil.cpu_percent()}

    json_cpu = json.dumps(cpu_dict, indent=4)

    return json_cpu


@app.route('/memory')


def memory():
    mem = virtual_memory()

    memory_dict = {"total_memory": size(mem.total, system=alternative),
                   "available_memory": size(mem.available, system=alternative),
                   "used_memory": size(mem.used, system=alternative),
                   "free_memory": size(mem.free, system=alternative),
                   }

    json_memory = json.dumps(memory_dict, indent=4)

    return json_memory


@app.route('/disk')


def disk():
    disk_dict = {"total_disk_size": size(psutil.disk_usage('/').total, system=alternative),
                 "total_disk_free": size(psutil.disk_usage('/').free, system=alternative),
                 "total_disk_used": size(psutil.disk_usage('/').used, system=alternative),
                 "percent_disk_used": psutil.disk_usage('/').percent}

    json_disk = json.dumps(disk_dict, indent=4)

    return json_disk


if __name__ == '__main__':
    app.run()
