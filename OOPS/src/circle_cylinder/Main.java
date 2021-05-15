package circle_cylinder;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Cylinder c1 = inputCylinder();
        Cylinder c2 = inputCylinder();

        System.out.println(compareCylinders(c1, c2));
    }

    static String compareCylinders(Cylinder c1, Cylinder c2) {
        String str = " ";
        if (!c1.equals(c2))
            str = " not ";

        return "The two cylinders are" + str + "same";
    }

    static Cylinder inputCylinder() {
        double radius, color, height;
        Scanner in = new Scanner(System.in);

        System.out.println("Enter the details for a cylinder: ");
        System.out.print("Radius: ");
        radius = in.nextDouble();
        System.out.print("Color: ");
        color = in.nextDouble();
        System.out.print("Height: ");
        height = in.nextDouble();
        System.out.println();

        return new Cylinder(radius, color, height);
    }
}
