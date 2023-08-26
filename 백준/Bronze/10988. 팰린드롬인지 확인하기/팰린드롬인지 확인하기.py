word = input()
word_li = list(word)
dn = 0 
detec = 0

if (len(word_li)%2 == 0):
    dn = len(word_li) // 2 
else:
    dn = (len(word_li) - 1) // 2

for i in range(0, dn, 1):
    if ( word_li[i] == word_li[len(word_li)-1-i] ):
        detec += 0 
    else :
        detec += 1
        
if (detec == 0):
    print ('1')
else:
    print('0')