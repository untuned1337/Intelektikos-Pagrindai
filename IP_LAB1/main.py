import FileOperations

data_file = './Database/WorkingHours.csv'
continuous_file = './Results/ContinuousData_Results.csv'

cdata_list = FileOperations.read_continuous_data(data_file)

FileOperations.write_continuous_data(cdata_list, continuous_file)