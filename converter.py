
from bs4 import BeautifulSoup


def convert2xml(arrdic):

    def do_arrdic2xml(arrdic):
        return "".join([_do_dic2tag(dic) for dic in arrdic])
        
    def _do_dic2tag(dic):
        tag = list(dic.keys())[0]
        value = (do_arrdic2xml(dic[tag])
                 if type(dic[tag]) == list
                 else "<![CDATA[{}]]>".format(dic[tag]))
        return "<{0}>{1}</{2}>".format(tag, value, tag.split()[0])

    xml = do_arrdic2xml(arrdic)
    bs = BeautifulSoup(xml, "xml")
    return bs


def convert2obj(dic):

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