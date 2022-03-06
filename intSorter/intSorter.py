def intSorter(number):
    count=0
    list=[int(i) for i in number]
    list.sort()
    while 0 in list:
        list.remove(0)
        count+=1
    for _ in range(count):
        list.insert(1,0)
    list=[str(i) for i in list]
    result=int("".join(list)) ##list 합치는 용도 
    return result

def main():
    number=input()
    result=intSorter(number)
    print(result)

if __name__=='__main__':
    main()
