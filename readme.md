## App Features

* **Gift Card Definition:**
    * Allows users to define new gift cards with a name, spending limit ($100-$500), and maximum number of items (1-5).
    * Validates user input to ensure it falls within the specified ranges.
    * Stores gift card details in a CSV file (`giftCards.csv`), preventing duplicate card names.
* **Default Gift Card:**
    * Provides a default gift card ("Victory-day gift card") with a $200 limit and a maximum of 4 items if the user skips card definition.
* **Spending Spree:**
    * Simulates a spending spree using defined or default gift cards.
    * Tracks purchases and updates the gift card's balance.
    * saves spending history to the `spendingHistory.csv` file.
* **Display Gift Card List:**
    * Displays a list of all defined gift cards from `giftCards.csv`, including their names, spending limits, and maximum item counts.
* **Display Spending History:**
    * Shows a list of all purchased items, including item names, prices, and the gift cards used, from the `spendingHistory.csv` file.
* **User-Friendly Menu:**
    * Presents a clear menu with options for defining gift cards, spending, viewing card lists, viewing spending history, and quitting.
* **Data Persistence:**
    * Uses CSV files (`giftCards.csv` and `spendingHistory.csv`) to store and retrieve gift card and spending data.