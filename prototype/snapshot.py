from _hashlib import openssl_md5

__author__ = 'hecxac0d3@gmail.com'

class snapshot:
    def __init__(self):
        # Do anything
        pass

    def read_config(self, path_config):
        self.monitor = {
            "path_snapshot_dir":[],
            "snapshot_file_exe":[],
            "ignore_snapshot_dir":[],
            "ignore_snapshot_file_exe":[]
        }
        return self.monitor

    def snapshot(self, snapshot_path):
        hash_new = openssl_md5(snapshot_path)
        hash_new = hash_new.hexdigest()
        hash_old = find_hash(snapshot_path)
        if (hash_new is hash_old):
            pass
        else:
            update(key, hash_new)

    def find_hash(self,path):
        hash_old = None
        return hash_old

    def update(self,key,hash_new):
        self.key = key
        self.hash_new = hash_new