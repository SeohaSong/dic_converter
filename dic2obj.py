
def convert(dic):

    class Obj():
        def __init__(self, dic):
            for key in dic:
                value = dic[key]
                if type(value) == dict:
                    obj = Obj(value)
                    setattr(self, key, obj)
                else:
                    setattr(self, key, value)
                    
    return Obj(dic)