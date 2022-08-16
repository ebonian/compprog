filename=input()
command=open(filename,'r')
first=command.readline().strip()
form=command.readline().strip()
for line in command:
    out=''
    if first=='T2M':
        for e in line.strip():
            begin=form.find('['+e+']')
            if begin==-1:
                out='Invalid : '+line.strip()
                break
            begin+=len('['+e+']')
            end=form.find('[',begin)
            out+=form[begin:end]+' '
    elif first=='M2T':
        for e in line.strip().split():
            begin=form.find(']'+e+'[')
            if begin==-1:
                out='Invalid : '+line.strip()
                break
            begin-=1
            out+=form[begin]
    else:
        print("Invalid code")
        break
    print(out.strip())
command.close()