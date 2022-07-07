import random
import psycopg2

days = {
    'monday': ['green', 'yellow', 'green', 'brown', 'blue', 'pink', 'blue', 'yellow', 'orange', 'cream', 'orange', 'red', 'white', 'blue', 'white', 'blue', 'blue', 'blue', 'green'],
    'tuesday': ['arsh', 'brown', 'green', 'brown', 'blue', 'blue', 'blue', 'pink', 'pink', 'orange', 'orange', 'red', 'white', 'blue', 'white', 'white', 'blue', 'blue', 'blue'],
    'wednesday': ['green', 'yellow', 'green', 'brown', 'blue', 'pink', 'red', 'yellow', 'orange', 'red', 'orange', 'red', 'blue', 'blue', 'white', 'blue', 'blue', 'white', 'white'],
    'thursday': ['blue', 'blue', 'green', 'white', 'blue', 'brown', 'pink', 'yellow', 'orange', 'cream', 'orange', 'red', 'white', 'blue', 'white', 'blue', 'blue', 'blue', 'green'],
    'friday': ['green', 'white', 'green', 'brown', 'blue', 'blue', 'black', 'white', 'orange', 'red', 'red', 'red', 'white', 'blue', 'white', 'blue', 'blue', 'blue', 'white'],
}

all_colors = []
for colors in days.values():  # Putting all shirt colors in a list
    for color in colors:
        all_colors.append(color)

color_name_frequency = {color: all_colors.count(color) for color in all_colors}
color_frequency = color_name_frequency.values()

# Solution to question 1 (Finding Mean)
frequency_sum = sum(color_frequency)
mean = frequency_sum / len(color_frequency)
print('Question 1 => Mean: ' + str(mean))


# Solution to question 2 (Finding Mode)
mode = max(color_frequency)
mode_color = [color for color, frequency in color_name_frequency.items() if frequency == mode][0]
print(f'Question 2 => Mode: {mode}, which is color {mode_color}')


# Solution to question 3 (Finding Median)
# Sorting the list and locating median number by index of the middle value
for i in (cf_sorted := sorted(color_frequency)):
    median = cf_sorted[len(cf_sorted) // 2]
median_color = [color for color, frequency in color_name_frequency.items() if frequency == median][0]
print(f'Question 3 => Median: {median}, which is color {median_color}')


# Solution to question 4 (Finding Variance) BONUS
variance = [(i - mean) ** 2 for i in color_frequency]
variance = sum(variance)
variance /= len(color_frequency)
print('Question 4 => Variance: ' + str(variance))


# Solution to question 5 (Probability that a color is red) BONUS
red_frequency = color_name_frequency['red']
probability_of_red = (1 / red_frequency) * sum(color_frequency)
print(f'Question 5 => Probability of picking 1 red shirt: {probability_of_red}')


# Solution to question 6 ()
conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='',
    host='localhost',
    port='5432'
)
conn.autocommit = True
cursor = conn.cursor()
try:
    sql = '''CREATE TABLE IF NOT EXISTS COLOR_DETAILS(color_name char(20) UNIQUE, color_frequency varchar(30));'''
    cursor.execute(sql)

    database_info = {color: (color, all_colors.count(color)) for color in all_colors}
    columns = database_info.keys()
    for i in database_info.values():
        sql2 = '''insert into COLOR_DETAILS(color_name, color_frequency) VALUES{};'''.format(i)
        cursor.execute(sql2)

    sql3 = '''select * from COLOR_DETAILS;'''
    cursor.execute(sql3)
    conn.commit()
    conn.close()
except psycopg2.errors.UniqueViolation:
    print('Color already exits in database')
finally:
    print('Question 6 => Color name and frequency stored in database')

# Solution to question 8 (converting to base 10)
base_2 = ''
for i in range(5):
    base_2 += str(random.randint(0, 1))
to_base_10 = int(base_2, base=2)
print(f'Question 8 => Random digit to base10: {base_2} -> {to_base_10}')


# Solution to question 9 (Fibonacci sequence)
sequence = [0, 1]
n1, n2 = 0, 1
for i in range(1, (50-1)):
    sequence.append(sequence[i - 1] + sequence[i])
print(f'Question 9 => Sum of first 50 Fibonacci sequence: {sum(sequence)}')
# print(sum_of_fibonacci)


# Solution to question 7 (Recursive algorithm) BONUS
list_of_numbers = [i for i in range(30)]
while True:
    try:
        user_number = int(input('Question 7 => Enter number: '))
        if user_number in list_of_numbers:
            print('Number in list of numbers')
            continue
        else:
            print('Number not in list')
    except ValueError:
        print('It must be a number')
