# Male Female Percentages
# 09/11/18
# CTI-110 P2HW2 - Male Female Percentage
# Forrest Bennett
# Find the percentage of males in the class.



# Get the total amount of Males in class.
total_males = float(input('total amount of males in class: '))

# Get the total amount of females in class
total_females= float(input('total amount of females in class: '))

# Get the percentage of males.
Percent_males = total_males / (total_males + total_females) * 100

# Get the percentage of females
Percent_females = total_females / (total_males + total_females) * 100

# Display the Perecentages
print(' The percentage is ' , Percent_males ) 

print(' the percentage is ' , Percent_females )

