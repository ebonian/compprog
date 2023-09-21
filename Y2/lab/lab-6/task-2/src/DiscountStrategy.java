public interface DiscountStrategy {
    double applyDiscount(double price);
}

class SampleDiscountStrategy implements DiscountStrategy {
    public SampleDiscountStrategy() {
    }

    public double applyDiscount(double price) {
        return price;
    }
}

class PercentageDiscountStrategy implements DiscountStrategy {
    private double percentage;

    public PercentageDiscountStrategy(double percentage) {
        this.percentage = percentage;
    }

    public double applyDiscount(double price) {
        return price * (1 - percentage);
    }

}

class FixedDiscountStrategy implements DiscountStrategy {
    private double fixedAmount;

    public FixedDiscountStrategy(double fixedAmount) {
        this.fixedAmount = fixedAmount;
    }

    public double applyDiscount(double price) {
        return price - fixedAmount;
    }
}