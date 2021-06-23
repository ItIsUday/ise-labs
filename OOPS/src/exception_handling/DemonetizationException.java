package exception_handling;

public class DemonetizationException extends Exception {
    DemonetizationException(Currency amount) {
        super("Deposit of old currency " + amount + " crosses " +
                Account.MAX_OLD_CURRENCY + " and cannot be deposited");
    }
}
