package circle_cylinder;

import static java.lang.Math.PI;

public class Circle {

    double radius, color;

    Circle(double radius) {
        this.radius = radius;
    }

    Circle(double radius, double color) {
        this.radius = radius;
        this.color = color;
    }

    double getRadius() {
        return radius;
    }

    double getArea() {
        return PI * radius * radius;
    }
}
