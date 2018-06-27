#The solution of python challenge

#1st 
'''
print (2**38)
'''

#2end
'''
original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
rq = list(original)
l = ''
for t in rq:
    if ord(t) in range(97,121):
        t = chr(ord(t) + 2)
        l += t
    elif ord(t) in range(121,123):
        t = chr(96+(ord(t)+2-122))
        l += t
    else:
        l+= t
print (l)
'''

#3rd
'''
'''