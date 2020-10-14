
def scrambled_eggs(recepies, list):
    for x in range(0, len(recepies)):
        if recepies[x] == 'scrambled eggs':
            list.append('eggs')
            list.append('ham')
            list.append('butter')

def spaghetti(recepies, list):
    for x in range(0, len(recepies)):
        if recepies[x] == 'spaghetti':
            list.append('spaghetti pasta')
            list.append('spaghetti sauce')
            list.append('parmesan')

def mascarpone_salomon(recepies, list):
    for x in range(0, len(recepies)):
        if recepies[x] == 'mascarpone salomon':
            list.append('salomon fillet')
            list.append('pappardelle pasta')
            list.append('mascarpone')
            list.append('capares')

def korean_fried_pork(recepies, list):
    for x in range(0, len(recepies)):
        if recepies[x] == 'korean fried pork':
            list.append('pork belly')
            list.append('rice')
            list.append('carrots')
            list.append('bell peppers')
            list.append('gochuchang paste')