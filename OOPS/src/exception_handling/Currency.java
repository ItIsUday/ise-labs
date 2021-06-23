package exception_handling;

import java.text.NumberFormat;
import java.util.Locale;

public class Currency {
    //    TODO: limit precision of amount
    //    TODO: add methods for comparing amount
    private double amount;

    public Currency(double amount) {
        this.amount = amount;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public void addAmount(Currency amount) {
        this.amount += amount.getAmount();
    }

    public void subAmount(Currency amount) {
        this.amount -= amount.getAmount();
    }

    @Override
    public String toString() {
        NumberFormat format = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        return format.format(amount);
    }
}
