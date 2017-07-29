
def neighbors(i, j, valid_index):
    all_neighbors = [(a,b) for a in [i-1, i, i+1] for b in [j-1,j,j+1]]
    valid_neighbors = [(a,b) for (a,b) in all_neighbors if (a,b) in valid_index]
    return valid_neighbors

def amount_value(input1):
    #print(input1)
    nrows = len(input1)
    #print(nrows)
    money = []
    for i in range(0, nrows):
        money.extend(input1[i].split('#'))
    print(money)
    money = [int(x) for x in money]
    
    valid_index = [(i,j) for i in range(nrows) for j in range(nrows)]
    print(valid_index)
    money_map = {}
    for a,(i,j) in enumerate(valid_index):
        money_map[(i,j)] = money[a]
    #print(money_map)
    
    money_neighbor_map = {}
    for a,(i,j) in enumerate(valid_index):
        neighbor = neighbors(i, j, valid_index)
        moneys = [money_map[(i,j)] for (i,j) in neighbor]
        money_neighbor_map[(i,j)] = min(moneys)
    #print(money_neighbor_map)    
    m = max(money_neighbor_map.values())
    
    indices = sorted([k for k, v in money_neighbor_map.items() if v == m])
    
    indices = [(i+1,j+1) for (i,j) in indices]
    
    output = []
    
    for (i,j) in indices:
        output.append(str(i) + '#' + str(j))
        
    return output