from functools import wraps
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename = "{}.log".format(orig_func.__name__,), level = logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            f"Ran with args: {args}, and kwargs: {kwargs} ")
        return orig_func(*args, **kwargs) # closure

    return wrapper

def my_timer(orig_func):
    import time
    
    @wraps(orig_func)
    def wrapper(*arg, **kwargs):
        t1 = time.time()
        result = orig_func(*arg, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in {t2} sec.")
        return result
    
    return wrapper

import time
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f"display_info ran with arguments ({name}, {age})")

display_info("john", 25)
display_info("tome", 21)