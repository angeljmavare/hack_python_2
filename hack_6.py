"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

def fn_hack_6(s):
    result = s
    salida= []
    
    for i in range(len(result)):
        if i % 2 == 0:
            salida.append(str(i+1))
        else:
            salida.append("-")
        
    if not result:
        salida.append("0")
    
    return salida