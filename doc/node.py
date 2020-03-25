class Simpul:
    def __init__ (self, nomor, matriks, cost, f, g):
        self.nomor = nomor
        self.matriks = matriks
        self.cost = cost
        self.f = f
        self.g = g
    def setMatriks(self,m):
        self.matriks = m
    def setF(self, cost_from_akar):
        self.f = cost_from_akar
    def setG(self, cost_menuju_goal):
        self.g = cost_menuju_goal
    def setC(self, cost):
        self.c = cost
    def setNo(self,no):
        self.nomor = no
    def print(self):
        print("node ke-"+str(self.nomor))
        print("nilai cost = " + str(self.cost))
        print("nilai cost dari akar = " + str(self.f))
        print("nilai const menuju goal = " + str(self.g))
        print("matriks")
        print(self.matriks)
    def getSimpul(self,no):
        if (self.nomor == no):
            return self

def load_from (file, size):
    mat = [[0 for i in range (size)] for i in range (size)]
    count = 0
    with open(file, 'r') as f:
        for line in f:
            # parsing perbaris
            split = line.split(" ")
            for i in range (0, len(split)):
                mat[count][i] = int(split[i])
            count += 1
    return mat

def tulis_matriks(m):
    for i in range (len(m)):
        for j in range (len(m)):
            if (j == len(m)-1):
                print(m[i][j])
            else:
                print(m[i][j], end=' ')
    print()

def copy_matriks(m):
    res = [[0 for i in range (len(m))] for i in range (len(m))]
    for i in range (len(m)):
        for j in range (len(m)):
            res[i][j] = m[i][j]
    return res

def matriks_to_array (m):
    arr = []
    for j in range (0,len(m)):
        for k in range (0,len(m)):
            arr.append(m[j][k])
    return arr

def kurang(i, init):
    count = i
    for j in range (len(init)):
        if (init[j] == i):
            count -= 1
            break
        elif (init[j] < i and init[j] != 0):
            count -= 1      
    return count

def kurang16(init):
    count = 0
    for i in range (len(init)):
        if (init[i] == 0):
            count += 1
            break
        else:
            count += 1
    return 16-count

def ubin_kosong(m):
    return posisi_X(0,m)%2

def posisi_X(value,m):
    posisi = 0
    for i in range (len(m)):
        for j in range (len(m)):
            if (m[i][j] == value):
                posisi = i+j
                break
    return posisi

def isOkayMoveUp(x, matriks):
    # move up posisi x dikurangi 1
    # cari posisi x di matriks
    xx = 0
    for i in range (len(matriks)):
        for j in range (len(matriks)):
            if (matriks[i][j] == x):
                xx = i
                break
    # cek boleh move up atau tidak
    return (xx-1>=0)

def moveUp(x, m):
    eltemp = 0
    xtemp,ytemp = 0,0
    res_mat = copy_matriks(m)
    for i in range (len(m)):
        for j in range (len(m)):
            # cari elemen yang = x
            if (res_mat[i][j] == x):
                xtemp, ytemp = i,j
                break
    # swap
    eltemp = res_mat[xtemp][ytemp]
    res_mat[xtemp][ytemp] = res_mat[xtemp-1][ytemp]
    res_mat[xtemp-1][ytemp] = eltemp
    return res_mat

def isOkayMoveDown(x, matriks):
    # move up posisi x tambahi 1
    # cari posisi x di matriks
    xx = 0
    for i in range (len(matriks)):
        for j in range (len(matriks)):
            if (matriks[i][j] == x):
                xx = i
                break
    # cek boleh move up atau tidak
    return (xx+1<=3)

def moveDown(x, m):
    eltemp = 0
    xtemp,ytemp = 0,0
    res_mat = copy_matriks(m)
    for i in range (len(m)):
        for j in range (len(m)):
            # cari elemen yang = x
            if (res_mat[i][j] == x):
                xtemp, ytemp = i,j
                break
    # swap
    eltemp = res_mat[xtemp][ytemp]
    res_mat[xtemp][ytemp] = res_mat[xtemp+1][ytemp]
    res_mat[xtemp+1][ytemp] = eltemp
    return res_mat

def isOkayMoveLeft(x, matriks):
    # move up posisi y dikurangi 1
    # cari posisi x di matriks
    xy = 0
    for i in range (len(matriks)):
        for j in range (len(matriks)):
            if (matriks[i][j] == x):
                xy = i
                break
    # cek boleh move up atau tidak
    return (xy-1>=0)

def moveLeft(x, m):
    eltemp = 0
    xtemp,ytemp = 0,0
    res_mat = copy_matriks(m)
    for i in range (len(m)):
        for j in range (len(m)):
            # cari elemen yang = x
            if (res_mat[i][j] == x):
                xtemp, ytemp = i,j
                break
    # swap
    eltemp = res_mat[xtemp][ytemp]
    res_mat[xtemp][ytemp] = res_mat[xtemp][ytemp-1]
    res_mat[xtemp][ytemp-1] = eltemp
    return res_mat

def isOkayMoveRight(x, matriks):
    # cari posisi x di matriks
    xy = 0
    for i in range (len(matriks)):
        for j in range (len(matriks)):
            if (matriks[i][j] == x):
                xy = j
                break
    # cek boleh move up atau tidak
    return (xy+1<=3)

def moveRight(x, m):
    eltemp = 0
    xtemp,ytemp = 0,0
    res_mat = copy_matriks(m)
    for i in range (len(m)):
        for j in range (len(m)):
            # cari elemen yang = x
            if (res_mat[i][j] == x):
                xtemp, ytemp = i,j
                break
    # swap
    eltemp = res_mat[xtemp][ytemp]
    res_mat[xtemp][ytemp] = res_mat[xtemp][ytemp+1]
    res_mat[xtemp][ytemp+1] = eltemp
    return res_mat

def solvable (value):
    return value%2==0

def cost_dari_simpul_ke_goal(mat_simpul, mat_goal):
    count = 0
    for i in range (len(mat_simpul)):
        for j in range (len(mat_simpul)):
            if mat_simpul[i][j] != 0:
                if mat_simpul[i][j] != mat_goal[i][j]:
                    count +=1
    return count

def is_same(m,m1):
    sama = True
    for i in range (len(m)):
        for j in range (len(m)):
            if m[i][j] != m1[i][j]:
                sama = False
                break
    return sama

def is_simpul_unique(simpul, list_simpul):
    # list_simpul bertipe simpul
    unique = True
    for i in range (len(list_simpul)):
        if is_same(simpul, list_simpul[i].matriks) == False:
            unique = False
            break
    return unique

def find_simpul(list_of_simpul, no_simpul):
    # list of simpul bertipe Simpul
    simpul = Simpul(0,[],0,0,0)
    for i in range (len(list_of_simpul)):
        if list_of_simpul[i].nomor == no_simpul:
            simpul = list_of_simpul[i]
            break
    return simpul

matriks_goal = load_from("final.txt",4)
init_conf = load_from("init.txt",4)
print("1. Matriks posisi awal")
tulis_matriks(init_conf)
x = ubin_kosong(init_conf)
print("2. Kurang(i)")
sum = 0
for i in range (1,16):
    print("Kurang(" + str(i) + ") = " + str(kurang(i,matriks_to_array(init_conf))))
    sum += kurang(i,matriks_to_array(init_conf))
print("X = " + str(x))
print()
print("Kurang(" + str(16) + ") = " + str(kurang16(matriks_to_array(init_conf))))
print()
sum += kurang16(matriks_to_array(init_conf))
print("3. Kurang(i)+X = " + str(sum+x))
if (solvable(sum+x)==False):
    print("4. Persoalan tidak dapat diselesaikan")
else:
    import time
    start_time = time.time()
    print("5. Persoalan dapat diselesaikan")
    print()
    print("Matriks input")
    tulis_matriks(init_conf)
    # membuat node dari akar
    akar = Simpul(1,init_conf,0,0,0)
    from queue import PriorityQueue
    simpul_hidup = PriorityQueue()
    # masukkan nomor simpul ke antrian
    simpul_hidup.put((1,akar.nomor))
    idx_simpul_hidup = 1
    nomor_simpul = 1
    tinggi_simpul_dari_akar = 0
    ketemu = False
    # list of simpul
    list_of_simpul = []
    list_of_simpul.append(akar)
    list_of_simpul_yang_dibangkitkan = []
    simpul_yang_dibangkitkan = 0
    while (ketemu == False):
        # menyimpan list akar dari suatu node
        list_cost_akar = []
        tinggi_simpul_dari_akar += 1
        key, value = simpul_hidup.get()
        akar = find_simpul(list_of_simpul,value)
        # cek available move dari akar
        if (isOkayMoveUp(0,akar.matriks)):
            nomor_simpul += 1
            up = moveUp(0,akar.matriks)
            #if (is_simpul_unique(up,list_cost_akar)):
            g = cost_dari_simpul_ke_goal(up,matriks_goal)
            f = tinggi_simpul_dari_akar
            simpulUp = Simpul(nomor_simpul,up,f+g,f,g)
            list_cost_akar.append(simpulUp)
            list_of_simpul.append(simpulUp)
        if (isOkayMoveRight(0,akar.matriks)):
            nomor_simpul += 1
            right = moveRight(0,akar.matriks)
            #if (is_simpul_unique(right,list_cost_akar)):
            g = cost_dari_simpul_ke_goal(right,matriks_goal)
            f = tinggi_simpul_dari_akar
            simpulRight = Simpul(nomor_simpul,right,f+g,f,g)
            list_cost_akar.append(simpulRight)
            list_of_simpul.append(simpulRight)
        if (isOkayMoveDown(0,akar.matriks)):
            nomor_simpul += 1
            down = moveDown(0,akar.matriks)
            #if (is_simpul_unique(down,list_cost_akar)):
            g = cost_dari_simpul_ke_goal(down,matriks_goal)
            f = tinggi_simpul_dari_akar
            simpulDown = Simpul(nomor_simpul,down,f+g,f,g)
            list_cost_akar.append(simpulDown)
            list_of_simpul.append(simpulDown)
        if (isOkayMoveLeft(0,akar.matriks)):
            nomor_simpul += 1
            left = moveLeft(0,akar.matriks)
            #if (is_simpul_unique(left,list_cost_akar)):
            g = cost_dari_simpul_ke_goal(left,matriks_goal)
            f = tinggi_simpul_dari_akar
            simpulLeft = Simpul(nomor_simpul,left,f+g,f,g)
            list_cost_akar.append(simpulLeft)
            list_of_simpul.append(simpulLeft)
        #print("banyak simpul yg telah dibangkitkan:", nomor_simpul)
        # cari cost dari simpul yg nilainya paling kecil
        for i in range (len(list_cost_akar)):
            for j in range (0,len(list_cost_akar)-i-1):
                if list_cost_akar[j].cost > list_cost_akar[j+1].cost:
                    list_cost_akar[j],list_cost_akar[j+1] = list_cost_akar[j+1],list_cost_akar[j]
        print("f(i) =", list_cost_akar[0].f)
        print("g(i) =", list_cost_akar[0].g)
        print("c(i) = f(i) + g(i) =", list_cost_akar[0].cost)
        tulis_matriks(list_cost_akar[0].matriks)
        # hanya cost yang paling kecil yang jadi prioritas sisanya antrian biasa
        simpul_hidup.put((0, list_cost_akar[0].nomor))
        if (tinggi_simpul_dari_akar == 1):
            for i in range (1,len(list_cost_akar)):
                simpul_hidup.put((i, list_cost_akar[i].nomor))
                idx_simpul_hidup += 1
        else:
            for i in range (1,len(list_cost_akar)):
                simpul_hidup.put((idx_simpul_hidup, list_cost_akar[i].nomor))
                idx_simpul_hidup += 1
        
        # membangkitkan tiap anak dari node
        
        if (is_same(list_cost_akar[0].matriks, matriks_goal)):
            ketemu = True
    print("6. Waktu eksekusi", end=" ")
    print("%s detik" % (time.time() - start_time))
    print("7. Jumlah simpul yang dibangkitkan")
    