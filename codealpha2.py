import tkinter as tk
import random

class StockPortfolio:
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Portfolio Tracker")
        self.stocks = {}
        self.symbol_label = tk.Label(master, text="Stock Symbol:")
        self.symbol_label.grid(row=0, column=0, padx=10, pady=10)
        self.symbol_entry = tk.Entry(master, width=15)
        self.symbol_entry.grid(row=0, column=1, padx=10, pady=10)

        self.quantity_label = tk.Label(master, text="Quantity:")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=10)
        self.quantity_entry = tk.Entry(master, width=15)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        self.price_label = tk.Label(master, text="Purchase Price:")
        self.price_label.grid(row=2, column=0, padx=10, pady=10)
        self.price_entry = tk.Entry(master, width=15)
        self.price_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Stock", command=self.add_stock)
        self.add_button.grid(row=3, column=1, padx=10, pady=10)

        self.stock_listbox = tk.Listbox(master, width=50, height=10)
        self.stock_listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.remove_button = tk.Button(master, text="Remove Stock", command=self.remove_stock)
        self.remove_button.grid(row=5, column=0, padx=10, pady=10)

        self.refresh_button = tk.Button(master, text="Refresh Prices", command=self.refresh_prices)
        self.refresh_button.grid(row=5, column=1, padx=10, pady=10)

        self.message_label = tk.Label(master, text="", fg="blue")
        self.message_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        self.total_value_label = tk.Label(master, text="Total Portfolio Value: $0.00", fg="green")
        self.total_value_label.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    def add_stock(self):
        symbol = self.symbol_entry.get().strip().upper()
        quantity = self.quantity_entry.get().strip()
        purchase_price = self.price_entry.get().strip()

        if not symbol or not quantity or not purchase_price:
            self.message_label.config(text="Please enter all fields.", fg="red")
            return

        if not quantity.isdigit() or not purchase_price.replace('.', '', 1).isdigit():
            self.message_label.config(text="Quantity and purchase price must be valid numbers.", fg="red")
            return

        quantity = int(quantity)
        purchase_price = float(purchase_price)

        if symbol in self.stocks:
            self.message_label.config(text="Stock already exists in the portfolio.", fg="red")
            return

        try:
            current_price = self.get_stock_price(symbol)
            if current_price is not None:
                self.stocks[symbol] = {'quantity': quantity, 'purchase_price': purchase_price, 'current_price': current_price}
                self.stock_listbox.insert(tk.END, f"{symbol}: {quantity} shares, Purchase Price: ${purchase_price:.2f}, Current Price: ${current_price:.2f}")
                self.message_label.config(text="Stock added successfully.", fg="green")
                self.update_total_value()
            else:
                self.message_label.config(text="Failed to add stock: Invalid symbol.", fg="red")
        except Exception as e:
            self.message_label.config(text=f"Failed to add stock: {e}", fg="red")

    def remove_stock(self):
        selected_index = self.stock_listbox.curselection()
        if not selected_index:
            self.message_label.config(text="Please select a stock to remove.", fg="red")
            return

        symbol = self.stock_listbox.get(selected_index[0]).split(":")[0].strip()
        del self.stocks[symbol]
        self.stock_listbox.delete(selected_index)
        self.message_label.config(text="Stock removed successfully.", fg="green")
        self.update_total_value()

    def refresh_prices(self):
        for i, (symbol, details) in enumerate(self.stocks.items()):
            try:
                current_price = self.get_stock_price(symbol)
                if current_price is not None:
                    self.stocks[symbol]['current_price'] = current_price
                    self.stock_listbox.delete(i)
                    self.stock_listbox.insert(i, f"{symbol}: {details['quantity']} shares, Purchase Price: ${details['purchase_price']:.2f}, Current Price: ${current_price:.2f}")
                else:
                    self.message_label.config(text=f"Failed to refresh prices for {symbol}: Invalid symbol.", fg="red")
            except Exception as e:
                self.message_label.config(text=f"Failed to refresh prices for {symbol}: {e}", fg="red")
        self.update_total_value()

    def get_stock_price(self, symbol):
        if symbol:  
            return round(random.uniform(100, 500), 2)
        else:
            return None

    def update_total_value(self):
        total_value = sum(details['quantity'] * details['current_price'] for details in self.stocks.values())
        self.total_value_label.config(text=f"Total Portfolio Value: ${total_value:.2f}")

def main():
    root = tk.Tk()
    app = StockPortfolio(root)
    root.mainloop()

if __name__ == "__main__":
    main()
