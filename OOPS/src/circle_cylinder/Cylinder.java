package circle_cylinder;

import java.util.Objects;

import static java.lang.Math.PI;
import static java.lang.Math.pow;

public class Cylinder extends Circle {

    double height;

    Cylinder(double radius, double height) {
        super(radius);
        this.height = height;
    }

    Cylinder(double radius, double color, double height) {
        super(radius, color);
        this.height = height;
    }

    double getVolume() {
        return PI * pow(getRadius(), 2) * height;
    }

    @Override
    double getArea() {
        return 2 * PI * getRadius() * (height + getRadius());
    }

    double getHeight() {
        return height;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Cylinder)) return false;
        Cylinder cylinder = (Cylinder) o;
        return Double.compare(cylinder.getArea(), this.getArea()) == 0 &&
                Double.compare(cylinder.color, color) == 0 &&
                Double.compare(cylinder.getVolume(), this.getVolume()) == 0;
    }

    @Override
    public int hashCode() {
        return Objects.hash(radius, color, height);
    }
}
