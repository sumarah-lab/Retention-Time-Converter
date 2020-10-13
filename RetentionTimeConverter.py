import pandas as pd
from scipy.interpolate import Akima1DInterpolator
import numpy as np
import PySimpleGUI as sg

def main():
	layout = [[sg.Text('Convert Retention Times')],
              [sg.Text('Reference File', size=(18, 1)), sg.InputText(), sg.FileBrowse()],
              [sg.Text('Conversion File', size=(18, 1)), sg.InputText(), sg.FilesBrowse()],
              [sg.Text('Output Folder', size=(18,1)), sg.InputText(), sg.FolderBrowse()],
              [sg.Text('Output Data File Name', size=(18, 1)), sg.InputText()],
              [sg.Button('Convert'), sg.Exit()]]

	window = sg.Window('Retention Index Converter', layout)
	while True:
		event, values = window.Read()
		if event is None or event == 'Exit':
			break
		if event == 'Convert':
			reference_path, database_path, save_folder, save_file_tag = values[0], values[1], values[2], values[3]
			for file in database_path.split(";"):
				if (save_file_tag.endswith('.csv')):
					save_file_path = (save_folder + "/" + save_file_tag)
				else:
					save_file_path = (save_folder + "/" + save_file_tag + ".csv")	
				convertFile(reference_path, database_path,  save_file_path)
			
			sg.Popup('Conversion Complete')
				
	window.Close()

def convertFile(referenceFile, databaseFile, save_file_path):
	#Open reference file and calculate spline function for RT conversion
	if (referenceFile.endswith('.csv') and databaseFile.endswith('.csv')):
		## Calculate Spline Function
		data = pd.read_csv(referenceFile)

		index = data.iloc[:, 0].values
		ref_retention_time = data.iloc[:, 1].values
		
		#Start interpolator function
		cs = Akima1DInterpolator(ref_retention_time, index)

        #Open mzML conversion file
		rawFile = pd.read_csv('Compounds.csv')
        
		##convert the retention times or retention indices and save output
		newFile = pd.DataFrame({'Compounds':rawFile.iloc[:,0], 'Converted':cs(rawFile.iloc[:,1].values)})
	
		print('test')
		newFile.to_csv(save_file_path,index=False)
		
	else:
		sg.PopupError(
		'Wrong data format. Please select a .csv file for the reference file and a .csv file for the data file.')

main()