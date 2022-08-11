# Prog-07: EAN-13 Barcode
# Knight N104

import math
import matplotlib.pyplot as plt
#-------------------------------------------------
def show_barcode(digits, ean13_code):  
    x = [[int(e) for e in ean13_code]]     
    plt.axis('off')         
    plt.imshow(x, aspect='auto', cmap='binary')    
    plt.title(digits)  
    plt.show()   
#-------------------------------------------------
def test1():
    digits = input('Enter a 13-digit number: ')    
    codes = encode_EAN13(digits)
    if codes == '':     
        print(digits, 'is not an EAN-13 number.')
    else:
        decoded_digits = decode_EAN13(codes)
        if decoded_digits == digits:
            show_barcode(digits, codes)
        else:
            print(digits)
            print(decoded_digits)
            print('Error in decoding.')
#-------------------------------------------------
L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', \
           '0110001', '0101111', '0111011', '0110111', '0001011']
G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', \
           '0111001', '0000101', '0010001', '0001001', '0010111']
R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', \
           '1001110', '1010000', '1000100', '1001000', '1110100']

#=================================================
G1=['LLLLLL','LLGLGG','LLGGLG','LLGGGL','LGLLGG','LGGLLG','LGGGLL','LGLGLG','LGLGGL','LGGLGL']
def codes_of(digits, patterns):
    a=''
    for i in range(len(digits)):
        a+=eval(f'{patterns[i]}_codes')[int(digits[i])]
    return a

def digits_of(codes):
    m=L_codes+G_codes+R_codes
    a=''
    b=0
    for i in range(len(codes)//7):
        if codes[7*i:7*i+7] in m:
            a+=str(m.index(codes[7*i:7*i+7])%10)
            b+=1
    return a*int(b==len(codes)//7 and codes.isdigit() and len(codes)%7==0)


def patterns_of(codes):
    m=L_codes+G_codes+R_codes
    d=['L','G','R']
    a=''
    b=0
    for i in range((len(codes))//7):
        if codes[7*i:7*i+7] in m:
            a+=d[(m.index(codes[7*i:7*i+7])//10)]
            b+=1
    return a*int(b==len(codes)//7 and len(codes)%7==0)


def check_digit(digits):
    a=0
    for i in range(len(digits)):
        a+=int(digits[i])*(1+2*int(i%2!=0))
    return str((10-(a%10))%10)


def encode_EAN13(digits):
    if (not digits.isdigit()) or (len(digits),check_digit(digits[:-1]))!=(13,digits[-1]):
        return ''
    a=codes_of(digits[1:7],G1[int(digits[0])])
    b=codes_of(digits[7:],'RRRRRR')
    c='101'+a+'01010'+b+'101'
    return c

def decode_EAN13(codes):
        if (codes[:3],codes[45:50],codes[92:],len(codes))==('101','01010','101',95) and codes.isdigit() and patterns_of(codes[3:45]) in G1 :
            if patterns_of(codes[3:45])=='GGGGGG':
                c=codes[::-1]
                return decode_EAN13(c)
            b=str(G1.index(patterns_of(codes[3:45])))+digits_of(codes[3:45]+codes[50:92])
            if b[-1]==check_digit(b[:-1]):
                return b
            else:
                return ''
        else:
            return ''
#-------------------------------------------------
test1()
