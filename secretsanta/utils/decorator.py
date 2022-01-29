from threading import Lock


# from https://theorangeduck.com/page/synchronized-python
def synchronized(func):
    func.__lock__ = Lock()

    def synced_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return synced_func


# from https://theorangeduck.com/page/synchronized-python
def synchronized_method(method):
    """A decorator similar to 'synchronized' keyword in Java for a method"""
    outer_lock = Lock()
    lock_name = "__" + method.__name__ + "_lock" + "__"

    def sync_method(self, *args, **kwargs):
        with outer_lock:
            if not hasattr(self, lock_name):
                setattr(self, lock_name, Lock())
            lock = getattr(self, lock_name)
            with lock:
                return method(self, *args, **kwargs)

    return sync_method
