'''
Created on Feb 18, 2013

@author: ben
'''

class arrays:
    a = list('aA@4')
    b = list('bB8')
    c = list('cC(')
    d = list('dD')
    e = list('eE3')
    f = list('fF')
    g = list('gG9')
    h = list('hH')
    i = list('iI!1')
    j = list('jJ')
    k = list('kKx')
    l = list('lL!1')
    m = list('mM')
    n = list('nN')
    o = list('oO0')
    p = list('pP')
    q = list('qQ')
    r = list('rR')
    s = list('sS$')
    t = list('tT!+7')
    u = list('uU')
    v = list('vV')
    w = list('wW')
    x = list('xX')
    y = list('yY')
    z = list('zZ')
    
    
## this makes first_array an object containing all the values of arrays()
first_array = arrays()

## this prints 'a', 'A', '@', '4'
print(first_array.a)
## this prints 'z', 'Z'
print(first_array.z)

## replace the value of a in object first_array with overwritten
setattr(first_array, 'a', "overwritten")
## print overwritten
print(first_array.a)

## this is the equivelant of setattr(first_array, 'a', "value")
first_array.a = "overwritten again"
print(first_array.a)

## the actual class arrays() never gets touched, because you made a secondary object that you can manipulate
print(getattr(arrays(), 'a'))
