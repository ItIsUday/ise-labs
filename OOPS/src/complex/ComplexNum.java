package complex;

import java.util.Objects;

public class ComplexNum {

    float real, imaginary;

    ComplexNum() {
    }

    ComplexNum(float real, float imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    ComplexNum add(ComplexNum other) {
        return new ComplexNum(this.real + other.real, this.imaginary + other.imaginary);
    }

    ComplexNum subtract(ComplexNum other) {
        return new ComplexNum(this.real - other.real, this.imaginary - other.imaginary);

    }

    void iAdd(ComplexNum other) {
        this.real += other.real;
        this.imaginary += other.imaginary;
    }

    void iSubtract(ComplexNum other) {
        this.real -= other.real;
        this.imaginary -= other.imaginary;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if (other == null || getClass() != other.getClass()) return false;
        ComplexNum that = (ComplexNum) other;
        return Float.compare(that.real, real) == 0 && Float.compare(that.imaginary, imaginary) == 0;
    }

    @Override
    public int hashCode() {
        return Objects.hash(real, imaginary);
    }

    @Override
    public String toString() {
        String sign = " + ";
        float imaginary = this.imaginary;
        if (this.imaginary < 0) {
            sign = " - ";
            imaginary *= -1;
        }

        return this.real + sign + "i" + imaginary;
    }
}