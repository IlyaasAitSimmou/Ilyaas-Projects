from tkinter import * # Import all classes and functions from tkinter for GUI
from tkinter import messagebox # Import messagebox from tkinter for displaying message boxes
from datetime import * # Import all classes and functions from datetime for date and time manipulation
from meteostat import *  # Import all classes and functions from meteostat for weather data
from geopy import * # Import all classes and functions from geopy for geocoding
from pytz import timezone # Import timezone from pytz for timezone handling
from suntime import Sun # Import timezone from pytz for timezone handling
from timezonefinder import TimezoneFinder # Import Sun from suntime for sunrise and sunset calculations

# Create the main window for the application
window = Tk()
window.title("Climixa Weather App")  # Set the title of the window to "Climixa Weather App"
window.geometry("1000x836")  # Set the size of the window to 1000x836 pixels
window.configure(bg="#2c3e50")  # Set the background color of the window to a dark blue shade

# Placeholder for the weather condition image
weather_cond_img = PhotoImage()

# Create a frame for user input with a dark gray background, padding, and specific width
input_frame = Frame(window, bg="#34495e", padx=50, pady=20, width=1500)
input_frame.grid(sticky="W")  # Place the input frame in the window, aligned to the west (left)

# Create a frame for displaying the main data with a dark blue background, padding, and specific width
main_data_frame = Frame(window, bg="#2c3e50", padx=50, pady=20, width=1500)
main_data_frame.grid(row=1)  # Place the main data frame in the window, in the second row

# Create a frame for displaying weather information with a dark gray background, padding, and specific width
weather_frame = Frame(window, bg="#34495e", padx=50, pady=20, width=1500)
weather_frame.grid(row=2)  # Place the weather frame in the window, in the third row

# Dictionary to store the last day of each month (non-leap year)
months_last_day = {
    1: 31,  # January
    2: 28,  # February (non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Get the current date and time
Cur_year = int(datetime.now().strftime("%Y"))  # Get the current year as an integer
Cur_month = int(datetime.now().strftime("%m"))  # Get the current month as an integer
Cur_day = int(datetime.now().strftime("%d"))  # Get the current day as an integer
Cur_hour = int(datetime.now().strftime("%H"))  # Get the current hour as an integer
Cur_minute = int(datetime.now().strftime("%M"))  # Get the current minute as an integer

# Function to update the maximum day in the day spinbox based on the selected month
def changedaymax():
    # Update the 'to' parameter of the Day spinbox to the last day of the selected month
    Day.configure(to=months_last_day[int(Month.get().replace("M", ""))])

# Create and place the location label and entry field
location_label = Label(input_frame, text="Location:", font=("Arial", 15), bg="#34495e", fg="white")
location_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")  # Place the label in the first row, first column
Location = Entry(input_frame, width=15, font=("Arial Bold", 15), bg="white", fg="black", borderwidth=5)
Location.insert(0, "location")  # Set the default text in the entry field to "location"
Location.grid(row=0, column=1, padx=10, pady=10)  # Place the entry field in the first row, second column

# Create and place the year label and spinbox
year_label = Label(input_frame, text="Year:", font=("Arial", 15), bg="#34495e", fg="white")
year_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")  # Place the label in the second row, first column
Year = Spinbox(input_frame, from_=1990, to=Cur_year, font=("Arial", 15), bg="white", fg="black", borderwidth=2)
Year.grid(row=1, column=1, padx=10, pady=10) # Place the spinbox in the second row, second column

# Create and place the month label and spinbox
month_label = Label(input_frame, text="Month:", font=("Arial", 15), bg="#34495e", fg="white")
month_label.grid(row=1, column=2, padx=10, pady=10, sticky="e") # Place the label in the second row, third column
Month = Spinbox(input_frame, from_=1, to=12, font=("Arial", 15), bg="white", fg="black", borderwidth=2, command=changedaymax)
Month.insert(0, "M")
Month.grid(row=1, column=3, padx=10, pady=10) # Place the spinbox in the second row, fourth column

# Create and place the day label and spinbox
day_label = Label(input_frame, text="Day:", font=("Arial", 15), bg="#34495e", fg="white")
day_label.grid(row=0, column=2, padx=10, pady=10, sticky="e") # Place the label in the second row, fifth column
Day = Spinbox(input_frame, from_=1, to=31, font=("Arial", 15), bg="white", fg="black", borderwidth=2)
Day.insert(0, "D")
Day.grid(row=0, column=3, padx=10, pady=10) # Place the spinbox in the second row, sixth column

# Initialize Nominatim API with a user agent "GetLoc"
loc = Nominatim(user_agent="GetLoc")

# Get the location information for Brampton
getLoc = loc.geocode("Brampton")

# Create an instance of Stations to find nearby weather stations
stations = Stations()
stations = stations.nearby(getLoc.latitude, getLoc.longitude) # Find weather stations near the latitude and longitude of Brampton
station = stations.fetch(1) # Fetch data for the nearest weather station

# Define the start and end date/time for weather data retrieval
start = datetime(Cur_year, Cur_month, Cur_day)
end = datetime(Cur_year, Cur_month, Cur_day, Cur_hour, Cur_minute)

# Create a label for current temperature with text saying "Cur_Temp" and specified font, background, and foreground color
temp_txt = Label(main_data_frame, text="Cur Temp:", font=("Arial", 20), bg="#34495e", fg="white")
temp_txt.grid(row=1, column=0, pady = 20)

# Create a label to display the main temperature
main_temp = Label(main_data_frame)
main_temp.grid(row=1, column=1, pady = 20, padx=(10, 30))

# Create a label for wind information (with text saying "Wind")
Wind_txt = Label(weather_frame, text="Wind", font=("Arial", 20), bg="#34495e", fg="white")
Wind_txt.grid(row=0, column=0, padx = (0, 35))

# Create a label to display wind direction
Wind_dir = Label(weather_frame, font=("Arial", 10), bg="#34495e", fg="white")
Wind_dir.grid(row=1, column=0, padx = (0, 35))

# Create a label to display wind speed
Wind_spd = Label(weather_frame, font=("Arial", 10), bg="#34495e", fg="white")
Wind_spd.grid(row=2, column=0, padx = (0, 35))

# Create a label for wind gust information (with the text "Wind Gust")
WindG_txt = Label(weather_frame, text="Wind Gust", font=("Arial", 20), bg="#34495e", fg="white")
WindG_txt.grid(row=0, column=1)

# Create a label to display wind gust speed
WindG_spd = Label(weather_frame, font=("Arial", 10), bg="#34495e", fg="white")
WindG_spd.grid(row=1, column=1)

# Create a label to indicate pressure information
Pressure_txt = Label(weather_frame, text="Pressure", font=("Arial", 20), bg="#34495e", fg="white")
Pressure_txt.grid(row=0, column=2, padx = 35)

# Create a label to display pressure
Pressure_val = Label(weather_frame, font=("Arial", 10), bg="#34495e", fg="white")
Pressure_val.grid(row=1, column=2, padx = 35)

# Create a label for weather forecast
forecast = Label(main_data_frame, font=("Arial", 20), bg="#34495e", fg="white")
forecast.grid(row=1, column=2, pady = 30)

# Create a label to display a weather condition icon or image
weather_cond_icon = Label(main_data_frame)
weather_cond_icon.grid(row=1, column=3)

# Create a label to indicate humidity information
Humidity_txt = Label(weather_frame, text="Humidity", font=("Arial", 20), bg="#34495e", fg="white")
Humidity_txt.grid(row=0, column=3)

# Create a label to display humidity percentage
Humidity_Perc = Label(weather_frame, font=("Arial", 10), bg="#34495e", fg="white")
Humidity_Perc.grid(row=1, column=3)

# Create a label to indicate precipitation information
Percip_txt = Label(weather_frame, text="Percipitation", font=("Arial", 20), bg="#34495e", fg="white")
Percip_txt.grid(row=0, column=4, padx = 35)

# Create a label to display precipitation in mm
Percip_val = Label(weather_frame, font=("Arial", 10), bg="#34495e", fg="white")
Percip_val.grid(row=1, column=4, padx = 35)

# Create a label to indicate temperature information
DayTemp_txt = Label(weather_frame, text="Temp", font=("Arial", 20), bg="#34495e", fg="white")
DayTemp_txt.grid(row=0, column=5)

# Create labels to display average temperature, maximum temperature, and minimum temperature
Avg_temp = Label(weather_frame, font=("Arial", 10), bg="#34495e", fg="white")
Avg_temp.grid(row=1, column=5)
Max_temp = Label(weather_frame, font=("Arial", 10), bg="#34495e", fg="white")
Max_temp.grid(row=2, column=5)
Min_temp = Label(weather_frame, font=("Arial", 10), bg="#34495e", fg="white")
Min_temp.grid(row=3, column=5, pady=(0, 40))

"""
The convert_forecast function takes two arguments: a forecast_code representing the forecasted weather condition, and a time_of_day string indicating whether it is "day" or "night" at the location.
The function returns an array containing a weather forecast description and the filename of an icon representing the weather condition. 
It determines the weather condition based on the forecast_code number. 
The icon selection varies depending on whether it is day or night.
"""

def convert_forecast(Forecast, DorN):
  if int(Forecast) == 1:
    return ["Clear", f"clear_{DorN}.png"]
  elif int(Forecast) == 2:
    return ["Partly Cloudy", f"partly_cloudy_{DorN}.png"]
  elif int(Forecast) == 3:
    return ["Cloudy", f"cloudy_{DorN}.png"]
  elif int(Forecast) == 4:
    return ["Overcast", "overcast.png"]
  elif int(Forecast) == 5:
    return ["Fog", f"foggy_{DorN}.png"]
  elif int(Forecast) == 6:
    return ["Freezing Fog", "freezing_fog.png"]
  elif int(Forecast) == 7:
    return ["Light Rain", f"light_rain_{DorN}.png"]
  elif int(Forecast) == 8:
    return ["Rain", f"rain_{DorN}.png"]
  elif int(Forecast) == 9:
    return ["Heavy Rain", "heavy_rain.png"]
  elif int(Forecast) == 10:
    return ["Freezing Rain", "freezing_rain.png"]
  elif int(Forecast) == 11:
    return ["Heavy Freezing Rain", "freezing_rain.png"]
  elif int(Forecast) == 12:
    return ["Sleet", "sleet.png"]
  elif int(Forecast) == 13:
    return ["Heavy Sleet", "heavy_sleet.png"]
  elif int(Forecast) == 14:
    return ["Light Snowfall", f"light_snow_{DorN}.png"]
  elif int(Forecast) == 15:
    return ["Snowfall", "snow.png"]
  elif int(Forecast) == 16:
    return ["Heavy Snowfall", "heavy_snow.png"]
  elif int(Forecast) == 17:
    return ["Rain Shower", "rain_shower.png"]
  elif int(Forecast) == 18:
    return ["Heavy Rain Shower", "rain_shower.png"]
  elif int(Forecast) == 19:
    return ["Sleet Shower", "heavy_sleet.png"]
  elif int(Forecast) == 20:
    return ["Heavy Sleet Shower", "heavy_sleet.png"]
  elif int(Forecast) == 21:
    return ["Snow Shower", "heavy_snow.png"]
  elif int(Forecast) == 22:
    return ["Heavy Snow Shower", "heavy_snow.png"]
  elif int(Forecast) == 23:
    return ["Lightning", "lightning.png"]
  elif int(Forecast) == 24:
    return ["Hail", f"hail_{DorN}.png"]
  elif int(Forecast) == 25:
    return ["Thunderstorm", "thunderstorm.png"]
  elif int(Forecast) == 26:
    return ["Heavy Thunderstorm", "thunderstorm.png"]
  elif int(Forecast) == 27:
    return ["Storm", "storm.png"]

# Function to get the weather data and update the GUI

def Get_weather(location="Brampton", Year=Cur_year, Month=Cur_month, Day=Cur_day):
  
  # Initialize a flag to check if the date is the current date
  date_is_current = False

  # Check if the provided date is the current date
  if Year==Cur_year and Month==Cur_month and Day==Cur_day:
    date_is_current = True

  # Initialize Nominatim API to get location data
  loc = Nominatim(user_agent="GetLoc")

  # Get the geographic coordinates of the specified location
  getLoc = loc.geocode(location)

  # Fetch nearby weather stations for the given location using its latitude and longitude
  stations = Stations()
  stations = stations.nearby(getLoc.latitude, getLoc.longitude)
  station = stations.fetch(1)

  # Find the timezone of the location
  obj = TimezoneFinder() # Creates an instance (a single occurance) of a class (obj will be this object)
  tz2 = obj.timezone_at(lng=getLoc.longitude, lat=getLoc.latitude) # Assign tz2 the timezone of the location using obj which is an instance of the TimezoneFinder() class
  Loctimezone = timezone(tz2)

  # Get the sunrise and sunset times for the location using its longitude and latitude
  sun = Sun(getLoc.latitude, getLoc.longitude)
  sr = sun.get_sunrise_time()
  ss = sun.get_sunset_time()

  # Convert sunrise and sunset times to the local timezone of the location
  sr = sr.astimezone(Loctimezone)
  ss = ss.astimezone(Loctimezone)

  # Extract the hour and minute values for sunrise and sunset
  srValues = str(sr).split(" ")[1].split(":") # Turns datetime type into string and then into a list with two indices.
  # The second index which includes the time of day, is taken and split into a list containing hours, minutes, and seconds.
  srHour = int(srValues[0]) # Sunrise hour assigned
  srMin = int(srValues[1]) # Sunrise minute assigned

  # Same process is completed again but with sunset
  ssValues = str(ss).split(" ")[1].split(":")
  ssHour = int(ssValues[0])
  ssMin = int(ssValues[1])

  # Define the start and end date/time for fetching weather data
  start = datetime(Year, Month, Day)
  if date_is_current:
    end = datetime(Year, Month, Day, Cur_hour, Cur_minute)
  else:
    end = datetime(Year, Month, Day, 23, 59)

  # Fetch hourly weather data for the specified station and date range
  data = Hourly(station, start, end)
  data = data.fetch().reset_index().transpose()

  # daily data
  data2 = Daily(station, start, end)
  data2 = data2.fetch().reset_index().transpose()

  # Initialize lists to store various weather parameters (not all of them were used)
  Times = []
  allTemps = []
  allDewPoints = []
  allRelHumid = []
  allPercip = []
  allSnow = []
  allWindDir = []
  allWindSpd = []
  allPkWindGust = []
  allAvgPresure = []
  coco = []

  # Populate the lists with the fetched hourly weather data
  # Meteostat provides dataframes containing the wether data. .iat method is used to access specific cells.
  # The for loop iterates through the columns of the dataframe. .append() method adds values to the lists in each iteration.
  for i in range(data.shape[1]):
    Times.append(data.iat[0, i])
    allTemps.append(data.iat[1, i])
    allDewPoints.append(data.iat[2, i])
    allRelHumid.append(data.iat[3, i])
    allPercip.append(data.iat[4, i])
    allSnow.append(data.iat[5, i])
    allWindDir.append(data.iat[6, i])
    allWindSpd.append(data.iat[7, i])
    allPkWindGust.append(data.iat[8, i])
    allAvgPresure.append(data.iat[9, i])
    coco.append(data.iat[11, i])

  # Extract daily weather summary values
  # Dataframe with single column is returned for daily data. Its cells are accessed again with iat
  DTemps = data2.iat[0, 0]
  tempAvg = data2.iat[1, 0]
  tempMin = data2.iat[2, 0]
  tempMax = data2.iat[3, 0]
  Dpercip = data2.iat[4, 0]
  DSnow = data2.iat[5, 0]
  DWindDir = data2.iat[6, 0]
  DWindSpd = data2.iat[7, 0]
  DPkWindGust = data2.iat[8, 0]
  DAvgPresure = data2.iat[9, 0]
  DTotSunShine = data2.iat[10, 0]
  forecastInfo = []

  # Update the GUI with current or average weather data based on the date
  # The different lables mentioned earlier are configured with the current temperature if the date is current. f strings are used to format the data into the text. The data.shape[1] - 1 is used as the index of each list because it is the index of the last (and latest) element of each list
  if date_is_current:
    temp_txt.configure(text="Cur Temp: ")
    main_temp.configure(text=f"{allTemps[data.shape[1] - 1]}˚C", font=("Arial", 30), bg="#34495e", fg="white")

    Wind_dir.configure(text=f"{allWindDir[data.shape[1] - 1]}˚N")
    Wind_spd.configure(text=f"{allWindSpd[data.shape[1] - 1]} km/h")

    WindG_spd.configure(text=f"{allPkWindGust[data.shape[1] - 1]} km/h")

    Pressure_val.configure(text=f"{int(allAvgPresure[data.shape[1] - 1])/10} kPa")

    # Determine if it is day or night and get the appropriate forecast information using sunrise and sunset times and the current time of day
    if (srHour <= Cur_hour < ssHour) or (Cur_hour == srHour and Cur_minute >= srMin) or (Cur_hour == ssHour and Cur_minute < ssMin):

      # if it is day is entered, it is formatted into the strings for the files and a daytime icon is returned in the two element list
      forecastInfo = convert_forecast(coco[data.shape[1] - 1], "day")      
      # Similarly if it is night, nighttime icons are used
    else:
      forecastInfo = convert_forecast(coco[data.shape[1] - 1], "night")
      # If the weather isn't current, the average temperature, pressure, wind direction, wind speed, and wind gust speed are displayed. The last forecast during the day is displayed along with a day icon
  else:
    temp_txt.configure(text="Avg Temp: ")
    main_temp.configure(text=f"{tempAvg}˚C", font=("Arial", 30), bg="#34495e", fg="white")

    Wind_dir.configure(text=f"Dir: {DWindDir}˚N")
    Wind_spd.configure(text=f"Spd: {DWindSpd} km/h")
    WindG_spd.configure(text=f"Gust Spd: {DPkWindGust} km/h")
    
    Pressure_val.configure(text=f"{DAvgPresure/10} kPa")
    
    forecastInfo = convert_forecast(coco[data.shape[1] - 1], "day")   

  # forecast and weather condition icon labels are now configured
  forecast.configure(text=f"{forecastInfo[0]}")
  weather_cond_img.configure(file = "images/"+forecastInfo[1])
  weather_cond_icon.configure(image=weather_cond_img, bg="#2c3e50")

  # Labels for other weather aspects that aren't affected by the type of date are configured
  Humidity_Perc.configure(text=f"{int(allRelHumid[data.shape[1] - 1])}%")

  Percip_val.configure(text=f"{Dpercip} mm")

  Avg_temp.configure(text=f"Avg: {tempAvg}˚C")
  Max_temp.configure(text=f"Max: {tempMax}˚C")
  Min_temp.configure(text=f"Min: {tempMin}˚C")
    

def submit():
  # Get the geographical location based on the user input
  getLoc = loc.geocode(Location.get()) # Takes location from Location entry box using .get() method

  
  try:
    # Extract the year, month, and day from the user input and convert them to integers
    year = int(Year.get())
    month = int(Month.get())
    day = int(Day.get())

    # Create datetime objects for the start and end of the specified day
    start = datetime(year, month, day)
    end = datetime(year, month, day, 23, 59)
  except:
    # If there's an error in the date conversion, configure the header to display the current weather
    # If there is an error, the date entered is unavailable
    header.configure(text=f"Current weather at {Location.get()}")
  try:
    # Check if the month or day inputs contain non-numeric characters
    if "M" in Month.get() or "D" in Day.get():   
      # Try to display the weather at the entered location at the current time
      try:
        messagebox.showinfo("Error", "No date has been entered. Current weather is displayed instead.")
        test = loc.geocode(Location.get()) # If the location is valid, no errors will occur
        Get_weather(location = Location.get(), Year = Cur_year, Month = Cur_month, Day = Cur_day)
      except AttributeError:
        # Other wise an exception error will be raised. Now the current weather at Brampton is displayed.
        messagebox.showinfo("Error", "Location and date are invalid. Current weather at Brampton is displayed instead.")
        Get_weather()
        Location.insert(0, "Brampton")
    else:
      try:
        test = loc.geocode(Location.get())
        # print(test) # This is a test line to test the geocode() function.
        
        # Get the weather for the specified location and date
        Get_weather(location = Location.get(), Year = year, Month = month, Day = day)

      # Again, if the location is invalid, show an error message and display weather for the default location (Brampton)
      except AttributeError:
        messagebox.showinfo("Error", "A valid location has not been entered. Weather at Brampton is displayed instead.")
        Location.insert(0, "Brampton")
        Get_weather(Year = Cur_year, Month = Cur_month, Day = Cur_day)
        
      if year == Cur_year and month == Cur_month and day == Cur_day:
        header.configure(text=f"Current weather at {Location.get()}")
      else:
        header.configure(text=f"Weather at {Location.get()} on {day}/{month}/{year}")
  
  # If the date is unavailable based display the current weather at the location
  except:
    Get_weather(location = Location.get(), Year = Cur_year, Month = Cur_month, Day = Cur_day)
    header.configure(text=f"Current weather at {Location.get()}")
    messagebox.showinfo("Error", "Date is unavailable.")
    pass

# Enter button to submit location and date information to aqcuire weather. Button calls submit function when clicked.
Enter = Button(input_frame, font=("Arial Bold", 15), bg="#2980b9", fg="white", borderwidth=5, text="Enter", command=submit)
Enter.grid(row=3, column=0, columnspan=6, pady=20)

# Header that displays a text describing what information is shown
header = Label(input_frame, text="Current weather at Brampton", font=("Arial Bold", 25))
header.grid(row=4, column=0, columnspan=6, pady=20)

# By default, display current weather at Brampton
Get_weather()

# Loop to run window
window.mainloop()
