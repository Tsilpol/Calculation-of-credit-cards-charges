
import random
from collections import Counter
import time
import matplotlib.pyplot as plt

# Creation of the graph
def plot_execution_times(execution_times_with_hash, execution_times_without_hash, labels):
    plt.figure(figsize=(10, 6))

    bar_width = 0.35
    index = range(len(labels))

    plt.bar(index, execution_times_with_hash, width=bar_width, label='With HashTable', color='blue')
    plt.bar([i + bar_width for i in index], execution_times_without_hash, width=bar_width, label='Without HashTable', color='yellow')

    plt.xlabel('Number of Charges (in millions)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs Number of Charges')
    plt.xticks([i + bar_width/2 for i in index], labels)
    plt.legend()

    plt.show()
    
    
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    #Find the next prime number greater than the given number.
    while not is_prime(num):
        num += 1
    return num

class HashTable:
    def __init__(self, initial_size=101):
        self.size = initial_size
        self.table = [None] * initial_size
        self.count = 0

    def hash_function(self, key):
        """A simple hash function for demonstration purposes."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        if self.load_factor() > 0.7:
            self.resize()

        index = self.hash_function(key)
        collisions = 0

        while self.table[index] is not None:
            collisions += 1
            index = (index + 1) % self.size

        self.table[index] = (key, value)
        self.count += 1

        return collisions

    def search(self, key):
        """Search for a key in the hash table and return its value."""
        index = self.hash_function(key)
        initial_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == initial_index:
                break  # Avoid infinite loop if the key is not in the table

        return None  # Key not found

    def load_factor(self):
        """Calculate the load factor of the hash table."""
        return self.count / self.size

    def resize(self):
        """Resize the hash table and find the next prime size."""
        new_size = self.size * 2
        prime_size = next_prime(new_size)

        old_table = self.table
        self.size = prime_size
        self.table = [None] * prime_size
        self.count = 0

        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])

def run_code_1():
   # Set seed for reproducibility
    random.seed(2563)
# Function to generate a random credit card number
    def generate_credit_card():
        return ''.join(str(random.randint(0, 9)) for _ in range(16))
# Generate 20,000 different random credit card numbers
    credit_cards = [generate_credit_card() for _ in range(20000)]

    hash_table = HashTable()
    
    # Measure the execution time for Code 1
    start_time = time.time()

    total_collisions = 0
# For 1,000,000 iterations, randomly select a credit card number and generate a charge
    for _ in range(1000000):
        credit_card = random.choice(credit_cards)
        amount = round(random.uniform(10, 1000), 2)

        if hash_table.search(credit_card) is not None:
            total_payment_amount, total_payments, total_transactions = hash_table.search(credit_card)
        else:
            total_payment_amount, total_payments, total_transactions = 0, 0, 0

        total_payment_amount += amount
        total_payments += 1
        total_transactions += 1
# Collisions caused
        total_collisions += hash_table.insert(credit_card, (total_payment_amount, total_payments, total_transactions))

# End the execution time
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
    
    
    print(f"Total number of collisions: {total_collisions}")
    
# Find the card with the lowest total payment amount
    min_payment_card = min(credit_cards, key=lambda card: hash_table.search(card)[0])

# Find the card with the smallest total amount of payments
    min_payments_card = min(credit_cards, key=lambda card: hash_table.search(card)[1])

# Find the card with the largest total amount of transactions
    max_transactions_card = max(credit_cards, key=lambda card: hash_table.search(card)[2])

# Find the card with the largest number of transactions
    max_transaction_count_card = max(credit_cards, key=lambda card: hash_table.search(card)[2])

# Output the results
    print(f"Card with the lowest total payment amount: {min_payment_card}")
    print(f"Card with the smallest total amount of payments: {min_payments_card}")
    print(f"Card with the largest total amount of transactions: {max_transactions_card}")
    print(f"Card with the largest number of transactions: {max_transaction_count_card}")

def run_code_2():
   # Set seed for reproducibility
    random.seed(2563)

# Function to generate a random credit card number
    def generate_credit_card():
        return ''.join(str(random.randint(0, 9)) for _ in range(16))
    
    # Generate 20,000 different random credit card numbers
    credit_cards = [generate_credit_card() for _ in range(20000)]

# Measure the execution time for Code 2
    start_time = time.time()

    # Create Counter objects to store transaction data
    total_payment_amount = Counter()
    total_payments = Counter()
    total_transactions = Counter()

# For 1,000,000 iterations, randomly select a credit card number and generate a charge
    for _ in range(1000000):
        credit_card = random.choice(credit_cards)
        amount = round(random.uniform(10, 1000), 2)

# Update counters
        total_payment_amount[credit_card] += amount
        total_payments[credit_card] += 1
        total_transactions[credit_card] += 1

# Find the card with the lowest total payment amount
    min_payment_card = min(total_payment_amount, key=total_payment_amount.get)

    # Find the card with the smallest total amount of payments
    min_payments_card = min(total_payments, key=total_payments.get)

    # Find the card with the largest total amount of transactions
    max_transactions_card = max(total_transactions, key=total_transactions.get)

# Find the card with the largest number of transactions
    max_transaction_count_card = max(total_transactions, key=total_transactions.get)

    # End the execution time 
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    # Output the results
    print(f"Card with the lowest total payment amount: {min_payment_card}")
    print(f"Card with the smallest total amount of payments: {min_payments_card}")
    print(f"Card with the largest total amount of transactions: {max_transactions_card}")
    print(f"Card with the largest number of transactions: {max_transaction_count_card}")

#Menu to choose whether you want to run the code with hash table or not
def main():
    while True:
        print("Choose an option:")
        print("1. Run Code with HashTable")
        print("2. Run Code without HashTable")
        print("0. Exit")

        choice = input("Enter your choice (0, 1, or 2): ")

        if choice == '1':
            run_code_1()
        elif choice == '2':
            run_code_2()
        elif choice == '0':
            print("Exiting the program. Goodbye Mr. Gogos!")
            break
        else:
            print("Invalid choice. Please enter 0, 1, or 2.")

if __name__ == "__main__":
    main()
    
execution_times_with_hash = [19.5, 71.0, 288.8, 864.2]  # execution times with hash table
execution_times_without_hash = [1.8, 5.2, 9.1, 18.5]  # execution times without hash table
labels = ['1 Million', '2 Million', '4 Million', '6 Million']

plot_execution_times(execution_times_with_hash, execution_times_without_hash, labels)
