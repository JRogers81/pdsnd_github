# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:37:16 2022

@author: Jason Rogers
"""

import time
import pandas as pd
from sys import exit

# Create a dictionary of cities and respective csv files
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# Create a list of applicable months
months = ['january', 'february', 'march', 'april', 'may', 'june']
# Create a list of the days of the week
day_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
# Create a list of possible exit commands
exit_commands = ['end', 'exit', 'quit', 'stop']
# Create a message for the exit command
exit_message = '\nSo sorry to see you go, but have a great day!\n'


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_test = 0
    while city_test < 1:
        city = str(input("\nWhat city would you like to explore: "))
        if city.lower() in CITY_DATA.keys():
            print('\nThanks for the city input')
            city_test += 1
        elif city.lower() in exit_commands:
            print(exit_message)
            exit()
        else:
            print('\nPlease enter one of the following cities: \n' + ', '.join([k.title() for k in CITY_DATA.keys()]))

    # TO DO: get user input for month (all, january, february, ... , june)
    month_test = 0
    while month_test < 1:
        month = str(input('\nWhat month would you like to review? (or enter "all") '))
        if month.lower() in months or month.lower() == 'all':
            print('\nThanks for the month input')
            month_test += 1
        elif month.lower() in exit_commands:
            print(exit_message)
            exit()
        else:
            print('\nPlease enter one of the following months: \n' + ', '.join([x.title() for x in months]))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_test = 0
    while day_test < 1:
        day = str(input('\nWhat day of week would you like to explore? (enter a day of week or enter "all") '))
        if day.lower() in day_of_week or day.lower() == 'all':
            print('\nThanks for the day input')
            day_test += 1
        elif day.lower() in exit_commands:
            print(exit_message)
            exit()
        else:
            print('\nPlease enter one of the following days of the week: \n' + ', '.join([y.title() for y in day_of_week]))
    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = df['Start Time'].astype('datetime64')

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        month_num = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month_num]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print('The most popular month is: {}.'.format(months[int(popular_month) - 1].title()))

    # display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print('The most popular day of the week is: {}.'.format(popular_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    if popular_hour >= 10:
        print('The most popular hour is: {}00.'.format(popular_hour))
    else:
        print('The most popular hour is: 0{}00.'.format(popular_hour))

    # Print the time it too to complete this function
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('The most popular start station is: {}.'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('The most popular end station is: {}.'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    df['start_end_station'] = 'starts at ' + df['Start Station'] + ' and ends at ' + df['End Station']
    popular_start_end_station = df['start_end_station'].value_counts().idxmax()
    print('The most popular route {}.'.format(popular_start_end_station))

    # Print the time it took to complete this function
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time is: {} minutes.'.format(int(sum(df['Trip Duration'])//60)))

    # display mean travel time
    print('The mean travel time is: {} minutes.'.format(int(df['Trip Duration'].mean()//60)))

    # Print the time it took to complete this function
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.columns:
        counts_user_types = df['User Type'].value_counts()
        print('The counts of user types are: ')
        for i in range(len(counts_user_types.index.values)):
            print(counts_user_types.index.values[i], ':', list(counts_user_types)[i])

    # Display counts of gender
    if 'Gender' in df.columns:
        counts_gender = df['Gender'].value_counts()
        print("\nThe counts_gender is:")
        for i in range(len(counts_gender.index.values)):
            print(counts_gender.index.values[i], ':', list(counts_gender)[i])

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nThe earliest year of birth is: {}.'.format(int(min(df['Birth Year']))))
        print('\nThe most recent year of birth is: {}.'.format(int(max(df['Birth Year']))))

        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nThe most common year of birth is: {}.'.format(int(most_common_year)))

    # Print the time it took to complete this function
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Ask if you want to see five rows of data?
        raw_data = input('\nWould you like to see the first five rows of data? Enter yes or no.\n').lower()
        record_count = 0
        while raw_data == 'yes':
            print(df.iloc[record_count:record_count+5])
            record_count += 5
            raw_data = input('\nWould you like to see five more rows of data? Enter yes or no.\n').lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print(exit_message)
            exit()


if __name__ == "__main__":
    main()
