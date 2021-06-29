package exception_handling;

import static java.lang.Double.compare;

public class Account {
    static final String RED = "\033[31;1m";
    static final String GREEN = "\033[32;1m";
    static final String RESET = "\033[0m";

    static final Currency MAX_OLD_CURRENCY = new Currency(5000);
    static final Currency MIN_BALANCE = new Currency(500);
    private final Currency balance;
    private final String name;

    Account(String name) {
        this.name = name;
        balance = new Currency(MIN_BALANCE.getAmount());
        System.out.println(GREEN + "Account created with " + balance + " balance" + RESET);
    }

    public String getName() {
        return name;
    }

    private void transactionMsg(boolean success) {
        if (success) {
            System.out.println(GREEN + "Transaction successful" + RESET);
        } else {
            System.out.println(RED + "Transaction failed" + RESET);
        }
    }

    public double getBalance() {
        return balance.getAmount();
    }

    public void currentBalance() {
        System.out.println("The current balance is " + balance);
    }

    public void deposit(double amount, String currencyType) {
        try {
            if (currencyType.equalsIgnoreCase("old") &&
                    compare(amount, MAX_OLD_CURRENCY.getAmount()) > 0) {
                throw new DemonetizationException(new Currency(amount));
            } else if (amount <= 0) {
                transactionMsg(false);
                System.out.println(RED + "Amount cannot be non-negative" + RESET);
            } else {
                balance.addAmount(amount);
                transactionMsg(true);
            }
        } catch (DemonetizationException e) {
            transactionMsg(false);
            System.out.println(RED + e.getMessage() + RESET);
        }
    }


    public void withdraw(double amount) {
        if (compare(getBalance(), amount) < 0) {
            transactionMsg(false);
            System.out.println(RED + "Insufficient balance" + RESET);
        } else if (amount <= 0) {
            transactionMsg(false);
            System.out.println(RED + "Amount cannot be non-negative" + RESET);
        } else if (compare(getBalance() - amount, MIN_BALANCE.getAmount()) < 0) {
            transactionMsg(false);
            System.out.println(RED + "Balance cannot fall below " + MIN_BALANCE + RESET);
        } else {
            balance.subAmount(amount);
            transactionMsg(true);
        }
    }
}
