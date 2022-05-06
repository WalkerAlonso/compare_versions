def checkVersion(v1,v2):
    v1 = [int(x) for x in v1.split('.')]
    v2 = [int(x) for x in v2.split('.')]
    
    limit = min(len(v1),len(v2))
    for i in range(limit):
        if v1[i]>v2[i]:
            return 1
        elif v1[i]<v2[i]:
            return -1
    if len(v1) == len(v2):
        return 0
    
    return 1 if len(v1)!=limit else -1
        
    
    
version1="1.2.9.9.9.9"
version2="1.3.4"
print(checkVersion(version1,version2)) #Expected: -1


version1="1.3.4"
version2="1.3.4"
print(checkVersion(version1,version2)) #Expected: 0


version1="1.10.1"
version2="1.1.9.9"
print(checkVersion(version1,version2)) #Expected: 1