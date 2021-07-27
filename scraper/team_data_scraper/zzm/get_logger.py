import logging


def get_logger(year: str, match: str):
    # 第一步，创建一个logger
    logger = logging.getLogger(year + '_' + match)
    logger.setLevel(logging.WARNING)  # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    log_path = '../../../logs/'
    log_name = log_path + "{}_{}".format(year, match) + ".log"
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.WARNING)  # 输出到file的log等级的开关
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)

    return logger
