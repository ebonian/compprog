def to_sec(time):
    minute,sec=time.split(':')
    return int(minute)*60+int(sec)

def to_time(sec):
    minute=sec//60
    sec-=minute*60
    sec='00'+str(sec)
    return str(minute)+':'+sec[-2:]

n=int(input())
type_music={}
for i in range (n):
    music_name,singer,type_song,time=input().split(', ')
    if type_song not in type_music:
        type_music[type_song]= to_sec(time)
    else:
        type_music[type_song]+=to_sec(time)
top3=sorted(type_music.items(),key= lambda x:x[1],reverse=True)[:3]
for e in top3:
    print(e[0],'-->',to_time(e[1]))