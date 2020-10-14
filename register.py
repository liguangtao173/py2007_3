def zhuang():
    def inner():
        pass
    return inner

@zhuang
def register():
    pass

register()
