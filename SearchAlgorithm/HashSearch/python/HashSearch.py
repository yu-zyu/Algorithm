hashTable = list(range(100));

def hash(value):
    return value % 10

target = 12
hashTable[hash(target)] = target

print('ターゲットは{}'.format(hashTable[hash(target)]))
print('場所はhash[{}]'.format(hash(target)))
