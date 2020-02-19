import FileOperations
import Drawing

data_file = './Database/WorkingHours.csv'
continuous_file = './Results/ContinuousData_Results.csv'
categorical_file = './Results/CategoricalData_Results.csv'

cont_data_list = FileOperations.read_continuous_data(data_file)
FileOperations.write_continuous_data(cont_data_list, continuous_file)

cat_data_list = FileOperations.read_categorical_data(data_file)
FileOperations.write_categorical_data(cat_data_list, categorical_file)

Drawing.plot_continuous(cont_data_list)
Drawing.identify_outliers(cont_data_list)
