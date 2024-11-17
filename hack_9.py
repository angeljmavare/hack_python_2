"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

def fn_hack_9(s):
    s["Foo"]="Fooziman"
    print (s)
    
    resultado ={}
    
    for clave, valor in s.items():
        if clave == "Foo":
            resultado[clave]= valor
    return resultado