import os
import sys
import json
import logging
import inspect
import numpy


def _serialize_ndarray(x):
    """Serializes ndarray.

    :param x: :class: `numpy.ndarray`
    :returns: json serialized string
    :rtype: str

    """
    if isinstance(x, numpy.ndarray):
        return json.dumps(x.tolist())
    # elif isinstance(x, torch.Tensor):
    #     return json.dumps(x.cpu().numpy().tolist())
    else:
        f"<<{type(x).__qualname__}>>"


def dumps_safe(x):
    return json.dumps(x, default=_serialize_ndarray)
    # return json.dumps(x, default=lambda o: f"{{Object, {type(o).__qualname__}}}")


def gen_file_logger(logdir, log_file_name):
    logger = logging.getLogger('default_logger')
    formatter = logging.Formatter(datefmt='%Y/%m/%d %I:%M:%S %p', fmt='%(asctime)s %(message)s')
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    if not log_file_name.endswith('.log'):
        log_file_name += '.log'
    log_file = os.path.abspath(os.path.join(logdir, log_file_name))
    if os.path.exists(log_file):
        backup_num = get_backup_num(logdir, log_file_name)
        os.rename(log_file, log_file + '.' + str(backup_num))
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger


def get_backup_num(filedir, filename):
    backup_files = [x for x in os.listdir(filedir) if x.startswith(filename)]
    backup_maybe_nums = [b.split('.')[-1] for b in backup_files]
    backup_nums = [int(x) for x in backup_maybe_nums
                   if any([_ in x for _ in list(map(str, range(10)))])]
    if backup_nums:
        cur_backup_num = max(backup_nums) + 1
    else:
        cur_backup_num = 0
    return cur_backup_num


def gen_file_and_stream_logger(logdir, log_file_name):
    logger = logging.getLogger('default_logger')
    formatter = logging.Formatter(datefmt='%Y/%m/%d %I:%M:%S %p', fmt='%(asctime)s %(message)s')
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    if not log_file_name.endswith('.log'):
        log_file_name += '.log'
    log_file = os.path.abspath(os.path.join(logdir, log_file_name))
    if os.path.exists(log_file):
        backup_num = get_backup_num(logdir, log_file_name)
        os.rename(log_file, log_file + '.' + str(backup_num))
    file_handler = logging.FileHandler(log_file)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)
    return logger


# Utility functions to ease logging
def _logi(logger, x):
    "Log to INFO and return string with name of calling function"
    f = inspect.currentframe()
    prev_func = inspect.getframeinfo(f.f_back).function
    x = f"[{prev_func}()] " + x
    logger.info(x)
    return x


def _logd(logger, x):
    "Log to DEBUG and return string with name of calling function"
    f = inspect.currentframe()
    prev_func = inspect.getframeinfo(f.f_back).function
    x = f"[{prev_func}()] " + x
    logger.debug(x)
    return x


def _logw(logger, x):
    "Log to WARN and return string with name of calling function"
    f = inspect.currentframe()
    prev_func = inspect.getframeinfo(f.f_back).function
    x = f"[{prev_func}()] " + x
    logger.warn(x)
    return x


def _loge(logger, x):
    "Log to ERROR and return string with name of calling function"
    f = inspect.currentframe()
    prev_func = inspect.getframeinfo(f.f_back).function
    x = f"[{prev_func}()] " + x
    logger.error(x)
    return x
