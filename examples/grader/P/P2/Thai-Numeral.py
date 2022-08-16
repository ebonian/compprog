thai={0:'soon',1:'neung',2:'song',3:'sam',4:'si',5:'ha',6:'hok',7:'chet',8:'paet',9:'kao'}
def to_Thai(N):
    num=str(N)
    out=''
    if N >= 1000:
        out+=thai[N//1000]+' pun '
        N%=1000
    if N >= 100:
        out+=thai[N//100]+' roi '
        N%=100
    if N >= 10:
        if N//10==2:
            out+='yi sip '
        elif N//10 == 1:
            out+='sip '
        else:
            out+=thai[N//10]+' sip '
        N%=10
    if len(num) > 1:
        if N==1:
            out+='et'
        elif N==0:
            pass
        else:
            out+=thai[N]
    else:
        out+=thai[N]
    return out.strip() 
exec(input().strip())