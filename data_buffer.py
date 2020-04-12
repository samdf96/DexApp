import os
import glob
import pandas as pd


def data_loader(gen_start, gen_end, column_slice, saves_dir, output_base):
    # Creating Test Directory if none is found:
    if not os.path.exists(saves_dir):
        os.mkdir(saves_dir)

    # Creating list of files, in sorted order
    file_list = sorted(glob.glob(saves_dir + '*.csv'))
    # Need to extract latest entry and number to create new save state
    import_file = file_list[-1]
    save_number = int(import_file.split('_')[-1][:-4])
    export_filename = saves_dir + output_base + str(save_number+1).zfill(4) + '.csv'

    # Load data
    data = pd.read_csv(import_file, sep=',', header=0)
    data = data.iloc[gen_start:gen_end, 0:column_slice]
    # Replacing 'Yes/'No' with True/False
    data = data.replace(to_replace='Yes', value=True)
    data = data.replace(to_replace='No', value=False)

    # Creating Dictionary for Data Buffer
    db = {}
    return data, db, export_filename


def exporter(filename, data_buffer, import_data):
    # Checking for empty data buffer
    if not bool(data_buffer):
        print('Empty Data Buffer found. File export rejected.')
        return
    # Copying imported data and applying data_buffer entries
    data_copy = import_data
    for item in data_buffer:
        # Change Entry, Lucky, FC
        data_copy.loc[data_copy['Name'] == item, 'Entry'] = data_buffer[item]['Entry']
        data_copy.loc[data_copy['Name'] == item, 'Lucky'] = data_buffer[item]['Lucky']
        data_copy.loc[data_copy['Name'] == item, 'FC'] = data_buffer[item]['FC']

    # Changing True/False values back to 'Yes'/'No'
    data_copy = data_copy.replace(to_replace=True, value='Yes')
    data_copy = data_copy.replace(to_replace=False, value='No')
    data_copy.to_csv(filename, index=False)
    return


def entry_maker(name, toggle, import_data, data_buffer,
                column=None, value=None):
    d = {name: {}}
    if column != 'Entry' or toggle == 'entry':
        d[name]['Entry'] = import_data.loc[import_data['Name'] == name]['Entry'][0]
    if column != 'Lucky' or toggle == 'entry':
        d[name]['Lucky'] = import_data.loc[import_data['Name'] == name]['Lucky'][0]
    if column != 'FC' or toggle == 'entry':
        d[name]['FC'] = import_data.loc[import_data['Name'] == name]['FC'][0]
    # Finally write the given column/value pair if 'toggle' if 'database'
    if toggle == 'database':
        d[name][column] = value

    if toggle == 'database':
        data_buffer[name] = d[name]
    elif toggle == 'entry':
        return d


class Row:
    def __init__(self, data_row, data_buffer, import_data):
        print('Being Created.')
        print('Lucky data', data_row['Lucky'])
        self.name = data_row['Name']
        self.dex_number = str(data_row['Pokedex Number'])
        self.type1 = str(data_row['Type 1']).lower()
        self._entry = data_row['Entry']
        self._lucky = data_row['Lucky']
        self._fc = data_row['FC']
        self.data_buffer = data_buffer
        self.import_data = import_data

    def data_logger(self, column, value):
        if self.name in self.data_buffer:
            # Entry found in database -> Check if different
            if self.data_buffer[self.name][column] != value:
                self.data_buffer[self.name][column] = value

            # Delete dc entry if same as imported data
            if self.data_buffer[self.name] == entry_maker(self.name,
                                                          'entry',
                                                          self.import_data,
                                                          self.data_buffer):
                del self.data_buffer[self.name]
        else:
            # Entry not found in database -> Add into database
            entry_maker(self.name, 'database',
                        self.import_data, self.data_buffer,
                        column, value)

    @property
    def entry(self):
        return self._entry

    @entry.setter
    def entry(self, value):
        self._entry = value
        self.data_logger('Entry', value)

    @property
    def lucky(self):
        print('Getter Accessed.')
        return self._lucky

    @lucky.setter
    def lucky(self, value):
        self._lucky = value
        self.data_logger('Lucky', value)

    @property
    def fc(self):
        return self._fc

    @fc.setter
    def fc(self, value):
        self._fc = value
        self.data_logger('FC', value)