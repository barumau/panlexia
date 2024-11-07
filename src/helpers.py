import csv

class csv_reader:
    """Helper for opening and closing a CSV or TSV file for reading."""
    def __init__(self, file_name, delimiter):
        self.file = open(file_name, 'r')
        self.dict = csv.DictReader(self.file, delimiter=delimiter)

    def __del__(self):
        self.file.close()

class tsv_reader:
    """Helper for opening and closing a TSV file for reading."""
    def __init__(self, file_name):
        self.file = open(file_name, 'r')
        self.dict = csv.DictReader(self.file, delimiter='\t')

    def __del__(self):
        self.file.close()

class tsv_writer:
    """Helper for opening and closing a TSV file for writing."""
    def __init__(self, file_name, open_mode):
        self.file = open(file_name, open_mode)
        self.dict = csv.writer(self.file, delimiter='\t')

    def __del__(self):
        self.file.close()

def get_other_id_to_Panlexia_id_map(other_id):
    """Creates a dictionary of ULD to Panlexia ids."""
    master_file = 'data/master.tsv'
    master = tsv_reader(master_file)
    map_to_Panlexia = {}
    for row in master.dict:
        if row[other_id] != "":
            map_to_Panlexia[row[other_id]] = row["id"]
    return map_to_Panlexia

class simple_file_reader:
    def __init__(self, filename):
        try:
            self.file = open(filename, 'r')
        except OSError:
            print("Error in reading file", filename)

    def __del__(self):
        self.file.close()

    def readline(self):
        return self.file.readline()

class simple_file_writer:
    def __init__(self, filename):
        try:
            self.file = open(filename, 'w')
        except OSError:
            print("Error in opening file", filename)

    def __del__(self):
        self.file.close()

    def write(self, text_string):
        return self.file.write(text_string)
