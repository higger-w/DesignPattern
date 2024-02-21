class Logger(object):
    __instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            print('Creating new instance')
            cls.__instance = super(Logger, cls).__new__(cls)   # cls.__new__(cls)
        return cls.__instance
    
# log = Logger()  # 报错
log1 = Logger.instance()
print(log1)

log2 = Logger.instance()
print(log1 is log2)