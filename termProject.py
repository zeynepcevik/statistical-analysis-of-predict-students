import matplotlib.pyplot as plt
def read_file(file_path):
    # Reads the 'Course' column from the file and returns it as a list
    enrollment_column = []
    # Read the file and extract the 'Course' column data
    # Assuming 'Course' column is at index 3
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip the header line
            data = line.split(',')
            course = float(data[17])
            enrollment_column.append(course)
    return enrollment_column

# Read the file and obtain the 'Age at enrollment' column data
file_path = r'C:\Users\ASUS\Downloads\archive\dataset.csv'
enrollment_column = read_file(file_path)

#print(course_column)

# Function to calculate the sum of a list of values
def sum(column):
    total = 0
    for value in column:
        total += value
    return total

# Function to calculate the length of a list
def len(column):
    count = 0
    for _ in column:
        count += 1
    return count
# Function to calculate the mean of a list of values
def calculate_mean(column):
    total = sum(column)
    mean = total / len(column)
    return mean

# Calculate and print the mean of the 'Age at enrollment' column
mean = calculate_mean(enrollment_column)
print("Mean:", mean)


# Function to calculate the median of a list of values
def calculate_median(column):
    sorted_column = sorted(column)
    length = len(sorted_column)

    if length % 2 == 0:
        mid = length // 2
        median = (sorted_column[mid - 1] + sorted_column[mid]) / 2
    else:
        mid = length // 2
        median = sorted_column[mid]

    return median

# Calculate and print the median of the 'CAge at enrollment' column
median = calculate_mean(enrollment_column)
print("Median:", median)

# Function to calculate the standard deviation of a list of values
def standard_deviation(column):
    s_deviation = 0.0
    num_data = len(column)
    if num_data <= 1:
        return 0.0
    else:
        mean = calculate_mean(column)
        for value in column:
            s_deviation += (float(value) - mean) ** 2
        sd = (s_deviation / float(num_data - 1)) ** 0.5
        return sd

# Calculate and print the standard deviation of the 'Age at enrollment' column
sd = standard_deviation(enrollment_column)
print("Standard Deviation:", sd)

# Function to calculate the variance of a list of values
def calculate_variance(column, sd):
    return standard_deviation(column) ** 2

# Calculate and print the variance of the 'Age at enrollment' column
variance = calculate_variance(enrollment_column, sd)
print("Variance:", variance)

# Function to calculate the standard error of a list of values
def calculate_standard_error(column):
    return standard_deviation(column) / (len(column) ** 0.5)

# Calculate and print the standard error of the 'Age at enrollment' column
standard_error = calculate_standard_error(enrollment_column)
print("Standard Error:", standard_error)


# Generate and display a histogram of the 'Age at enrollment' column
plt.hist(enrollment_column, bins=7)  # Adjust the number of bins as needed
plt.xlabel('Age at enrollment')
plt.ylabel('Frequency')
plt.title('Histogram of Age at enrollment Column')
plt.show()

# Calculate quartiles and identify outliers in the 'Age at enrollment' column
sorted_column = sorted(enrollment_column)
length = len(sorted_column)
q1_index = int(length * 0.25)
q3_index = int(length * 0.75)
q1 = sorted_column[q1_index]
q3 = sorted_column[q3_index]
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = [x for x in enrollment_column if x < lower_bound or x > upper_bound]

# Print the outliers in the 'Age at enrollment' column
print("Outliers:", outliers)

plt.boxplot(enrollment_column)
plt.ylabel('Age at enrollment')
plt.title('Boxplot of Age at enrollment Column')


# Add annotation indicating if outliers are present
if len(outliers) == 0:
    plt.annotate('No outliers', xy=(0.5, 0.9), xycoords='axes fraction', ha='center', fontsize=12)
else:
    plt.annotate('Outliers detected', xy=(0.5, 0.9), xycoords='axes fraction', ha='center', fontsize=12)

plt.show()


# Function to calculate the confidence interval of a list of values
def calculate_confidence_interval(data, confidence_level):
    mean = calculate_mean(data)
    standard_error = calculate_standard_error(data)
    t_critical = t_value(confidence_level, len(data) - 1)
    margin_of_error = t_critical * standard_error
    confidence_interval = (mean - margin_of_error, mean + margin_of_error)
    return confidence_interval

# Function to retrieve the t-value based on the confidence level and degrees of freedom
def t_value(confidence_level, degrees_of_freedom):
    t_distribution = {
        0.9: 1.645,
        0.95: 1.96,
        0.99: 2.626,
    }
    return t_distribution[confidence_level]

confidence_level = 0.95

# Calculate and print the confidence intervals for the mean and variance of the 'Age at enrollment' column
confidence_interval_mean = calculate_confidence_interval(enrollment_column, confidence_level)
confidence_interval_variance = calculate_confidence_interval(enrollment_column, confidence_level)

print(f"{confidence_level * 100}% Confidence Interval for the Mean:", confidence_interval_mean)
print(f"{confidence_level * 100}% Confidence Interval for the Variance:", confidence_interval_variance)

# Function to calculate the required sample size based on the error margin, confidence level, and standard deviation
def calculate_sample_size(error_margin, confidence_level, standard_deviation):
    if confidence_level == 0.9:
        t_critical = 1.645
    elif confidence_level == 0.95:
        t_critical = 1.96
    elif confidence_level == 0.99:
        t_critical = 2.626
    else:
        raise ValueError("Unsupported confidence level")

    sample_size = (t_critical * standard_deviation / error_margin) ** 2
    return int(sample_size)

error_margin = 0.1
confidence_level = 0.9

# Calculate and print the required sample size for the 'Age at enrollment' column
standard_deviation = standard_deviation(enrollment_column)  # Use the calculated standard deviation
sample_size = calculate_sample_size(error_margin, confidence_level, standard_deviation)
print("Required Sample Size:", sample_size)