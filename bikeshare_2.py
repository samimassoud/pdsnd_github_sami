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
    cities = ['chicago','new york city', 'washington']
    months = ['all','january','february','march','april','may','june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    time_filters = ['month', 'day', 'both', 'none']
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city in cities:
            choice = input("It looks like you have entered " + city.title() +". If you want to cancel enter 'n'\nIf you wish to proceed press any key\n").lower()
            if(choice =='n'):
                continue
            else:
                break
        else:
            print("Invalid input. Please choose one of the current options: Chicago, New York City, or Washington.")
    while True:
        time_filter = input ("Would you like to filter the data by month, day, both, or not at all? Type \"none\" for no time filter.\n").lower()
        if time_filter in time_filters:
            choice = input("It looks like you have entered " + time_filter.title() +". If you want to cancel enter 'n'\nIf you wish to proceed press any key\n").lower()
            if(choice =='n'):
                continue
            else:
                break
        else:
            print("Please choose one of the available time filter's options")
    if(time_filter=="both"):
        # get user input for month (all, january, february, ... , june)
        while True:
            month = input("Which month? January, February, March, April, May, June or All?\n").lower()
            if month in months:
                choice = input("It looks like you have entered " + month.title() +". If you want to cancel enter 'n'\nIf you wish to proceed press any key\n").lower()
                if(choice =='n'):
                    continue
                else:
                    break
            else:
                print("Invalid input. Please choose one of the available month's options")

        # get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All?\n").lower()
            if day in days:
                choice = input("It looks like you have entered " + day.title() +". If you want to cancel enter 'n'\nIf you wish to proceed press any key\n").lower()
                if(choice =='n'):
                    continue
                else:
                    break
            else:
                print("Invalid input. Please choose one of the available day's options.")
    elif(time_filter=="month"):
        day="all"
        while True:
            month = input("Which month? January, February, March, April, May, June or All?\n").lower()
            if month in months:
                choice = input("It looks like you have entered " + month.title() +". If you want to cancel enter 'n'\nIf you wish to proceed press any key\n").lower()
                if(choice =='n'):
                    continue
                else:
                    break
            else:
                print("Invalid input. Please choose one of the available month's options")
    elif(time_filter=="day"):
        month="all"
        while True:
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All?\n").lower()
            if day in days:
                choice = input("It looks like you have entered " + day.title() +". If you want to cancel enter 'n'\nIf you wish to proceed press any key\n").lower()
                if(choice =='n'):
                    continue
                else:
                    break
            else:
                print("Invalid input. Please choose one of the available day's options.")
    else:
        #none
        day="all"
        month="all"

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
    #Firstly, load data for chosen city
    df = pd.read_csv(CITY_DATA[city])

    #Then we convert the Start Time column to datetime like in the practice problem
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract Month and day and hour as columns from the Start Time column
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    months = ['january','february','march','april','may','june']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    #Filter by month if it 'all' option wasn't chosen
    if month != "all":
        month_index = months.index(month) + 1 #so that 1 is Jan and so on, so that it is compatiable with .dt.month resulting column
        df = df[df['month'] == month_index]
        #Filtered by month
    if day != "all":
        df = df[df['day'] == day.title()] # .title() so that it is compatiable with .dt.day_name() resulting column
    #Didn't use elif, because there is 'both' option, meaning that
    #  one being filtered doesn't necessarily means that the other isn't.
    #If 'none' was chosen then it would skip the filtering, meaning that
    #  it will give me the right 'df' that I'm after.

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    months = ['january','february','march','april','may','june']

    print('\nCalculating The Most Frequent Times of Travel...\n')
    print('\n')
    total_start_time=time.time()
    # display the most common month
    print('Calculating The Most Common Month...\n')
    start_time = time.time()
    common_month_index = df['month'].mode()[0]
    print("Most Common Month: ", months[common_month_index-1].title())
    print("\nThis took %s seconds." %(time.time()- start_time))
    print('\n-'*40)


    # display the most common day of week
    print('Calculating The Most Common Day of The Week...\n')
    start_time = time.time()
    common_day = df['day'].mode()[0]
    print("Most Common Day of The Week: ", common_day )
    print("\nThis took %s seconds." %(time.time()- start_time))
    print('\n-'*40)

    # display the most common start hour
    print('Calculating The Most Common Start Hour...\n')
    start_time = time.time()
    common_hour = df['hour'].mode()[0]
    print("Most Common Start Hour: ", common_hour)
    print("\nThis took %s seconds." %(time.time()- start_time))
    print('\n-'*40)

    print("\nAll statistics took %s seconds." % (time.time() - total_start_time))
    print('\n-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    total_start_time = time.time()
    # display most commonly used start station
    print("Calculating The Most Commonly Used Start Station...\n")
    start_time = time.time()
    common_start_station = df['Start Station'].mode()[0]
    print("Most Commonly Used Start Station: ", common_start_station)
    print("\nThis took %s seconds." %(time.time()- start_time))
    print('\n-'*40)

    # display most commonly used end station
    print("Calculating The Most Commonly Used End Station...\n")
    start_time = time.time()
    common_end_station = df['End Station'].mode()[0]
    print("Most Commonly Used End Station: ", common_end_station)
    print("\nThis took %s seconds." %(time.time()- start_time))
    print('\n-'*40)
    # display most frequent combination of start station and end station trip
    print("Calculating The Most Frequent Trip...\n")
    start_time = time.time()
    df['Trip'] = "From " + df['Start Station'] + " to " + df['End Station']
    common_trip = df["Trip"].mode()[0]
    print("Most Frequent Trip (Start - End): ", common_trip)
    print("\nThis took %s seconds." %(time.time()- start_time))
    print('\n-'*40)


    print("\nAll statistics took %s seconds." % (time.time() - total_start_time))
    print('\n-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    total_start_time = time.time()

    # display total travel time
    print("Calculating The Total Travel Time...\n")
    start_time = time.time()
    total_travel_time = df['Trip Duration'].sum()
    hours = total_travel_time // 3600
    minutes = (total_travel_time % 3600) // 60
    seconds = (total_travel_time % 3600) % 60
    print("Total Travel Time:\n")
    print(f"{total_travel_time} Seconds")
    print(f"{total_travel_time / 60:.2f} Minutes")
    print(f"{hours} Hours: {minutes} Minutes: {seconds} Seconds\n")
    print("\nThis took %s seconds." %(time.time()- start_time))
    print('\n-'*40)

    # display mean travel time
    print("Calculating The Mean Travel Time...\n")
    start_time = time.time()
    print("Mean Travel Time:\n", df['Trip Duration'].mean(), " seconds")
    print("\nThis took %s seconds." %(time.time()- start_time))
    print('\n-'*40)

    print("\nAll statistics took %s seconds " % (time.time() - total_start_time))
    print('\n-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    total_start_time = time.time()

    # Display counts of user types
    print("Calculating The Count Of User Types...\n")
    start_time = time.time()
    print("User Types Counts:\n", df['User Type'].value_counts())
    print("\nThis took %s seconds." %(time.time()- start_time))
    print('\n-'*40)
    

    # Display counts of gender
    if 'Gender' in df.columns:
        print("Calculating The Count Of Gender...\n")
        start_time = time.time()
        print("Gender Counts:\n", df['Gender'].value_counts())
        print("\nThis took %s seconds." %(time.time()- start_time))
        print('\n-'*40)
    else:
        print("Gender is Not Regarded in The Washington CSV File")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("The Earliest Year of Birth: ", earliest_year_of_birth)
        print("The Most Recent Year of Birth: ", most_recent_year_of_birth)
        print("The Most Common Year of Birth: ", most_common_year_of_birth)
    else:
        print("Birth Date is Not Regarded in The Washington CSV File")


    print("\nAll The Statistics took %s seconds." % (time.time() - total_start_time))
    print('\n-'*40)

def preview_data(df):
    """Displays raw data of the filtered bikeshare users, upon request"""
    view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no\n").lower()
    start_loc = 0
    if(view_data == "yes"):
        while (True):
            print(df.iloc[start_loc:(start_loc+5)])
            start_loc+=5
            view_data = input("Do you wish to continue?:\nPress 'Enter' to continue\n Enter no to stop\n").lower()
            if(view_data =="no"):
                break
            else:
                continue



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        preview_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
