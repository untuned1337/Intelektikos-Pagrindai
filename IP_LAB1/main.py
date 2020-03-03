import FileOperations
import Drawing
import Calculations as Cl

data_file = './Database/WorkingHours.csv'
continuous_file = './Results/ContinuousData_Results.csv'
categorical_file = './Results/CategoricalData_Results.csv'

''' SKAITYMAS '''
cont_data_list, tdata_list = FileOperations.read_continuous_data(data_file)
cat_data_list = FileOperations.read_categorical_data(data_file)
all_data = FileOperations.read_all_data(data_file)

''' 2 STEP '''
FileOperations.write_continuous_data(cont_data_list, continuous_file)

''' 3 STEP '''
FileOperations.write_categorical_data(cat_data_list, categorical_file)

''' 4 STEP '''
Drawing.plot_continuous(cont_data_list)
Drawing.plot_categorical(cat_data_list)

''' 5 STEP '''
Drawing.identify_outliers(cont_data_list)

Cl.remove_outliers(all_data)

''' 6 STEP '''
Drawing.scatter_plot(all_data.continuousData)
Drawing.histograms(all_data.categoricalData)

''' 7 STEP '''
Drawing.correlation_matrix(all_data.continuousData)

''' 8 STEP '''
Cl.normalization(all_data.continuousData)

''' 9 STEP '''
all_data.categoricalData = Cl.cat_to_cont(all_data.categoricalData, all_data.continuousData)

