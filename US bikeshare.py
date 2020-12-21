import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Which city would you like to view? please, choose from Chicago, New York city, Washington.\n").lower()
    while city not in(CITY_DATA.keys()):
        print("Invalid input. Please provide a correct city name..")
        city = input("Which city would you like to view? please, choose from Chicago, New York city, Washington.\n").lower()
   
    #get user input for filter type (month, day or both)
    filter = input("Would you like to filter the data by month, day, both, none?\n").lower()
    while filter not in (["month", "day", "both", "none"]):
        print("Invalid input. Please provide a valid input to proceed..")
        filter = input("Would you like to filter the data by month, day, both, none?\n").lower()
    
    
    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if filter == "month" or filter == "both":
        month = input("which month you need to view: January, February, March, April, May, June?\n").lower()
        while month not in months:
            print("Invalid input. Please provide a correct month name..")
            month = input("which month you need to view: January, February, March, April, May, June?\n").lower()
    else:
        month = "all"
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if filter == "day" or filter == "both":
        day = input("which day of week you need to view? Please type from(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday):\n").title()
        while day not in days:
            print("Invalid input. Please provide a correct day of week name..")
            day = input("which day of week you need to view? Please type from(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday):\n").title()
    else:
        day = "all" 
    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #load datafile into a dataframe
    
    df = pd.read_csv(CITY_DATA[city])
    
    #convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
                              
    #extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
                           
    #filter by month
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month)+1
                           
                           
    #filter by month to create new dataframe
        df = df[df["month"] == month]
                           
                           
    #filter by day of week
                           
    if day != "all":
        df = df[df["day_of_week"] == day.title()]
                           
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ["january", "february", "march", "april", "may", "june"]
    month = df["month"].mode()[0]
    print(f'The most common month is: {months[month-1]}')
                           

    # TO DO: display the most common day of week
    day = df["day_of_week"].mode()[0]
    print(f'The most common day of week is: {day}')

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    popular_hour = df["hour"].mode()[0]
    print(f'The most common Start Hour is: {popular_hour}')
               

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print(f"The most commonly used Start Station is: {popular_start_station}")

    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print(f"The most commonly used End Station is: {popular_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df["Start Station"]+ " to " +df["End Station"]
    print(f"The most popular trip is from {popular_trip.mode()[0]}")
                           

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    from datetime import timedelta as td
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = (pd.to_datetime(df["End Time"]) - pd.to_datetime(df["Start Time"])).sum()
    days = total_travel_time.days
    hours = total_travel_time.seconds // (60*60)
    minutes = total_travel_time.seconds % (60*60) // 60
    seconds = total_travel_time.seconds % (60*60) % 60
    print(f"The total travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds")

    # TO DO: display mean travel time
    average_travel_time = (pd.to_datetime(df["End Time"]) - pd.to_datetime(df["Start Time"])).mean()
    days = total_travel_time.days
    hours = total_travel_time.seconds // (60*60)
    minutes = total_travel_time.seconds % (60*60) // 60
    seconds = total_travel_time.seconds % (60*60) % 60
    print(f"The average total travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df["User Type"].value_counts())
    print("\n")

    # TO DO: Display counts of gender
    if "Gender" in (df.columns):
        print(df["Gender"].value_counts())
        print("\n")
                           

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth year" in (df.columns):
        year = df["Birth Year"].fillna(0).astype("int64")
        print(f'The earlist birth year is: {year.min()}\nthe most recent is: {year.max()}\nThe most common birth year is: {year.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def diplay_raw_data(df):
    """We can ask the user if he/she wants to show the raw data and print 5 raws at a time"""
    
    raw = input("\nWould you like to show raw data?\n")
    if raw.lower() == "yes":
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input("Next 5 raws?")
            if ask.lower() != "yes":
                break          
                                                                         
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
