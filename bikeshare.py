#Python LIBRARIES
import time
import pandas as pd
import numpy as np

#Seting usefull dictionnary and arrays
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
ACEPTABLE_MONTH_OPTIONS = "january february march april may june all"
ACEPTABLE_DAY_OPTIONS = "monday, tuesday, wednesday, thursday, friday, saturday, sunday, all"

#Definition of functions to interact with program's users
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

    while True:
        city = input("Enter the name of the city to analyze: ").lower()
        if CITY_DATA.get(city) is not None:
            break
        print ("¡¡ERROR!! Not a valid input, try: chicago, new york city or washington")

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('name of the month to filter by, or "all" to apply no month filter: ').lower()
        if ACEPTABLE_MONTH_OPTIONS.find(month) >=0:
            break
        print ('¡¡ERROR!! Not a valid input, try: january, february, march, april, may, june or "all" to apply no month filter')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('name of the day of week to filter by, or "all" to apply no day filter: ').lower()

        if ACEPTABLE_DAY_OPTIONS.find(day) >=0:
            break
        print ('¡¡ERROR!! Not a valid input, try: monday, tuesday, wednesday, thursday, friday, saturday, sunday or "all" to apply no weekday filter')


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[df['month'].mode()[0]-1]
    print("Most popular month: {}".format(popular_month.title()))

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("Most popular day of the week: {}".format(popular_day_of_week))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most popular hour: {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most popular used start station: {}".format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most popular used end station: {}".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination']='"'+df['Start Station']+'" & "'+ df['End Station']+'"'
    popular_combination = df['Combination'].mode()[0]
    print("Most popular combination of stations: {}".format(popular_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("total travel time: {}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("mean travel time: {}".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earlies year of birth: {}".format(df['Birth Year'].min()))
        print("Most recent year of birth: {}".format(df['Birth Year'].max()))
        print("Most common year of birth: {}".format(df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Begining of main code

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        row = 0
        while True:
            viewData = input("Would you like to see the raw data? Type 'Yes' or 'No'.")
            if viewData.title() == "Yes":
                print(df.iloc[row:row+5])
                row += 5
            elif viewData.title() =="No":
                break
            else:
                print("¡¡ERROR!! Invalid input, try; 'Yes' or 'No'")

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
