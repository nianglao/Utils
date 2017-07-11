def main():
    fp=open("delta-log.data", "r")
    a={}
    b={}
    idx=0
    cnt=0
    parse_update = False
    parse_inc = False
    parse_dec = False
    for line in fp.readlines():
        words = line.split()
        if len(words) > 2 and words[1] == 'UPDATE':
            print "*"*100
            print 'UPDATE', words[2]
            parse_update = True
            a = {}
        if parse_update and len(words) == 2 and words[1] == 'WHERE':
            parse_inc = True
        if parse_inc and len(words) == 2 and words[1] == 'SET':
            parse_inc = False
            parse_dec = True
            cnt = idx
        if parse_inc:
            a[idx] = words[1]
            idx = idx + 1
        if parse_dec:
            b[cnt-idx] = words[1]
            idx = idx - 1
        if parse_update and cnt != 0 and idx == 0:
            parse_update = False
            parse_dec = False
            for i in range(cnt):
                if i==2 or i==1 or a[i] != b[i]:
                    print a[i],"=>" , b[i]
            cnt = 0

if __name__ == '__main__':
    main()
