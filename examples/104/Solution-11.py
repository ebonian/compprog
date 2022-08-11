# Prog-11: Weather report (EP.2)
# Knight N104
import json
import math
def top_K_max_temp_by_region(data, K):
    D={}
    for x in data:
        for t in data[x]['list']:
            if data[x]['city']['region'] not in D:
                D[data[x]['city']['region']]=[]
            D[data[x]['city']['region']].append((-t['main']['temp'],data[x]['city']['name'],t['dt_txt']))
    return {k:[(-x,y,z) for (x,y,z) in sorted(D[k])[:K]] for k in D}
def average_temp_by_date(data, region):
    D={}
    for x in data:
        if data[x]['city']['region']==region or region=='ALL':
            for t in data[x]['list']:
                if t['dt_txt'][:10] not in D:
                    D[t['dt_txt'][:10]]=[]
                D[t['dt_txt'][:10]].append(t['main']['temp'])
    return sorted([(y,sum(D[y])/len(D[y])) for y in D])    
def max_rain_in_3h_periods(data, region, date):
    L={}
    for x in data:
        for t in data[x]['list']:
            if date==t['dt_txt'][:10] and (data[x]['city']['region']==region or region=='ALL') and 'rain' in t:
                if int(t['dt_txt'][11:13]) not in L:
                    L[int(t['dt_txt'][11:13])]=[]
                L[int(t['dt_txt'][11:13])].append(t['rain']['3h'])
    return sorted([(a,max(L[a])) for a in L])        
def AM_PM_weather_description_by_region(data, date):
    D={}
    for x in data:
        for t in data[x]['list']:
                m='AM'*int('00'<=t['dt_txt'][11:][:2]<'12')+'PM'*int('12'<=t['dt_txt'][11:][:2]<'24')
                if t['dt_txt'][:10]==date:
                    if data[x]['city']['region'] not in D:
                        D[data[x]['city']['region']]={}
                    if m not in D[data[x]['city']['region']]:
                        D[data[x]['city']['region']][m]=[]
                    D[data[x]['city']['region']][m]+=[t['weather'][i]['description'] for i in range(len(t['weather']))]
    return {x:{y:max(D[x][y],key=D[x][y].count) for y in D[x]} for x in D}
def most_varied_weather_provinces(data):
    c,S=0,set()
    for x in data:
            L=len({t['weather'][i]['description'] for t in data[x]['list'] for i in range(len(t['weather']))})
            if L>c:c,S=L,{data[x]['city']['name']}
            elif L==c:S.add(data[x]['city']['name'])
    return S   
def main():
    #from unittest import *
    pass
main()

