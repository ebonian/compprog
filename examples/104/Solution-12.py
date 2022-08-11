# Prog-12: COVID-19: The Latest Wave
# Knight N104
import numpy as np
def read_data(filename):
    d = np.loadtxt(filename, delimiter=",", encoding='utf-8', dtype=str)
    new_cases = np.array(d[1:,1:], dtype=int)
    norm = new_cases / np.max(new_cases, axis=1).reshape((new_cases.shape[0],1))
    return {'new_cases': new_cases,
        'norm_data': norm,
        'province_names': d[1:,0],
        'dates': d[0,1:]}

def max_new_cases_date(data):
    tt=np.sum(data['new_cases'],axis=0)
    return (data['dates'][np.argmax(tt)],np.max(tt))
def max_new_cases_province(data, beg_date, end_date):
    case2=np.sum(data['new_cases'][:,np.where(data['dates']==beg_date)[0][0]:np.where(data['dates']==end_date)[0][0]+1],axis=1)
    return (data['province_names'][np.argmax(case2)],np.max(case2))
def max_new_cases_province_by_dates(data):
    return np.stack((data['dates'],data['province_names'][np.argmax(data['new_cases'],axis=0)],np.max(data['new_cases'],axis=0)),axis=-1,out=np.ndarray((len(data['dates']),3),dtype=object))
def most_similar(data, province):
    n=np.where(data['province_names']==province)[0][0]
    i1=np.argmin(np.sum((data['norm_data'][n]-np.append(data['norm_data'][:n],data['norm_data'][n+1:]).reshape((-1,len(data['norm_data'][0]))))**2,axis=1))
    return data['province_names'][i1+(i1>=n)]
def most_similar_province_pair(data):
    r,c=data['norm_data'].shape
    mn=data['province_names'][np.argmin(np.sum((np.array([data['norm_data']])-np.reshape(data['norm_data'],(r,1,c)))**2,axis=2)+c*np.eye(r))//r]
    return (mn,most_similar(data, mn))
def most_similar_in_period(data, province, beg_date, end_date):
    n=np.where(data['dates']==end_date)[0][0]-np.where(data['dates']==beg_date)[0][0]+1
    x=np.arange(data['norm_data'].shape[1]-n+1).reshape((-1,1))
    p=data['norm_data'][np.where(data['province_names']==province)][0][np.where(data['dates']==beg_date)[0][0]:np.where(data['dates']==end_date)[0][0]+1].reshape((1,1,-1))
    s=np.sum((p-data['norm_data'][:,np.arange(n).reshape((1,-1))+x])**2,axis=2)
    s[[np.where(data['province_names']==province)][0],:]+=n
    n2=np.argmin(s)%len(x)
    return (data['province_names'][np.argmin(s)//len(x)],data['dates'][n2],data['dates'][n2+n-1])
def main():
    data = read_data('TH_20210401_20210416.csv')
    #a=max_new_cases_date(data)
    #b=max_new_cases_province(data, '2021-04-10', '2021-04-13')
    #c=max_new_cases_province_by_dates(data)
    #d=most_similar(data, 'ขอนแก่น')
    #e=most_similar_province_pair(data)
    #f=most_similar_in_period(data, 'กรุงเทพมหานคร', '2021-04-05', '2021-04-09' )
    #g=most_similar_in_period(data, 'กรุงเทพมหานคร', '2021-04-01', '2021-04-16' )
    return None
main()
