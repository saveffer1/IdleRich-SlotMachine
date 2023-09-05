from datetime import datetime
from collections import deque
import threading
import queue
import pickle
import time

class TransactionNode:
    def __init__(self):
        self.children = {}
        self.transactions = []
    
    def __str__(self) -> str:
        return self.transactions

class TransactionTrie:
    def __init__(self):
        self.root = TransactionNode()
    
    def insert(self, word, transaction):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TransactionNode()
            node = node.children[char]
            node.transactions.append(transaction)

    def search(self, query) -> tuple:
        node = self.root
        for char in query.lower():
            if char.lower() not in node.children:
                return []
            node = node.children[char]
        return tuple(node.transactions)
        
class TransactionHistory:
    def __init__(self):
        self.transactions_by_date = TransactionTrie()
        self.transactions_by_detail = TransactionTrie()
        self.transactions_by_amount = {}
        self.recent_transactions = deque(maxlen=30)
        self.all_transactions = []

    def insert(self, amount: int, detail: str, date: str=datetime.now().strftime("%d/%m/%Y-%H:%M:%S")):
        detail = detail.lower()
        amount = amount
        transaction = {"date": date, "detail": detail, "amount": amount}

        self.transactions_by_date.insert(date, transaction)
        self.transactions_by_detail.insert(detail, transaction)
        
        amount_str = str(amount)
        if amount_str in self.transactions_by_amount:
            self.transactions_by_amount[amount_str].append(transaction)
        else:
            self.transactions_by_amount[amount_str] = [transaction]
        
        self.all_transactions.append(transaction)
        self.recent_transactions.append(transaction)
    
    def transaction_history(self, limit:int=5) -> tuple:
        if limit <= 0:
            raise ValueError("Limit must be greater than 0 and less than 30")
        if limit > self.recent_transactions.maxlen:
            limit = self.recent_transactions.maxlen
        if limit > len(self.recent_transactions):
            limit = len(self.recent_transactions)
        return tuple(self.recent_transactions)[-limit:]

    def search_by_date(self, desired_date) -> tuple:
        return tuple(self.transactions_by_date.search(desired_date))

    def search_by_detail(self, desired_detail) -> tuple:
        return tuple(self.transactions_by_detail.search(desired_detail))

    def search_by_amount(self, desired_amount) -> tuple:
        amount_str = str(desired_amount)
        return tuple(self.transactions_by_amount.get(amount_str, None))

class Balance:
    def __init__(self, amount: int=0):
        self.clicked_balance = 0
        self.amount = 0
        self.transactions = TransactionHistory()
        if self.amount < 0:
            raise ValueError("Starting balance must be greater or equal 0")
        # self.add_transaction(amount, "Starting balance")
    
    def add_balance_by_click(self, clicked_balance: int):
        self.amount += clicked_balance
        self.clicked_balance += clicked_balance
    
    def add_transaction(self, transaction_amount: int, transaction_detail: str="What is this?", transaction_date: str=datetime.now().strftime("%d/%m/%Y-%H:%M:%S")) -> bool:
        if transaction_amount < 0:
            if self.amount + transaction_amount < 0:
                return False
        self.amount += transaction_amount
        transaction_th = threading.Thread(target=self.transactions.insert, args=(transaction_amount, transaction_detail, transaction_date))
        transaction_th.daemon = True
        transaction_th.start()
        transaction_th.join()
        return True
    
    def search_transaction(self, word: str, mode: str="detail"):
        if mode not in ["detail", "date", "amount"]:
            return None

        result_queue = queue.Queue()

        def thread_function():
            if mode == "detail":
                result = self.transactions.search_by_detail(word)
            elif mode == "date":
                result = self.transactions.search_by_date(word)
            elif mode == "amount":
                result = self.transactions.search_by_amount(word)

            result_queue.put(result)

        search_th = threading.Thread(target=thread_function)
        search_th.daemon = True
        search_th.start()

        search_th.join()
        result = result_queue.get()
        return result if result else None

    def last_transection(self, limit: int=5):
        return self.transactions.transaction_history(limit=limit)
        
    @staticmethod
    def format_balance(amount):
        suffixes = ["", "K", "M", "B", "T", "Q"]
        for suffix in suffixes:
            if abs(amount) < 1000:
                if abs(amount) >= 10:
                    return f"฿ {amount:,.2f} {suffix}"
                else:
                    return f"฿ {amount:,.2f} {suffix}"
            amount /= 1000.0
        return f"฿ {amount:,.2f} {'Q'}"

    def get_balance(self):
        return self.amount
    
    def __str__(self):
        return self.format_balance(self.amount)
    

# test
if __name__ == "__main__":
    raise RuntimeError("This module is not meant to run on its own!")