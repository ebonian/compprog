abstract class Shape {
    protected String color;

    public Shape(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    public abstract double getArea();

    public abstract void printDetails();
}

class Square extends Shape {
    private double sideLength;

    public Square(String color, double sideLength) {
        super(color);
        this.sideLength = sideLength;
    }

    public double getSideLength() {
        return sideLength;
    }

    public double getArea() {
        return sideLength * sideLength;
    }

    public void printDetails() {
        System.out.println("Shape: Square");
        System.out.println("Color: " + color);
        System.out.println("Side Length: " + sideLength);
        System.out.println("Area: " + getArea());
        System.out.println("----------------------");
    }

    public void resize(double factor) {
        sideLength *= factor;
    }
}

class Rectangle extends Shape {
    private double width;
    private double height;

    public Rectangle(String color, double width, double height) {
        super(color);
        this.width = width;
        this.height = height;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    public double getArea() {
        return width * height;
    }

    public void printDetails() {
        System.out.println("Shape: Rectangle");
        System.out.println("Color: " + color);
        System.out.println("Width: " + width);
        System.out.println("Height: " + height);
        System.out.println("Area: " + getArea());
        System.out.println("----------------------");
    }

    public void resize(double factor) {
        width *= factor;
        height *= factor;
    }
}

class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public double getArea() {
        return Math.PI * radius * radius;
    }

    public void printDetails() {
        System.out.println("Shape: Circle");
        System.out.println("Color: " + color);
        System.out.println("Radius: " + radius);
        System.out.println("Area: " + getArea());
        System.out.println("----------------------");
    }

    public void resize(double factor) {
        radius *= factor;
    }
}

public class Lab4_6538068821 {
    public static void main(String[] args) throws Exception {
        Shape[] shapes = {
                new Square("Red", 5.0),
                new Square("Blue", 3.0),
                new Rectangle("Green", 4.0, 6.0),
                new Rectangle("Yellow", 2.0, 8.0),
                new Circle("Orange", 7.0)
        };

        for (Shape shape : shapes) {
            shape.printDetails();
        }
    }
}
