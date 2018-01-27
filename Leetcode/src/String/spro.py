# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:32:02 2016

@author: dong.qu
"""

def spro(mystr):
    l = len(mystr)
    if l ==0:
        return False
    if l==1:
        return True
    if l==2:
        return mystr[0]==mystr[1]
    if l>=3:
        for sublen in range(1, l):
            if l%sublen!=0: # this is repeatition
                continue
            else:
                if checksub(mystr, sublen):
                    return True
    return False
            
def checksub(mystr, sublen):
    substr = mystr[:sublen]
    rpt = len(mystr)//sublen
#    print('rpt', rpt)
    for i in range(0, rpt):
#        print(substr, mystr[i*sublen:(i+1)*sublen], i*sublen, (i+1)*sublen)
        if substr != mystr[i*sublen:(i+1)*sublen]:
            return False
    return True
    
mystr = 'abcdabcdabcd'
print(spro(mystr))

def convert(s, numRows):
    if numRows==1:
        return s
    temp = [s]*numRows
    rslt = ['']*numRows
    r=0
    down = True
    for i in range(len(s)):
        rslt[r] += temp[r][i]
        if down:
            r+=1
        else:
            r-=1
        if r==numRows-1:
            down=False
        if r==0:
            down=True
    return ''.join(x for x in rslt)

tstr = "GEEKSFORGEEKS"
print(convert(tstr,3 ), 'expected is GSGS EKFREKEOE')
print(convert('ab', 1 ))

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

def canConstruct(ransomNote, magazine):
    from collections import Counter
    rd = Counter(ransomNote)
    md = Counter(magazine)
    for k in rd:
        if not( k in md and rd[k]<=md[k]):
            return False
    return True

print(canConstruct(ransomNote,magazine))
print(canConstruct('aa','ab'))
print(canConstruct('aabbbc', 'aaabbbbb'))
print(canConstruct('aabbbc', 'aaabbbbcb'))


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    l = len(s)-1
    rslt = 0
    while l>=0 and s[l] == ' ': # l>=0 should occur first as l=-1 will fail for
    # empty string ('')
        l-=1
    while l>=0 and s[l] != ' ':
        rslt +=1
        l-=1
    return rslt
    
print(lengthOfLastWord('sdf sadff '))
print(lengthOfLastWord('       '))
print(lengthOfLastWord(''))
print(lengthOfLastWord('a'))


def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    ver1 = [int(x) for x in version1.split('.')]
    ver2 = [int(x) for x in version2.split('.')]
    l1, l2= len(ver1), len(ver2)
    s = l1-l2
    ver1+=[0]*-s
    ver2+=[0]*s
    for i in range(max(l1, l2)):
        if ver1[i] > ver2[i]:
            return 1
        elif ver1[i] < ver2[i]:
            return -1
    return 0
print(compareVersion('1.2.3.0', '1.2.3'))   



a = [1,3,4,5,6,7,9, 14, 16]

def binsearch(a, val):
    l = 0
    h = len(a)-1
    while l<=h:
        mid = (l+h)//2
        if a[mid] < val:
            l=mid+1
        elif a[mid]>val:
            h=mid-1
        else:
            return mid
    return -1
            
print(binsearch(a, 14))

def isBadVersion(v, badver=0):
    if v>=badver:
        return True
    else:
        return False

def firstBadVersion( n):
    """
    :type n: int
    :rtype: int
    """
    l=1
    h=n
    while l<=h:
        mid = (h+l)//2
        print('mid', mid)
        if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid
        if isBadVersion(mid):
            h = mid-1
        else:
            l = mid+1
            
print(firstBadVersion(10))


def findRadius(houses, heaters):
    """
    :type houses: List[int]
    :type heaters: List[int]
    :rtype: int
    """
    import bisect
    heaters.sort()
    dis=[]
    for h in houses:
        i = bisect.bisect(heaters, h)
        if i==0:
            dis.append(heaters[0]-h)
        if i==len(heaters):
            dis.append(heaters[-1]-h)
        else:
            disr = heaters[i]-h
            disl = h-heaters[i-1]
            dis.append(min(disr, disl))
    return min(dis)
        
        
def arrangeCoins_timelimit( n):
    """
    :type n: int
    :rtype: int
    """
    a = []
    i=1
    while sum(a) <=n:
        a.append(i)
        i+=1
    return i-2
    
def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    i=1
    while i*(i-1)/2<=n:
        i+=1
    return i-2
    
print('Coins')   
print(arrangeCoins(0))
print(arrangeCoins(1))
print(arrangeCoins(2))
print(arrangeCoins(3))
print(arrangeCoins(4))
print(arrangeCoins(5))