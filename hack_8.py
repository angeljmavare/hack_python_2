"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""

def fn_hack_8(s):
    result = s 
    salida = []
    
    if len(result) % 2 != 0:
        for i in range(len(result)-1, -1, -1): 
            salida.append(f"{result[i]}-{str(i+1)}")
    else:
        for i in range(len(result)-1,-1,-1): 
            salida.append(f"{str(i+1)}")
        
    return salida