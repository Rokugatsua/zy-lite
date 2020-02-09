import config, os


class GetList:
    def __init__(self):
        pass
    def csv(self):
        default_csv_dir = config.cfgDir.csvdir
        csv_extn = ".csv"
        list_csv = self.from_dir(default_csv_dir,csv_extn)
        return list_csv
        
    def from_dir(self, dirc, extn):
        list_data = []

        for r, d , f in os.walk(dirc):
            for files in f:
                if extn in files:
                    list_data.append(files)

        return list_data
        
