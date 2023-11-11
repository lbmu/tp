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
              '\nTotal = Rp. ',
              self.__harga())
        pass

    def __harga(self):
        a = (self.__pertalite * self.__voltalite,
             self.__pertamax * self.__voltamax,
             self.__pertamaxturbo * self.__volturbo)
        return sum(a)
        pass

    pass


yoz = SPBU('yoz')
yoz.hitung(15, 35, 50, 32)
yoz.bensin(8765, 14750, 18865)
yoz.cek()


class AlatTulis:
    def __init__(self, nama):
        self.__hpenggaris = None
        self.__hpulpen = None
        self.__hpensil = None
        self.__penggaris = None
        self.__pulpen = None
        self.__pensil = None
        self.nama = nama

    def barang(self, a, b, c, d, e, f):
        self.__pensil = a
        self.__pulpen = b
        self.__penggaris = c
        self.__hpensil = d
        self.__hpulpen = e
        self.__hpenggaris = f
        pass

    def cekbarang(self):
        print('Jumlah Barang'
              '\nPensil = ', self.__pensil,
              '\nPulpen = ', self.__pulpen,
              '\nPenggaris = ', self.__penggaris)
        pass

    def cekharga(self):
        print('Harga Barang'
              '\nPensil = ', self.__hpensil,
              '\nPulpen = ', self.__hpulpen,
              '\nPenggaris = ', self.__hpenggaris)
        pass

    def cekakhir(self):
        totalbarang, totalharga = self.__total()
        print('Total Barang = ', totalbarang,
              '\nTotal Harga', totalharga)
        pass

    def __total(self):
        cektotal = (self.__pensil, self.__pulpen, self.__penggaris)
        cekharga = (self.__pensil * self.__hpensil,
                    self.__pulpen * self.__hpulpen,
                    self.__penggaris * self.__hpenggaris)
        return sum(cektotal), sum(cekharga)
        pass

    pass


obj = AlatTulis('Yoz')
obj.barang(7, 9, 3, 2500, 7600, 8500)
obj.cekharga()
obj.cekbarang()
obj.cekakhir()
