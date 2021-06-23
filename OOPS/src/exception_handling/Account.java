package exception_handling;

public class Account {
    static final Currency MAX_OLD_CURRENCY = new Currency(5000);
    static final Currency MIN_BALANCE = new Currency(500);
    private final Currency balance;

    Account() {
        balance = new Currency(MIN_BALANCE.getAmount());
    }

    public void deposit(Currency amount, String currencyType) {
        try {
            if (currencyType.equalsIgnoreCase("old") &&
                    amount.getAmount() > MAX_OLD_CURRENCY.getAmount()) {
                throw new DemonetizationException(amount);
            } else {
                balance.addAmount(amount);
            }
        } catch (DemonetizationException e) {
            System.out.println(e.getMessage());
        }
    }

    public double currentBalance() {
        return balance.getAmount();
    }

    public void withdraw(double withdrawal) {
    }
}
