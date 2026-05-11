import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

df = pd.read_csv(r'D:\snake\Uni\Lab7\sales.csv')



def menu():
    print("1. The biggest profit month")
    print("2. Average sales for the whole year")
    print("3. Print records where >6000 for toothpaste, <3000 for face cream")
    print("4. Total profit in all months")
    print("5. Visualization of units sold per month for each product")
    print("6. Correlation between sales of face cream and shampoo")
    print("7. Bar chart for sales of a shampoo in all the months")
    print("8. Yearly Average sales of moisturizer")
    print("9.Line Plot for all the months")
    print("10. Exit")


if __name__ == "__main__":
        
    while True:
        menu()
        choice = input("Enter your choice: ")
        match choice:
            case '1':

                idx = df['total_profit'].idxmax()
                month = df.loc[idx, 'month_number']
                profit = df.loc[idx, 'total_profit']
                print(f"The biggest profit month is: Month {month} with a profit of {profit}")
                time.sleep(1)
                print("\n")

            case '2':
                print(f"Average sales for the whole year: {df['total_profit'].mean()}")
                time.sleep(1)
                print("\n")

            case '3':
                filtered_data = df.loc[(df['toothpaste'] > 6000) & (df['facecream'] < 3000), 
                       ['month_number', 'toothpaste', 'facecream']]
                print(filtered_data.to_string(index=False))
                time.sleep(1)
                print("\n")

            case '4':
                print(f"Total profit in all months: {df['total_profit'].sum()}")
                time.sleep(1)
                print("\n")
                
            case '5':
                df.plot(x='month_number', y=['facecream', 'toothpaste', 'shampoo', 'moisturizer'], kind='line')
                plt.xlabel('Month Number')
                plt.ylabel('Units Sold')
                plt.title('Units Sold per Month for Each Product')
                plt.legend()
                plt.show()

            case '6':
                correlation = df['facecream'].corr(df['shampoo'])
                print(f"Correlation between sales of face cream and shampoo: {correlation:.5f}")
                time.sleep(1)
                print("\n")

            case '7':
                df.plot(x='month_number', y='shampoo', kind='bar')
                plt.xlabel('Month Number')
                plt.ylabel('Units Sold')
                plt.title('Sales of Shampoo in All Months')
                plt.show()
                time.sleep(1)
                print("\n")
            case '8':
                average_moisturizer = df['moisturizer'].mean()
                print(f"Yearly Average sales of moisturizer: {average_moisturizer:.3f}")
                time.sleep(1)
                print("\n")
            case '9':
                df.plot(x='month_number', y=['facecream', 'toothpaste', 'shampoo', 'moisturizer'], kind='line')
                plt.xlabel('Month Number')
                plt.ylabel('Units Sold')
                plt.title('Line Plot for All the Months')
                plt.legend()
                plt.show()
                time.sleep(1)
                print("\n")
            case '10':
                print("Exiting the program.")
                time.sleep(2)
                break
            case _:
                print("Invalid choice. Please try again.")
                time.sleep(2)