package complex;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        var num1 = new ComplexNum();
        System.out.println("Created " + num1 + " using default constructor");

        ComplexNum num2 = scanComplexNum();
        ComplexNum num3 = scanComplexNum();

        ComplexNum num4 = num2.add(num3);
        System.out.println("Added " + num2 + " and " + num3 + " to get " + num4);
        System.out.print("Subtracted " + num3 + " from " + num1 + " in place to update it to ");
        num1.iSubtract(num3);
        System.out.println(num1);

        ComplexNum num5 = num1.subtract(num2);
        System.out.println("Subtracted " + num1 + " and " + num2 + " to get " + num5);
        System.out.print("Added " + num5 + " to " + num3 + " in place to update it to ");
        num3.iAdd(num5);
        System.out.println(num3);

    }

    static ComplexNum scanComplexNum() {
        Scanner in = new Scanner(System.in);

        System.out.println("Enter a new Complex number: ");
        System.out.print("Real part: ");
        float real = in.nextFloat();
        System.out.print("Imaginary part: ");
        float imaginary = in.nextFloat();

        var num = new ComplexNum(real, imaginary);
        System.out.print("Created " + num + " using parameterized constructor\n\n");
        return num;
    }
}
