import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months_dict = {'january':'january', 'february':'february', 'march':'march', 'april':'april','may':'may', 'june':'june'}
days_of_week = {'monday':'monday', 'tuesday':'tuesday', 'wednesday':'wednesday', 'thursday':'thursday', 'friday':'friday','saturday':'saturday', 'sunday':'sunday'}

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
    city_input=''
    while city_input.lower() not in CITY_DATA.keys():
        city_input=input('\nWhich city?NYC,Chicago or Washington DC.\n')
        if city_input.lower() not in CITY_DATA.keys():
            print('Sorry, I do not understand your input. Please type in a valid city')              
    city = CITY_DATA[city_input.lower()]       
    # TO DO: get user input for month (all, january, february, ... , june)
    month_input=''
    while month_input.lower() not in months_dict.keys():
        month_input=input('\nWhich month ?January,February,March,April,May or June?\n')
        if month_input.lower() not in months_dict.keys():
            print('Sorry, I do not understand your input. Please type in a '
                  'month between January and June')
    month = months_dict[month_input.lower()]        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_input=''
    while day_input.lower() not in days_of_week:
        day_input=input('Please input the day of week')
        if day_input.lower() not in days_of_week:
            print('Sorry I dont understand your input,please enter valid input')
    day=days_of_week[day_input.lower()]

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
    city,month,day=get_filters()
    print('Loading Data')
    df=pd.read_csv(city)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    index=int(df['start_time'].dt.month.mode())        
    common_month=months_dict[index-1]
    print('Most common month is {}'.format(common_month))          
    # TO DO: display the most common day of week
    Index=int(df['start_time'].dt.dayofweek.mode())
    common_day=days_of_week[Index]
    print('Most common day is {}'.format(common_day))            
 
    # TO DO: display the most common start hour
    most_common_hour=int(df['start_time'].dt.hour.mode()) 
    if most_common_hour == 0:
        am_pm = 'am'
        common_hour_readable = 12
    elif 1 <= most_common_hour < 13:
        am_pm = 'am'
        pop_common_readable = most_common_hour
    elif 13 <= most_common_hour < 24:
        am_pm = 'pm'
        common_hour_readable = most_common_hour - 12
    print('The most common hour of day for start time is {}{}.'.format(common_hour_readable, am_pm))
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start=df[start_time].mode().to_string(index=False)

    # TO DO: display most commonly used end station
    common_end=df['time.time()'].mode().to_string(index=False) 

    # TO DO: display most frequent combination of start station and end station trip
    comb=common_start+common_end            

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration=(df['time.time()']-df['start_time']).sum()
    minute,second=divmod(total_duration,60)
    hour,minute=divmod(minute,60)
    print('The total trip duration is {} hours,{} minutes and {} seconds.',format(hour,minute,second))
                
    # TO DO: display mean travel time
    average_duration=round((df['time.time()']-df['start_time']).mean())            
    m, s = divmod(average_duration, 60)
    if m > 60:               
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {} seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))           
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    subs=df.query('user_type=="Subscriber"').user_type.count()
    cust=df.query('user_type=="Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs,cust))            

    # TO DO: Display counts of gender
    male_count=df.query('gender=="Male"').gender.count()
    female_count=df.query('gender=="Female"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count,female_count))            

    # TO DO: Display earliest, most recent, and most common year of birth
    while city.lower not in CITY_DATA[washington]:
        earliest=int(df['birth_year'].min())
        latest=int(df['birth_year'].max())
        mode=int(df['birth_year'].mode())
        print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))

       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    Args:
        data frame
    Returns:
        none
    '''
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Sorry, I do not understand your input. Please type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
        # prints every column except the 'journey' column created in statistics()
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry, I do not understand your input. Please type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
       

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
