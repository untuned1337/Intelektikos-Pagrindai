import FileOperations
import Calculations

data_file = './Database/WorkingHours.csv'
continuous_file = './Results/ContinuousData_Results.csv'
categorical_file = './Results/CategoricalData_Results.csv'

cont_data_list = FileOperations.read_continuous_data(data_file)
FileOperations.write_continuous_data(cont_data_list, continuous_file)

cat_data_list = FileOperations.read_categorical_data(data_file)
#print(Calculations.count_distinct_values(cat_data_list.occupation_list))
Calculations.most_frequent(cat_data_list.occupation_list)
