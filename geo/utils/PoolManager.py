import logging
import multiprocessing


class PoolManager:
    _instance = None

    def __init__(self):
        if PoolManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.pool = multiprocessing.Pool(processes=4)
            PoolManager._instance = self

    @staticmethod
    def get_instance():
        if PoolManager._instance is None:
            PoolManager()
        return PoolManager._instance

    def cleanup(self):
        if self.pool:
            self.pool.close()
            self.pool.join()
            logging.info("Pool closed and joined successfully.")

    def __del__(self):
        self.cleanup()