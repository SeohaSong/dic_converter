
from bs4 import BeautifulSoup


def convert(arrdic):

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