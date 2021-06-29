package exception_handling;

public class DemonetizationException extends Exception {
    DemonetizationException(Currency amount) {
        super("Deposit of old currency " + amount + " exceeds " +
                Account.MAX_OLD_CURRENCY + " and cannot be deposited");
    }
}
