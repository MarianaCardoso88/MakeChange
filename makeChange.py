#Algorithm Solution prova Encora

def makeChange (amount):
    coinQuarter = 25
    coinDime = 10
    coinNickel = 5
    coinPenny = 1

    penny = [0,0,0,amount]

    subamount = amount
    nickel = [0,0]
    otherCoin = coinNickel
    for count in range (2):
        nickel.append(subamount // otherCoin)
        subamount = subamount - ((subamount // otherCoin)*otherCoin)
        otherCoin = coinPenny
    
    subamount = amount
    dime = [0]
    otherCoin = coinDime
    for count in range (3):
        dime.append(subamount // otherCoin)
        subamount = subamount - ((subamount // otherCoin)*otherCoin)
        if otherCoin == coinDime:
            otherCoin = coinNickel
        else:
            otherCoin = coinPenny
    
    count = 0
    otherCoin = coinDime
    quarter = []
    qtdQuarters = amount // coinQuarter

    #tentei implementar nesse trecho uma variação do código, tentando variar a quantidade de moedas de 25 a partir do total possível, implementação não está totalmente completa
    #para números inferiores a 25, fica estranho a apresentação (fica cheio de zeros), mas para números acima de 25 já está bem mais interessante

    while count <= qtdQuarters:
        quarter.append(count)
        subamount = subamount - (count*coinQuarter)
        for i in range (3):
            quarter.append(subamount // otherCoin)
            subamount = subamount - ((subamount// otherCoin)*otherCoin)
            if otherCoin == coinDime:
                otherCoin = coinNickel
            elif otherCoin == coinNickel:
                otherCoin = coinPenny
        count = count + 1
        subamount = amount
        otherCoin = coinDime
    
    n = 3
    splited = []
    len_l = len(quarter)
    for i in range(n):
        start = int(i*len_l/n)
        end = int((i+1)*len_l/n)
        splited.append(quarter[start:end])
    
    solution = [penny,nickel,dime,splited]
    print(solution)

#falta implementar também a exclusão de possibilidades repetidas durante a exibição

makeChange(50)
   