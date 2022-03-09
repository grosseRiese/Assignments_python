import numpy as np
import string

##### test-case    #####
ciphertext ="FLAPJBCZFAEMAUHJNREPGPDVUNLINGNWSRMCABAHTNOREPFESGFSEMBSAHGOHJNREPGPDVUNCRAJLAEMHJNGSRPAAMNEXUULHDLEDZ"
key = 'NOPRESSURENODIAMONDS'
ciphertext = ciphertext.lower()


#The plain text should be:
    ##"if debugging is the process of removing bugs 
    ## then programming must be the process of putting them in. edsger w dijkstra" 
### => < Edsger Wybe Dijkstra >


#####   basic-case   #####
#key = 'playfair example'
plaintext = 'hide the gold inthetreestump'
#ciphertext = "bmodzbxdnabekudmuixmmouvif"

plaintext=plaintext.lower()
plaintext = plaintext.replace(" ", "")

plaintextpairs = []
ciphertextpairs = []

#############################################################

def filter_key(key):
    key =  key.lower()
    key = key.replace(" ", "")
    return key

new_key = filter_key(key)
#print("New key: ", new_key)

############################################################

def playfair(text):
    en_alphabets = string.ascii_lowercase.replace("q",".")
    empt_matrix = ["" for i in range(5)]
    index = 0
    column = 0
    for chara_ in text:
        if chara_ in en_alphabets:
            empt_matrix[index] += chara_
            en_alphabets = en_alphabets.replace(chara_,'.')            
            column += 1
            if column > 4:
                index += 1
                column = 0
                
    for _char in en_alphabets:
        if(_char != '.'):
            empt_matrix[index] += _char
            column += 1
            if column > 4:
                index += 1
                column = 0
    
    return empt_matrix

key_matrix = playfair(new_key)  
print("---------------------------------------------------")


############################################################
################     Decryption      #######################

def cipher_text_method(key_matrix):
    _index = 0
    while _index < len(ciphertext):
        a = ciphertext[_index]
        b = ciphertext[_index+1] 
        
        ciphertextpairs.append(a + b)
        _index += 2
    
    for pair in ciphertextpairs:
        applied_rule = False

        for row in key_matrix:
            if pair[0]in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])
                
                plaintextpair = row[(j0+4)%5] + row[(j1+4)%5]
                plaintextpairs.append(plaintextpair)
                applied_rule = True
                
        if applied_rule:
            continue

        for j in range(5):
            col = "".join([key_matrix[i][j] for i in range(5)])
            if pair[0]in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])
                
                plaintextpair = col[(i0+4)%5] + col[(i1 +4)%5]
                plaintextpairs.append(plaintextpair)
                applied_rule = True
                
        
        if applied_rule:
            continue

        i0=0
        i1=0
        j0=0
        j1=0
    
        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])
                
            if pair[1] in row:
                i1 = i
                j1= row.find(pair[1])
            
        plaintextpair = key_matrix[i0][j1] + key_matrix[i1][j0]
        plaintextpairs.append(plaintextpair)
    print("---------------------------------------------------")
    print("The key : ", new_key)  
    print("---------------------------------------------------")
    print("Ciphertext : " ,"".join(ciphertextpairs))
    print("---------------------------------------------------")
    print("PlainText: ","".join(plaintextpairs))
    print("---------------------------------------------------")
    
#cipher_text_method(key_matrix)  # <===== 'if u want to run plain-text(), comment out this method'
 
print("---------------------------------------------------")
print("---------------------------------------------------")
############################################################
################     Encryption      #######################
def rules_method_plain_text(key_matrix):

    _index = 0
    while _index < len(plaintext):
        a = plaintext[_index]
        b = '' 
        if (_index + 1) == len(plaintext):
            b = 'x'
        else:
            b = plaintext[_index+1]
        
        if a != b :
            plaintextpairs.append(a + b)
            _index += 2
        else:
            plaintextpairs.append(a + 'X')
            _index += 1

    print("Plain-text pair: ", plaintextpairs) 
     
    for pair in plaintextpairs:
        applied_rule = False
        
        for row in key_matrix:
            if pair[0] in row and pair[1] in row:
                
                fst_index = row.find(pair[0])
                scnd_index = row.find(pair[1])
                
                ciphertextpair = row[(fst_index+1)%5] + row[(scnd_index+1)%5]
                ciphertextpairs.append(ciphertextpair)
                applied_rule = True
                
        if applied_rule:
            continue
        
        for j in range(5):
            col = "".join([key_matrix[i][j] for i in range(5)])
            if pair[0]in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])
                
                ciphertextpair = col[(i0+1)%5] + col[(i1 +1)%5]
                ciphertextpairs.append(ciphertextpair)
                applied_rule = True
            
        if applied_rule:
            continue
        
        i0=0
        i1=0
        j0=0
        j1=0
        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])
                
            if pair[1] in row:
                i1 = i
                j1= row.find(pair[1])
        ciphertextpair = key_matrix[i0][j1] + key_matrix[i1][j0]
        ciphertextpairs.append(ciphertextpair)
    print("The key : ", new_key)    
    print("plaintext : ","".join(plaintextpairs))
    print("Ciphertext : ","".join(ciphertextpairs))

#rules_method_plain_text(key_matrix) # <===== 'if u want to run cipher-text(), comment out this method

print("---------------------------------------------------")

def main():
        print("---------------------------------------------------")
        choice=int(input("\n 1.Encryption:  \n 2.Decryption:  \n 3.EXIT: \n"))
        if choice==1:
            rules_method_plain_text(key_matrix)
            print("---------------------------------------------------")
        elif choice==2:
            cipher_text_method(key_matrix)
            print("---------------------------------------------------")
        elif choice==3:
            raise SystemExit
            #exit()
            print("---------------------------------------------------")
        else:
            print("Choose correct choice")
        print("---------------------------------------------------")
        
if __name__ == '__main__':
    main()