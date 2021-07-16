package exception_handling;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int choice;
        String currencyType;
        double amount;
        Scanner in = new Scanner(System.in);

        System.out.print("Enter your name: ");
        Account account = new Account(in.nextLine());
        System.out.println("Welcome, " + account.getName());

        while (true) {
            System.out.print("\n1. Check balance\n2. Deposit\n3. Withdraw\n-1. Exit\nEnter your choice: ");
            choice = in.nextInt();
            switch (choice) {
                case 1 -> account.currentBalance();
                case 2 -> {
                    System.out.print("Enter amount: ");
                    amount = in.nextDouble();
                    in.nextLine();
                    System.out.print("Enter currency type: ");
                    currencyType = in.nextLine();
                    account.deposit(amount, currencyType);
                    account.currentBalance();
                }
                case 3 -> {
                    System.out.print("Enter amount: ");
                    amount = in.nextDouble();
                    account.withdraw(amount);
                    account.currentBalance();
                }
                case -1 -> System.exit(0);
                default -> System.out.println("Invalid choice");
            }
        }
    }
}
