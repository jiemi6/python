import logging,sys

filelog = True
path = r'log.txt'

logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)

# 调用模块时,如果错误引用，比如多次调用，每次会添加Handler，造成重复日志，这边每次都移除掉所有的handler，后面在重新添加，可以解决这类问题
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)

# file log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
if filelog:
    fh = logging.FileHandler(path,encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

# console log
formatter = logging.Formatter('%(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

if __name__ == '__main__':
    logger.info("这是一个测试")