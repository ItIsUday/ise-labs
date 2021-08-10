package lambda_expressions;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        performOperation obj = (operation, num) -> {
            boolean result = false;

            switch (operation) {
                case 1 -> result = num % 2 == 1;

                case 2 -> {
                    if (num >= 2) {
                        for (int i = 2; i <= Math.sqrt(num); i++) {
                            if (num % i == 0)
                                return false;
                        }
                        result = true;
                    }
                }

                case 3 -> {
                    int originalNum = num, reversedNum = 0, remainder;
                    while (num != 0) {
                        remainder = num % 10;
                        reversedNum = reversedNum * 10 + remainder;
                        num /= 10;
                    }
                    result = originalNum == reversedNum;
                }

                default -> System.out.println("Invalid operation");
            }
            return result;
        };

        Scanner in = new Scanner(System.in);
        int choice, num;


        System.out.print("Enter a number: ");
        num = in.nextInt();

        System.out.print("""
                1. Check if odd
                2. Check if prime
                3. Check if palindrome
                -1. Exit
                Enter your choice:\s""");
        choice = in.nextInt();

        switch (choice) {
            case 1 -> {
                if (obj.operate(choice, num))
                    System.out.println(num + " is odd");
                else
                    System.out.println(num + " is even");
            }

            case 2 -> {
                if (obj.operate(choice, num))
                    System.out.println(num + " is a prime number");
                else
                    System.out.println(num + " is not a prime number");
            }
            case 3 -> {
                if (obj.operate(choice, num))
                    System.out.println(num + " is a palindrome");
                else
                    System.out.println(num + " is not a palindrome");
            }
            default -> System.out.println("Invalid choice");
        }
    }
}
