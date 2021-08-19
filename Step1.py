def stepen(a):
    if a.find('^')!=-1:
        b=float(a[:a.find('^')])
        a=a[a.find('^')+1:]
        while a.find('^')!=-1:
            b=b**float(a[:a.find('^')])
            a = a[a.find('^') + 1:]
        a=str(b**float(a))
        return a
    else:
        return a
def proizvedenie(ch):
    m=1.0
    if ch.find("*")!=-1 or ch.find("/")!=-1:
        ch="*"+ch
        j=1
        while j<len(ch):
            if ch[j]=='*' or ch[j]=='/':
                mn=ch[1:j]
                if ch[0]=='*':
                    m*=float(stepen(mn))
                else:
                    m/=float(stepen(mn))
                ch=ch[j:]
                j=1
            else: j+=1
        if ch[0]=='*':
            ch=ch[1:]
            m *= float(stepen(ch))
        else:
            ch = ch[1:]
            m /= float(stepen(ch))
        return str(m)
    else: return stepen(ch)
def chislo(st):
    sum = 0.0
    if st[-1]=='-' or st[-1]=='+':
        st=st[:len(st)-1]
    if st[0]!='+' and st[0]!='-':
        st="+"+st
    i=2
    while i<len(st):
        if st[i]=='+' or st[i]=='-':
            if st[i]=='-' and (st[i-1]=='*' or st[i-1]=='/' or st[i-1]=='^'):
                i+=1
                continue
            Ch=st[1:i]
            if st[0]=='-': sum-=float(proizvedenie(Ch))
            else: sum+=float(proizvedenie(Ch))
            st=st[i:]
            i=2
        else: i+=1
    if st[0]=='-':
        st = st[1:]
        sum-=float(proizvedenie(st))
    else:
        st = st[1:]
        sum+=float(proizvedenie(st))
    st=str(sum)
    return st
def calc(St):
    i=1
    while i<len(St)-1:
        if St[i]=='(' and St[i-1]!='+' and St[i-1]!='-' and St[i-1]!='*' and St[i-1]!='/' and St[i-1]!='(' and St[i-1]!='^':
            St=St[:i]+"*"+St[i:]
        if St[i]==')' and St[i+1]!='+' and St[i+1]!='-' and St[i+1]!='*' and St[i+1]!='/' and St[i+1]!=')' and St[i+1]!='^':
            St=St[:i+1]+"*"+St[i+1:]
        i+=1
    if St[-1]=='+' or St[-1]=='-':
        St=St[:len(St)-1]
    if St[0]!='+' or St[0]!='-':
        St="+"+St
    while St.find("(")!=-1:
        St2=St[:St.find(')')]
        x=St2.rfind("(")
        St2=St2[x+1:]
        St2=chislo(St2)
        St=St[:x]+St2+St[St.find(')')+1:]
    return chislo(St)