
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv(r'D:\Project\Emergency Nav\Emergency Nav\data\crime.csv')
X = dataset.iloc[0:155, 0].values
y1 = dataset.iloc[:, 10].values
y2 = dataset.iloc[:, 11].values


sum_values = dataset[['murder', 'rape', 'gangrape', 'robbery', 'theft', 'assualt murders', 'sexual harassement','totalcrime']].sum(axis=1)

min_value = sum_values.min()
max_value = sum_values.max()
new_min = 1
new_max = 5

scaled_values = ((sum_values - min_value) / (max_value - min_value)) * (new_max - new_min) + new_min


mag_values = list(np.round(scaled_values))

places =['Nagala Park', 'Shahupuri', 'Tarabai Park', 'Kadamwadi','Shivaji Park', 'Rankala', 'Phulewadi', 'Rukmini Nagar',
       'Mangalwar Peth', 'Shahaji Umarane', 'Shivane', 'Raviwar Peth','Kolhapur City', 'Rajarampuri', 'Shiroli', 'Ichalkaranji',
       'Uchgaon', 'Gokul Shirgaon', 'Valivade', 'Kagal', 'Jayanthi Nagar','Shivaji Udyam Nagar', 'Gandhinagar', 'New Shahupuri',
       'Mahadwar Road', 'Shantinagar', 'Rajopadhye Nagar', 'Peth Vadgaon','Warana Nagar', 'Mangasuli', 'Kavala Naka', 'Rukadi',
       'Hatkanangale', 'Morewadi', 'Sane Guruji Nagar', 'Malkapur','Budhwar Peth', 'Gokak Falls', 'Haripuri', 'Siddhagiri Math',
       'Kagal Five Star MIDC', 'Shelke Nagar', 'Shukrawar Peth','Bhendwade', 'Kadamwadi', 'Shahupuri East',
       'Babanrao Padval Nagar', 'Shinganapur', 'Rankala Market', 'Shirol','Siddhivinayak Nagar', 'Sukhada Colony', 'Yamunachya Variche',
       'Chandgad', 'Kaneri', 'Gandhinagar', 'Tal Panhala', 'Padali Khurd','Phulewadi', 'Kavala Naka', 'Ichalkaranji Road', 'Phulewadi',
       'Kolhapur Railway Station', 'New Shahupuri', 'Mahadwar Road','Shantinagar', 'Rajopadhye Nagar', 'Peth Vadgaon', 'Warana Nagar',
       'Mangasuli', 'Kavala Naka', 'Rukadi', 'Hatkanangale', 'Morewadi','Sane Guruji Nagar', 'Malkapur', 'Budhwar Peth', 'Gokak Falls',
       'Haripuri', 'Siddhagiri Math', 'Kagal Five Star MIDC','Shelke Nagar', 'Shukrawar Peth', 'Bhendwade', 'Kadamwadi',
       'Shahupuri East', 'Babanrao Padval Nagar', 'Shinganapur','Rankala Market', 'Shirol', 'Siddhivinayak Nagar',
       'Sukhada Colony', 'Yamunachya Variche', 'Chandgad', 'Kaneri','Gandhinagar', 'Tal Panhala', 'Padali Khurd', 'Phulewadi',
       'Kavala Naka', 'Ichalkaranji Road', 'Phulewadi','Kolhapur Railway Station', 'Vivekanand Colony', 'Gadikhana',
       'Nagala Park', 'Shahupuri West', 'Panchganga Ghat', 'Jadhavwadi','Tarabai Park', 'Gokul Shirgaon', 'Rajarampuri',
       'Dabholkar Corner', 'Kadamwadi', 'Sane Guruji Nagar', 'Udyamnagar','Kadamwadi', 'Shahupuri East', 'Tarabai Park', 'Jadhavwadi',
       'Shahupuri West', 'Panchganga Ghat', 'Gokul Shirgaon','Rajarampuri', 'Gadikhana', 'Sane Guruji Nagar',
       'Dabholkar Corner', 'Kadamwadi', 'Gandhinagar', 'Udyamnagar','Vivekanand Colony', 'Shahupuri East', 'Nagala Park',
       'Ichalkaranji Road', 'Rankala Market', 'Kadamwadi', 'Morewadi','Shirol', 'Shukrawar Peth', 'Gokak Falls', 'Bhendwade',
       'Kolhapur Railway Station', 'Shukrawar Peth', 'Gandhinagar','Siddhivinayak Nagar', 'Sukhada Colony', 'Yamunachya Variche',
       'Chandgad', 'Kavala Naka', 'Vivekanand Colony', 'Gadikhana','Nagala Park', 'Shahupuri West', 'Panchganga Ghat','Gokul Shirgaon', 'Rajarampuri']

new_array= []

for i in range(0, 155):
    str = places[i]+", Kolhapur, India"
    new_array.append(str)
dataset2 = pd.read_csv(r'D:\Project\Emergency Nav\Emergency Nav\data\crime.csv')
lati = dataset2.iloc[:, 0].values
longi = dataset2.iloc[:, 1].values

ar = []
   
for i in range(0, 156):
    y1[i] = round(y1[i], 4)
    y2[i] = round(y2[i], 4)

    o = {  "type": "Feature",
           "properties": { 'mag': mag_values[i]   },                 
            'lati': y1[i], 
            'longi': y2[i]
        }
    ar.append(o)
print(ar)