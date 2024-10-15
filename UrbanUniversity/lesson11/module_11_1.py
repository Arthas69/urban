import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def matplot():
    # Load the dataset from a CSV file and plot the Dow Jones Index using Matplotlib.
    data = pd.read_csv('datasets/dowjones.csv')

    # Set up the figure and axes for the plot.
    fig, ax = plt.subplots()

    # Set the title, labels, and plot the data.
    plt.title('DowJones Index')

    # Format the x-axis ticks and labels.
    ax.set_xticks(np.arange(0, len(data['DATE']), 50))
    ax.set_xticklabels(data['DATE'][::50], rotation=45)

    # Format the y-axis ticks and labels.
    ax.set_xlabel('DATE')
    ax.set_ylabel('INDEX')

    # Plot the Dow Jones Index data.
    plt.plot(data['DATE'], data['M1109BUSM293NNBR'])

    # Show the plot.
    plt.show()


def pandas_analysis():
    # Read for csv file
    data = pd.read_csv('datasets/dowjones.csv')

    # Print the first 5 rows.
    print(data.head(5))

    # Print the last 5 rows.
    print(data.tail(5))

    # Make a graph from csv file.
    data.plot()
    plt.show()


def numpy_analysis():
    # Generate a random array of 50 integers between 1 and 10,000.
    array = np.random.randint(1, 10_000, 50)

    # Calculate the mean, median of the array.
    mean = np.mean(array)
    median = np.median(array)

    print(f'Mean: {mean}')
    print(f'Median: {median}')

    # Generate a 2D array with the first half of the original array on the first row and the second half on the second row.
    array_2n = np.array([array[:len(array) // 2], array[len(array) // 2:]])

    # Calculate the mean of the first and second half of the array.
    mean_2n = array_2n.mean(axis=1)
    print(mean_2n)


if __name__ == '__main__':
    print("""
    To plot the Dow Jones Index, press 1.
    To analise the data with Pandas, press 2.
    To analyze the data with Numpy, press 3.
    
    To exit, press any other key.
    """)
    choice = input('Enter: ')
    while True:
        if choice == '1':
            matplot()
            break
        elif choice == '2':
            pandas_analysis()
            break
        elif choice == '3':
            numpy_analysis()
            break
        else:
            exit()
