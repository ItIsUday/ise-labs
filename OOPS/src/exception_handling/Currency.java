package exception_handling;

import java.text.NumberFormat;
import java.util.Locale;

public class Currency {
    private double amount;

    public Currency(double amount) {
        this.amount = amount;
    }

    public double getAmount() {
        return amount;
    }

    public void addAmount(double amount) {
        this.amount += amount;
    }

    public void subAmount(double amount) {
        this.amount -= amount;
    }

    @Override
    public String toString() {
        NumberFormat format = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        return format.format(amount);
    }
}
