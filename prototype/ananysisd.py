from time import sleep
from watchdog.watchdog.prototype import alert

__author__ = 'hecxac0d3@gmail.com'

class ananysisd():
    def compare_hash(self,value, hash_new, hash_old):
        if hash_new is not hash_old:
            alert.msg()
            update_value(value, hash_new)
        else:
            pass

    def time_delay_scan(self,time):
        self.time = time
        sleep(time)