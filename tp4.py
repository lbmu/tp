class SPBU:
    def __init__(self, nama):
        self.__volturbo = None
        self.__voltamax = None
        self.__voltalite = None
        self.__knd = None
        self.nama = nama
        self.__pertalite = None
        self.__pertamax = None
        self.__pertamaxturbo = None

    def hitung(self, a, b, c, d):
        self.__knd = a
        self.__voltalite = b
        self.__voltamax = c
        self.__volturbo = d
        pass

    def bensin(self, x, y, z):
        self.__pertalite = x
        self.__pertamax = y
        self.__pertamaxturbo = z
        pass

    def cek(self):
        print('Nama = ', self.nama,
              '\nKendaraan = ', self.__knd,
              '\nPertalite = ', self.__voltalite, 'L'
              '\nPertamax = ', self.__voltamax, 'L'
              '\nTurbo = ', self.__volturbo, 'L'
              '\nTotal = Rp. ', self.__harga())
        pass

    def __harga(self):
        a = []
        a.append(self.__pertalite * self.__voltalite)
        a.append(self.__pertamax * self.__voltamax)
        a.append(self.__pertamaxturbo * self.__volturbo)
        return sum(a)
        pass

    pass


yoz = SPBU('yoz')
yoz.hitung(15, 35, 50, 32)
yoz.bensin(8765, 14750, 18865)
yoz.cek()


