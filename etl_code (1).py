import pandas as pd
import glob
import xml.etree.ElementTree as ET 
from datetime import datetime

log_file = "log_file.txt"
target_file = 'transform_data.csv'

def  extract_from_csv(file_to_process):
    dataframe = pd.dataframe(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    dataframe= pd.dataframe(file_to_process)
    return dataframe

def extract_from_xml(file_to_process):
    dataframe = pd.dataframe(columns = ['name','height','weight'])
    tree = ET.parse(file_to_process)
    root= tree.getroot()

    for person in root:
        name= person.find("name").text
        height=person.find("height").text
        weight=person.find("weight").text
        dataframe = pd.concat([dataframe,pd.dataframe([{"name":name, "height": height, "weight": weight}])],ignore_index =True)
    return dataframe

def extract():
    extract_data = pd.dataframe(columns=['name','height','weight'])

    for  csvfile in glob.glob("*.csv"):
        extract_data = pd.concat([extract_data, pd.dataframe(extract_from_csv(csvfile))], ignore_index = True)

    for jsonfile in glob.glob("*.json"):
        extract_data = pd.concat([extract_data, pd.dataframe(extract_from_json(jsonfile))],ignore_index=True)
    
    for xmlfile in glob.glob("*.xml"):
        extract_data = pd.concat([extract_data, pd.dataframe(extract_from_xml(xmlfile))],ignore_index=True)

    return extract_data

def transform(data):
    data['height'] = round(data.height* 0.0254,2)
    data['weight']= round(data.weight*0.45359237,2)

    return data

def load_data(target_file, transform_data):
    transform_data.to_csv(target_file)

def log_progress(message):
    timestamp_formate = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_formate)
    with open(load_data,'a') as f:
        f.write(timestamp + ' , ' + message + '\n')

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended")