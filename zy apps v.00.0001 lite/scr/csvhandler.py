import csv

class pickleData:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.datapick = []
        self._open_csv()

    def _open_csv(self):
        print("open csv")
        temp_data = []
        print("csv file",self.csv_file)
        with open(self.csv_file) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            for rows in csvreader:
                if rows[0] == "FK":
                    if rows[3] != "NOMOR_FAKTUR":
                        x = rows[3]
                        temp_data.append(x)

        self.datapick = temp_data

    def get_data(self):
        return self.datapick
                        
                        
