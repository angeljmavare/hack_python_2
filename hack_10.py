"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    lista = []
    contador_clave= 1
    contador_llave= 2
    
    for dic in result:
        nuevo_diccionario= {}
        nuevo_diccionario[str(contador_clave)]= str(contador_llave)
        contador_clave+=2
        contador_llave+=2
        lista.append(nuevo_diccionario)  
    return lista
