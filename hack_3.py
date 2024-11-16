"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(s):
    result = s
    result = result.capitalize()
    result = result[:-1] + result[-1].upper()
    result = result.replace("a","@").replace("e","3").replace("i","¡").replace("o","0").replace("u","v").replace("U","v")
    return result
  