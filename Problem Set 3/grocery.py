def main():
    d = dict()
    while True:
        try:
            g = input().upper()

            if g not in d.keys():
                d[g] = 1
            else:
                d[g]+=1

        except EOFError:
            print()
            a = list(d)
            a.sort()
            for i in a:
                print(d[i],i)
            break
        except KeyError:
            continue
main()
