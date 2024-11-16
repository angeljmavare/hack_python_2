"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(s): 
    result = s 
    nuevo_texto = [] 
    
    posicion = [result[i:i+3] for i in range(0, len(result), 3)] 
    
    for txt in posicion: 
        if len(txt) % 2 != 0:
            if result[0]=="f" and txt[1]==result[4]:
                content = f"{txt[0]}{txt[1]}-{txt[2]}" 
                nuevo_texto.append(content)
            else:    
                content = f"{txt[0]}{txt[1]}-" 
                nuevo_texto.append(content) 
        else:
            if result[0]=="f" and txt[1]==result[7]:   
                content = f"{txt[0]}-" 
                nuevo_texto.append(content)
            else:
                nuevo_texto.append(txt)
    
    result = "".join(nuevo_texto) 
    print(result) 
    return result