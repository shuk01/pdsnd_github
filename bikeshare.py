import time
import pandas as pd
import numpy as np

# CITY_DATA provided by Udacity course on python. There is additional data on users for both Chicago and New York City.

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
    print('Hello! Let\'s explore some US bikeshare data!\nFirst, let\'s set some parameters by which we will filter the data with. All data displayed will depend on these parameters')

    # Get user input for city (chicago, new york city, washington)
    city = str(input('Type in chicago, new york city, or washington: ').lower().strip())
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        print('Not a valid city. Please try again')
        city = str(input('Type in the city of your interest, chicago, new york city, or washington:').lower().strip())

    # Get user input for month (all, january, february, ... , june)
    month = str(input('Type in the month you want to filter by, from january to june, or all: ').lower().strip())
    while month != 'all' and month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june':
        print('Not a valid month. Please try again')
        month = str(input('Type in the month you want to filter by, from january to june, or all: ').lower().strip())

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input('Type in the day you want to filter by, from monday to sunday, or all: ').lower().strip())
    while day != 'all' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday':
        print('Not a valid day. Please try again')
        day = str(input('Type in the day you want to filter by, from monday to sunday, or all: ').lower().strip())

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

    # Set df
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to datetime format, then create 'month' column and 'day_of_week' column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Change df based on filters. Filters are from user inputs in the the get_filters() function
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        if day != 'all':
            df = df[df['day_of_week'] == day.title()]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Set most_common_month to the most common month from the 'month' column, using the mode function
    most_common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_common_month = months[most_common_month - 1]


    # Set most_common_day to the most common day in the 'day_of_week' column, using the mode function
    most_common_day = df['day_of_week'].mode()[0]

    # Set most_common_hour to the most common hour in the 'hour' column, using the mode function
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]

    # Display the most common month, the most common day, and the most common start hour
    print('\nBased on the parameters given:\n\nThe most common month - {}\nThe most common day - {}\nThe most common start hour - {}'.format(most_common_month, most_common_day, most_common_hour))

    # Promt user for additional display of most common month data
    show_data = input('\nWould you like to see raw data for most common months? y/n: ').lower().strip()
    if show_data == 'y':
        print('\nDisplaying months and frequencies:')
        for i in range(0, len(df['month'].value_counts()), 5):
            print('\n', df['month'].value_counts()[i:(i+5)])
            if (len(df['month'].value_counts()) - 4) < i:
                print('\nEnd of data reached! Moving to next set...')
                break
            show_more = input('Do you want to see more of this data? y/n: ').lower()
            if show_more != 'y':
                break

    # Promt user for additional display of most common day data
    show_data = input('\nWould you like to see raw data for most common day? y/n: ').lower().strip()
    if show_data == 'y':
        print('\nDisplaying days and frequencies:')
        for i in range(0, len(df['day_of_week'].value_counts()), 5):
            print('\n', df['day_of_week'].value_counts()[i:(i+5)])
            if (len(df['day_of_week'].value_counts()) - 4) < i:
                print('\nEnd of data reached! Moving to next set...')
                break
            show_more = input('Do you want to see more of this data? y/n: ').lower()
            if show_more != 'y':
                break


    # Promt user for additional display of most common hour data
    show_data = input('\nWould you like to see raw data for most common start hour? y/n: ').lower().strip()
    if show_data == 'y':
        print('\nDisplaying start hours and frequencies:')
        for i in range(0, len(df['hour'].value_counts()), 5):
            print('\n', df['hour'].value_counts()[i:(i+5)])
            if (len(df['hour'].value_counts()) - 5) < i:
                print('\nEnd of data reached! Moving to next set...')
                break
            show_more = input('Do you want to see more of this data? y/n: ').lower()
            if show_more != 'y':
                break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Set most_common_start_st to the most common station in the 'Start Station' column, using the mode function
    most_common_start_st = df['Start Station'].mode()[0]

    # Set most_common_end_st to the most common station in the 'End Station' column, using the mode function
    most_common_end_st = df['End Station'].mode()[0]

    # Set most_common_combination to the most common station in the newly created 'Start End Station' column
    df['Start End Stations'] = df['Start Station'] + ' and ' + df ['End Station']
    most_common_combination = df['Start End Stations'].mode()[0]

    # Display the most common start station, end station, and start end combination stations
    print('\nBased on the parameters given:\n\nThe most common start station - {}\nThe most common end station - {}\nThe most common start and stop stations - {}'.format(most_common_start_st, most_common_end_st, most_common_combination))

    # Promt user for additional display of most common start station data
    show_data = input('\nWould you like to see raw data for most common start station? y/n: ').lower().strip()
    if show_data == 'y':
        print('\nDisplaying start stations and frequencies:')
        for i in range(0, len(df['Start Station'].value_counts()), 5):
            print('\n', df['Start Station'].value_counts()[i:(i+5)])
            if (len(df['Start Station'].value_counts()) - 5) < i:
                print('\nEnd of data reached! Moving to next set...')
                break
            show_more = input('Do you want to see more of this data? y/n: ').lower()
            if show_more != 'y':
                break

    # Promt user for additional display of most common end station data
    show_data = input('\nWould you like to see raw data for most common end station? y/n: ').lower().strip()
    if show_data == 'y':
        print('\nDisplaying end stations and frequencies:')
        for i in range(0, len(df['End Station'].value_counts()), 5):
            print('\n', df['End Station'].value_counts()[i:(i+5)])
            if (len(df['End Station'].value_counts()) - 5) < i:
                print('\nEnd of data reached! Moving to next set...')
                break
            show_more = input('Do you want to see more of this data? y/n: ').lower()
            if show_more != 'y':
                break

    # Promt user for additional display of most common combination of start and end station data
    show_data = input('\nWould you like to see raw data for most common combination of start and end station? y/n: ').lower().strip()
    if show_data == 'y':
        print('\nDisplaying start/end stations and frequencies:')
        for i in range(0, len(df['Start End Stations'].value_counts()), 5):
            print('\n', df['Start End Stations'].value_counts()[i:(i+5)])
            if (len(df['Start End Stations'].value_counts()) - 5) < i:
                print('\nEnd of data reached! Moving to next set...')
                break
            show_more = input('Do you want to see more of this data? y/n: ').lower()
            if show_more != 'y':
                break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Set total_travel_time_s to the sum of the 'Trip Duration' column, using the sum() function
    total_travel_time_s = int(df['Trip Duration'].sum())

    # Set mean_travel_time_s to the sum of the 'Trip Duration' column, using the mean() function
    mean_travel_time_s = int(df['Trip Duration'].mean())

    # Display the total travel time and mean travel time
    show_data = input('\nWould you like to see total travel time and mean travel time? y/n: ').lower().strip()
    if show_data == 'y':
        print('\nBased on the given parameters:\n\nTotal travel time is {} seconds'.format(total_travel_time_s))
        print('Mean travel time is {} seconds'.format(mean_travel_time_s))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    show_data = input('\nWould you like to see data of user types? y/n: ').lower().strip()
    if show_data == 'y':
        print('User types for the given parameters are as follows:\n', df['User Type'].value_counts())

    # Not all cities have the 'Gender' data, so display gender data using a 'try' condition
    show_data = input('\nWould you like to see data of user gender? y/n: ').lower().strip()
    if show_data == 'y':
        try:
            print('\nUser gender breakdown for given parameters are as follows:\n', df['Gender'].value_counts())
        except KeyError:
            print('\n\nUser gender data is unavailable for this city\n')


    # Not all cities have the 'Birth Year' data, so display earliest, most recent, and most common year of birth
    #  using a 'try' statement
    show_data = input('\nWould you like to see data of user birth year? y/n: ').lower().strip()
    if show_data == 'y':
        try:
            print('\nThe birth year data for users in the given parameters are as follows:\nEarliest birth year - ', int(df['Birth Year'].min()))
            print('Most recent birth year - ', int(df['Birth Year'].max()))
            print('Most common birth year - ', int(df['Birth Year'].value_counts().idxmax()))
        except:
            print('\nBirth year data is unavailable in this city\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Create function main() that uses other function if this is the main shell
def main():
    while True:
        city, month, day = get_filters()
        print('Parameters chosen are:\nCity - {}\nMonth - {}\nDay - {}\n'.format(city, month, day))
        df = load_data(city, month, day)

        time_stats(df)
        print('Moving to Station Stats')
        station_stats(df)
        print('Moving to trip duration stats')
        trip_duration_stats(df)
        print('Moving to user stats')
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thanks for using this bikeshare data explorer!')
            break

#
if __name__ == "__main__":
	main()
