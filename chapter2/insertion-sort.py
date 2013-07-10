def insertion_sort(wlist):
    temp = 0
    for j in range(1,len(wlist)):
        i = j-1
        key = wlist[j]
        while i>=0 and wlist[i] > key:
            temp = wlist[i+1]
            wlist[i+1] = wlist[i]
            wlist[i] = temp
            i = i-1
    print wlist
        
if __name__ == "__main__":
    l = [5,2,4,6,67,13,1,0]
    insertion_sort(l)
