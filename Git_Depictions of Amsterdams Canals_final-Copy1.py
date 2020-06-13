#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Let's try converting each individual canal dataframe into a list to see what we're working with!
#Starting with the Singel

import pandas as pd
rijks = pd.read_csv('/Users/anikhash/Desktop/Rijksdataset.csv',low_memory=False)
rijks_top = rijks.head()
rijks_top
#DropNaN
rijks.dropna()
rijks.drop(['objectInventoryNumber', 'objectImage',             
            'objectPersistentIdentifier'], axis = 1, inplace = True) 
rijks.reset_index(drop=True, inplace=True)

# SOLUTION FOR FINDING A SPECIFIC STRING IN A SPECIFIC COLUMN / Don't forget NAN
singel2 =  rijks[rijks['objectTitle[1]'].str.contains('Singel', na=False)]
print(singel2.to_string())

#Counting how many instances of this canal show ups up in depictions of art is 227
singel2.dropna()
singel2['objectType[1]'].count()

#Another way of counting the amount of items, which is again 227 
singel2.info()

#The amount of artistic depictions of the Singel are 227...now let's filter for photo depictions of it

#Filtering for photos
singel2[singel2['objectType[1]'].str.contains("foto")==True]

#Filtering for photos
singel_3 = singel2[singel2['objectType[1]'].str.contains("foto")==True]

#Try not changing it to a list and SORT THE DATA FRAME!
type(singel_3)
singel4 = singel_3.sort_values(by='objectType[1]', ascending=False, na_position='first')
singel4.dropna()

#Display the entire dataframe
from IPython.display import display, HTML
display(HTML(singel4.to_html()))

#Display the filtered dataframe for PHOTOS only
singel_df_filtered = singel4[singel4['objectType[1]'] == 'foto']

from IPython.display import display, HTML
display(HTML(singel_df_filtered.to_html()))

#The amount of photos of the Singel canal are 66
singel_df_filtered.count()

#So the amount of original art depictions are 227 and the photo depictions are 66
singel_df_filtered.info()

#SINGEL - Original art depictions = 227
#SINGEL - Photo depictions = 66

#1/4 canals done

#For the Herengracht canal
import pandas as pd
rijks = pd.read_csv('/Users/anikhash/Desktop/Rijksdataset.csv',low_memory=False)
rijks_top = rijks.head()
rijks_top
rijks.dropna()
rijks.drop(['objectInventoryNumber', 'objectImage',             
            'objectPersistentIdentifier'], axis = 1, inplace = True) 
rijks.reset_index(drop=True, inplace=True)

#  SOLUTION FOR FINDING A SPECIFIC STRING IN A SPECIFIC COLUMN / Don't forget NAN
herengracht =  rijks[rijks['objectTitle[1]'].str.contains('Herengracht', na=False)]
print(herengracht.to_string())

#Counting how many instances of this canal show ups up in depictions of art is 190
herengracht.dropna()
herengracht['objectType[1]'].count()

#Another way of counting the amount of items, which is 190
herengracht.info()

#The amount of artistic depictions of the Singel are 190
#...now let's filter for photo depictions of it!

#Filtering for photos
herengracht[herengracht['objectType[1]'].str.contains("foto")==True]

#Filtering for photos
herengracht_fotos = herengracht[herengracht['objectType[1]'].str.contains("foto")==True]

#Try not changing it to a list and SORT THE DATA FRAME!
type(herengracht_fotos)

herengracht_df = herengracht_fotos.sort_values(by='objectType[1]', ascending=False, na_position='first')
herengracht_df.dropna()

#Display the entire dataframe
from IPython.display import display, HTML
display(HTML(herengracht_df.to_html()))

#Display the filtered dataframe for PHOTOS only
herengracht_df_filtered = herengracht_df[herengracht_df['objectType[1]'] == 'foto']

from IPython.display import display, HTML
display(HTML(herengracht_df_filtered.to_html()))

#The amount of photos of the Singel canal are 48
herengracht_df_filtered.count()

#So the amount of original art depictions are 190 and the photo depictions are 48
herengracht_df_filtered.info()

#HERENGRACHT - Original art depictions = 190
#HERENGRACHT - Photo depictions = 48

#2/4 canals done

#For the Keizersgracht canal
import pandas as pd
k_rijks = pd.read_csv('/Users/anikhash/Desktop/Rijksdataset.csv',low_memory=False)
k_rijks_top = k_rijks.head()
k_rijks_top
k_rijks.dropna()
k_rijks.drop(['objectInventoryNumber', 'objectImage',             
            'objectPersistentIdentifier'], axis = 1, inplace = True) 
k_rijks.reset_index(drop=True, inplace=True)
#  SOLUTION FOR FINDING A SPECIFIC STRING IN A SPECIFIC COLUMN / Don't forget NAN
keizersgracht =  k_rijks[k_rijks['objectTitle[1]'].str.contains('Keizersgracht', na=False)]
print(keizersgracht.to_string())

#Counting how many instances of this canal show ups up in depictions of art is 183
keizersgracht['objectType[1]'].count()

#Filtering for photos
keizersgracht[keizersgracht['objectType[1]'].str.contains("foto")==True]
keizersgracht.count()

#The amount of artistic depictions of the Keizersgracht are 183
#...now let's filter for photo depictions of it!

#Filtering for photos
keizersgracht[keizersgracht['objectType[1]'].str.contains("foto")==True]

#Filtering for photos
keizersgracht_fotos = keizersgracht[keizersgracht['objectType[1]'].str.contains("foto")==True]

#Try not changing it to a list and SORT THE DATA FRAME!
type(keizersgracht_fotos)

keizersgracht_df = keizersgracht_fotos.sort_values(by='objectType[1]', ascending=False, na_position='first')
keizersgracht_df.dropna()

#Display the entire dataframe
from IPython.display import display, HTML
display(HTML(keizersgracht_df.to_html()))

#Display the filtered dataframe for PHOTOS only
keizersgracht_df_filtered = keizersgracht_df[keizersgracht_df['objectType[1]'] == 'foto']

from IPython.display import display, HTML
display(HTML(keizersgracht_df_filtered.to_html()))

#The amount of photos of the Keizersgracht canal are 
keizersgracht_df_filtered.count()

#So the amount of original art depictions are 183 and the photo depictions are 35
keizersgracht_df_filtered.info()

#KEIZERSGRACHT - Original art depictions = 183
#KEIZERSGRACHT - Photo depictions = 35

#3/4 canals done

#PRINSENGRACHT
#For the Prinsengracht canal
import pandas as pd
p_rijks = pd.read_csv('/Users/anikhash/Desktop/Rijksdataset.csv',low_memory=False)
p_rijks_top = p_rijks.head()
p_rijks_top
p_rijks.dropna()
p_rijks.drop(['objectInventoryNumber', 'objectImage',             
            'objectPersistentIdentifier'], axis = 1, inplace = True) 
p_rijks.reset_index(drop=True, inplace=True)

#  SOLUTION FOR FINDING A SPECIFIC STRING IN A SPECIFIC COLUMN / Don't forget NAN
prinsengracht =  p_rijks[p_rijks['objectTitle[1]'].str.contains('Prinsengracht', na=False)]
print(prinsengracht.to_string())

#Counting how many instances of this canal show ups up in depictions of art is 95
prinsengracht['objectType[1]'].count()

#Another way of counting the amount of items, which is 95
prinsengracht.dropna()
prinsengracht.info()

#The amount of artistic depictions of the Prinsengracht are 95
#...now let's filter for photo depictions of it!

#Filtering for photos
prinsengracht[prinsengracht['objectType[1]'].str.contains("foto")==True]
prinsengracht.count()

#Filtering for photos
prinsengracht[prinsengracht['objectType[1]'].str.contains("foto")==True]

#Filtering for photos
prinsengracht_fotos = prinsengracht[prinsengracht['objectType[1]'].str.contains("foto")==True]

#Try not changing it to a list and SORT THE DATA FRAME!
type(prinsengracht_fotos)

prinsengracht_df = prinsengracht_fotos.sort_values(by='objectType[1]', ascending=False, na_position='first')
prinsengracht_df.dropna()

#Display the entire dataframe
from IPython.display import display, HTML
display(HTML(prinsengracht_df.to_html()))

#Display the filtered dataframe for PHOTOS only
prinsengracht_df_filtered = prinsengracht_df[prinsengracht_df['objectType[1]'] == 'foto']

from IPython.display import display, HTML
display(HTML(prinsengracht_df_filtered.to_html()))

#The amount of photos of the Keizersgracht canal are 
prinsengracht_df_filtered.count()

#So the amount of original art depictions are #### and the photo depictions are ####
prinsengracht_df_filtered.info()

#PRINSENGRACHT - Original art depictions = 95
#PRINSENGRACHT - Photo depictions = 17

#4/4 canals done

import matplotlib.pyplot as plt

# Data to plot
labels = 'Singel', 'Herengracht', 'Keizersgracht', 'Prinsengracht'
sizes = [227, 190, 183, 95]
colors = ['gold', 'peachpuff', 'darkorange', 'burlywood']
explode = (0, 0, 0, 0) 

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.title("Depictions of all canals in art prior to 1826")
plt.show()

######## PIE CHART PHOTOS ##########

import matplotlib.pyplot as plt

# Data to plot
labels = 'Singel', 'Herengracht', 'Keizersgracht', 'Prinsengracht'
sizes = [66, 48, 35, 17]
colors = ['gold', 'peachpuff', 'darkorange', 'burlywood']
explode = (0, 0, 0, 0) 

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.title("Depictions of canals in photos after 1826")
plt.show()

#Next steps - extract Prinsengracht,
#Create images and pie plots for those
#Let's start by creating the CSV and then doing the object count
#Prinsengracht

import pandas as pd
rijks = pd.read_csv('/Users/anikhash/Desktop/Rijksdataset.csv',low_memory=False)
rijks_top = rijks.head()
rijks_top
#DropNaN
rijks.dropna()
rijks.drop(['objectInventoryNumber',              
            'objectPersistentIdentifier'], axis = 1, inplace = True) 
rijks.reset_index(drop=True, inplace=True)
prinsengracht_experiment =  rijks[rijks['objectTitle[1]'].str.contains('Prinsengracht', na=False)]
prinsengracht_experiment.dropna()
prinsengracht_experiment['objectType[1]'].value_counts('')

import tkinter as tk
from tkinter import filedialog
from pandas import DataFrame

df = DataFrame(prinsengracht_experiment, columns= ['objectTitle[1]','objectType[1]', 'objectCreator[1]', 'objectCreationDate[1]','objectImage'])

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def exportCSV ():
    global df
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = None, header=True)

saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()
#SINGEL PIE PLOT
import pandas as pd
df = pd.DataFrame({    'Object Type': [66, 51, 51, 20, 14, 7, 5, 5, 3, 2, 1,1,1]},
                  index=['Fotos/Photos', 'Prent/painting', 'Schetsboekblad/sketch', 
'Stereofoto', 'Tekening/drawing', 'Fotomechanische afdruk', 'Schilderij', 
'Affice', 'Ektachrome', 'Digitaal bestand', 'Fotomechanisch procedé', 
'Negatief', 'Ex libris'])
plot = df.plot.pie(y='Object Type', figsize=(25,21), colors = ['gold', 'peachpuff', 'darkorange', 
          'burlywood', 'palegoldenrod', 'tomato', 'wheat', 'lightsalmon','lightslategray',
                                                                
         'coral', 'khaki', 'cornflowerblue','aqua'], labeldistance=1.05, radius=1,textprops={'fontsize': 10}, autopct='%1.1f%%')

######
#For the Herengracht canal
import pandas as pd
df = pd.DataFrame({    'Object Type': [77, 48, 23, 9, 7, 7, 4, 4, 3 ,3, 2, 1,1,1]},
                  index=['Prent/painting', 'Fotos/photos', 'Schetsboekblad/sketch', 
 'Tekening/drawing', 'Stereofoto', 'interieuronderdeel', 'Schilderij', 
'Bouwfragment', 'Fotomechanische afdruk', 'raamkozijn', 'kabinetfoto', 
'bord(vaatwerk)', 'balkon', 'affiche'])
plot = df.plot.pie(y='Object Type', figsize=(25,21), colors = ['gold', 'peachpuff', 'darkorange', 
          'burlywood', 'palegoldenrod', 'tomato', 'wheat', 'lightsalmon','lightslategray',
                                                                
         'coral', 'khaki', 'cornflowerblue','aqua'], labeldistance=1.05, radius=1,textprops={'fontsize': 10}, autopct='%1.1f%%')
######
################
#######
#For the Keizergracht canal
import pandas as pd
df = pd.DataFrame({    'Object Type': [92, 35, 16, 13, 13, 7, 2, 1,1,1,1,1]},
                  index=['Prent/painting', 'Foto/photos',  
 'Tekening/drawing', 'Stereofoto', 'Schetsboekblad', 'Kabinetfoto', 'Fotomechanische afdruk', 'Opticaprent','Schilderij','Digitaal bestand','Tekstblad', 'Fotoalbum'])
plot = df.plot.pie(y='Object Type', figsize=(25,21), colors = ['gold', 'peachpuff', 'darkorange', 
          'burlywood', 'palegoldenrod', 'tomato', 'wheat', 'red','lightsalmon','aqua','lightslategray',
                                                                
         'blue', 'green', 'cornflowerblue',], labeldistance=1.05, radius=1,textprops={'fontsize': 10}, autopct='%1.1f%%')
######
#Statistics and numbers for overall collection
#Number of canal art objects in dataset and then number of photos of the canals
singel = 227
singel_fotos = 66
#Singel objects and photos
herengracht = 190
herengracht_fotos = 48
#Keizersgracht objects and photos
keizersgracht = 183
keizersgracht_fotos = 35
#Prinsengracht objects and photos
prinsengracht = 95 
prinsengracht_fotos = 17
#Total number of art objects in Rijks set
total = singel + herengracht + keizersgracht + prinsengracht
print (total)
#Total number of photos
total_fotos = singel_fotos + herengracht_fotos + keizersgracht_fotos + prinsengracht_fotos
print (total_fotos)
#Foto percentages by canal
singel_fotos_percent = 66/227 * 100
print (singel_percent)
herengracht_fotos = 48/190 * 100
print (herengracht_fotos)
keizersgracht_fotos_percent = 35/183 * 100
print (keizersgracht_fotos_percent)
prinsengracht_fotos_percent = 17/95 * 100
print(prinsengracht_fotos_percent)


# In[ ]:




######
df['items', 'Items_4'] = df['items','Items_4'].str.strip()

#####

df['items'] = df['items'].str.strip()

df.dropna(axis=0, subset=['Order'], inplace=True)
df['items'] = df['items'].astype('str')

df = df[~df['Items_4'].str.contains('NaN', 'None', na=False)]
display(df)


rijks_top = rijks.head()
rijks_top
#DropNaN
rijks.dropna()
rijks.drop(['objectInventoryNumber', 'objectImage',             
            'objectPersistentIdentifier'], axis = 1, inplace = True) 
rijks.reset_index(drop=True, inplace=True)

#  SOLUTION FOR FINDING A SPECIFIC STRING IN A SPECIFIC COLUMN / Don't forget NAN
singel2 =  rijks[rijks['objectTitle[1]'].str.contains('Singel', na=False)]
print(singel2.to_string())

#Counting how many instances of this canal show ups up in depictions of art is 227
singel2.dropna()
singel2['objectType[1]'].count()

#Another way of counting the amount of items, which is again 227 
singel2.info()

#The amount of artistic depictions of the Singel are 227...now let's filter for photo depictions of it

#Filtering for photos
singel2[singel2['objectType[1]'].str.contains("foto")==True]

#Filtering for photos
singel_3 = singel2[singel2['objectType[1]'].str.contains("foto")==True]

#Try not changing it to a list and SORT THE DATA FRAME!
type(singel_3)
singel4 = singel_3.sort_values(by='objectType[1]', ascending=False, na_position='first')
singel4.dropna()

#Display the entire dataframe
from IPython.display import display, HTML
display(HTML(singel4.to_html()))

#Display the filtered dataframe for PHOTOS only
singel_df_filtered = singel4[singel4['objectType[1]'] == 'foto']

from IPython.display import display, HTML
display(HTML(singel_df_filtered.to_html()))

#The amount of photos of the Singel canal are 66
singel_df_filtered.count()

#So the amount of original art depictions are 227 and the photo depictions are 66
singel_df_filtered.info()

#SINGEL - Original art depictions = 227
#SINGEL - Photo depictions = 66

#1/4 canals done

 

