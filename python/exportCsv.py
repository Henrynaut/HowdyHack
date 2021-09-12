
import csv

def writeFile(rows):  
    # field names 
    fields = ['PitchValue'] 
        
    # # data rows of csv file 
    # rows = [ ['Nikhil', 'COE', '2', '9.0'], 
    #         ['Sanchit', 'COE', '2', '9.1'], 
    #         ['Aditya', 'IT', '2', '9.3'], 
    #         ['Sagar', 'SE', '1', '9.5'], 
    #         ['Prateek', 'MCE', '3', '7.8'], 
    #         ['Sahil', 'EP', '2', '9.1']] 
    
    with open('pitchData.csv', 'w') as f:
        
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(rows)