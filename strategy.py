#import function
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

"""CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
TARGET_DIR_PATH = os.path.join(CURR_DIR_PATH + "")

subject_path = CURR_DIR_PATH + "/zip/"
all_subject_file_paths = glob(subject_path + "/weather.csv")"""

# read csv file and choose columns
data = pd.read_csv("weather.csv")
select = data[['city','date','temperature','pressure','humidity','weather_description']]
print(select)


#create a scatter plot by matplotlib
#use city's column and temperature's column
plt.scatter(select['city'], select['temperature'], color = 'blue')
plt.ylabel('temperature')
plt.xlabel('city')
plt.title("Temperature of cities on 30 april 2023 at 16.30")

plt.grid(True)
plt.show()


#create a scatter plot by matplotlib
#use pressure's column and temperature's column

plt.scatter(select['pressure'], select['temperature'], color = 'red')
plt.ylabel('temperature')
plt.xlabel('pressure')
plt.title("air pressure per temperature on 30 april 2023 at 16.30")

plt.text(1012,  10.72,'Stockholm')
plt.text(1021, 17.71,'London')
plt.text(1017, 23.73,'Madrid')
plt.text(1011, 19.55,'Rom')
plt.text(1014 , 23.42,'Cairo')

plt.grid(True)
plt.show()

#create a scatter plot by matplotlib
#use humidity's column and temperature's column


plt.scatter(select['humidity'], select['temperature'], color = 'green')
plt.ylabel('temperature')
plt.xlabel('humidity')
plt.title("humidity per temperature on 30 april 2023 at 16.30")

plt.text(37, 10.72,'Stockholm')
plt.text(51, 17.71,'London')
plt.text(36, 23.73,'Madrid')
plt.text(71, 19.55,'Rom')
plt.text(33, 23.42,'Cairo')

plt.grid(True)
plt.show()