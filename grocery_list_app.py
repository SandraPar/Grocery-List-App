class Shopping: 
    def __init__(self):
        self.groceries = []
            
    def add_item(self):
        item = input("What item would you like to add? ")
        self.groceries.append(item)
        print(f'{item} has been added to your list.')

                    
    def remove_item(self):
        item = input('What item would you like to remove? ')
        if item in self.groceries:
            self.groceries.remove(item)
            print(f'{item} has been remove from your grocery list. ')
                        
    def update_list(self):
        if len(self.groceries) == 0:
            print('There are no items in your grocery list!')
        else:
            print('Grocery List:')
            for i, item in enumerate(self.groceries, start=1):
                print(f"{i}. {item}")
                    
def main():
    print('----- Grocery List App -----')
    my_list = Shopping()  # create an instance

    while True:
        print('\nMenu:')
        print('1. Add item')
        print('2. Delete item')
        print('3. View list')
        print('4. Exit')

        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue  # go back to the start of the loop

        if choice == 1:
            my_list.add_item()
        elif choice == 2:
            my_list.remove_item()
        elif choice == 3:
            my_list.update_list()
        elif choice == 4:
            print('Exiting app. Goodbye!')
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")




if __name__ == '__main__':
    main()