alp='abcdefghijklmnopqrstuvwxyz'
alp+=alp.upper()
def chk_col(col):
    if len(col)==0: return True
    for e in col:
        if e in alp:
            return True
        elif e<'0' or e>'9':
            return True
    return int(col)>52 or int(col)<1

def chk_row(row):
    if len(row)>1: return True
    return row not in alp

text=input().strip()
if len(text)>3:
    temp=[e.strip() for e in text.split(',')]
    for e in temp:
        if 'row' in e:
            i=e.find('=')
            row=e[i+1:].strip()
        elif 'col' in e:
            i=e.find('=')
            col=e[i+1:].strip()
else:
    row=text[0]
    col=text[1:].strip()
col_error=chk_col(col)
row_error=chk_row(row)     
if row_error and col_error:
    print("Invalid row and column")
elif row_error:
    print("Invalid row")
elif col_error:
    print("Invalid column")
else:
    idx=alp.find(row)
    if idx%2==int(col)%2:
        print('Black')
    else:
        print('White')