import config
import os
from scr import csvhandler, lihandler, dbhandler

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] =  super(Singleton, cls).__call__(*args, **kwargs)
        #else:
            #cls._instances[cls].__init__(*args, *kwargs)
        return cls._instances[cls]


class Out(object):
    __metaclass__ = Singleton

    # db config 
    db = dbhandler.io()
    dbc = db.create_the()
    dbi = db.insert_to()
    dbs = db.select_from()
    dbu = db.update_of()

    
    def get_list_csv(self):
        list_of_csv = []
        getlist = lihandler.GetList()
        list_of_csv = getlist.csv()
        
        return list_of_csv

    def get_enofa_ref(self):
        list_enofa_ref = []
        getdb = self.dbs._enofa_ref()

        datas = {}
        def tname():
            d_tname = []
            for rows in getdb:
                d_tname.append(str(rows[1]))
            return d_tname
        def ref():
            d_ref = []
            for rows in getdb:
                d_ref.append(str(rows[2]))
            return d_ref
        def awal():
            d_awal = []
            for rows in getdb:
                d_awal.append(str(rows[1]))
            return d_awal
        def akhir():
            d_akhir = []
            for rows in getdb:
                d_akhir.append(str(rows[1]))
            return d_akhir
        datas["tname"] = tname()
        datas["ref"] = ref()
        datas["awal"] = awal()
        datas["akhir"] = akhir()
        return datas

    def get_enofa_lists(self, tname):
        data = self.dbs._enofa_lists(tname)
        datali = []
        for li in data:
            if li[1] == 0:
                datali.append(li[0])
        return datali
    def spliting_data(self, tname):
        datali = []
        datali = self.get_enofa_lists(tname)
        a = 0
        x = []
        y = []
        print("total : ", len(datali))
        for i in datali:
            try:
                i = int(i)
                ix = datali.index(i)
                fx = ix + 1
                si = i + 1
                if i != a:
                    if x:
                        y.append(x)
                    x = []
                    x.append(i)
                    a = i + 1
                elif datali[fx] != si:
                    x.append(i)
                    y.append(x)
                    x = []
                else:
                    a = i + 1
            except:
                if i == datali[-1]:
                    x.append(i)
                    y.append(x)
                    x = []
                print('error',i)
                
        for li in y:
            print li

            
        



class In(object):
    __metaclass__ =  Singleton

    # db config 
    db = dbhandler.io()
    dbc = db.create_the()
    dbi = db.insert_to()
    dbu = db.update_of()

    def save_enofa(self, enofa_awal, enofa_akhir):
        # create the Tname , ref, awal, akhir 
        #example enofa awal = 0022012345678, enofa akhir = 0022012345690
        ref =  enofa_awal[:5] # result 00220 in str
        awal = enofa_awal[-8:] #result 12345678 in str
        akhir = enofa_akhir[-8:] #result 12345690 in str
        tname = "enofa" + ref + awal + "to" + akhir #result enofa002201234567_12345690

        val = (tname, ref, awal, akhir)
        enofa =  range(int(awal),int(akhir)+1)
        self.dbi._enofa_ref(val)
        self.dbc._enofa_list(tname)
        self.dbi._enofa_lists(tname,enofa)

    def add_csvfile(self, csv_name):
        cfg = config.cfgDir
        csv_dirfile = os.path.join(cfg.csvdir,csv_name)
        open_csv = csvhandler.pickleData(csv_dirfile)
        collect_data = open_csv.get_data() #collect data = data with str and have ref
        # filtering collect data with enofa ref
        O = Out()
        getenofaref = O.get_enofa_ref()
        ref = getenofaref["ref"]
        tname = getenofaref["tname"]
        dacon = {}
        def slicing():
            for re in ref:
                dacon[re] = []
                for li in collect_data:
                    refrence = li[:5]
                    if refrence == re:
                        dacon[re].append(int(li[-8:]))
            return dacon
        data = slicing()
        for dat in data:
            ix = ref.index(dat)
            table_name = tname[ix]
            datalist = data[dat]
            print table_name
            self.dbu._enofa_lists(table_name,datalist)        



class OnReady:
    """ This class for installing preparation configure zy app"""
    def check_init(self):
        databasefile = os.path.join(config.cfgDir.dbdir, "database.db")
        if os.path.isfile(databasefile):
            has_instaled = True
        else:
            has_instaled = False
        return has_instaled

    def initialize(self):
        print("initialize configure database")
        #init database
        dbIOc =  dbhandler.io.create_the()
        dbIOc._enofa_ref()

        

    
        
        
