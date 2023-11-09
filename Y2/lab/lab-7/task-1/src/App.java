public class App {
    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();

        cart.addItem("Apple:2:50.0");
        cart.addItem("Orange:1:30.0");

        cart.addDeliveryFee(10);
        System.out.println("Expected Delivery fee: $10.0");
        System.out.println("Actual Delivery fee: $" + cart.getDeliveryFee() + "\n");

        System.out.println("Expected Net price before any discounts: $140.0 (100 for apples + 30 for orange + 10 delivery fee)");
        System.out.println("Actual Net price: $" + cart.getNetPrice() + "\n");

        cart = new DiscountByPercentDecorator(cart, 10);
        System.out.println("Expected Net price after 10% discount: $127.0 ((100 + 30) * 0.9 + 10 delivery fee)");
        System.out.println("Actual Net price: $" + cart.getNetPrice() + "\n");

        cart = new DiscountByAmountDecorator(cart, 10);
        System.out.println("Expected Net price after additional $10 discount: $117.0 (127 - 10)");
        System.out.println("Actual Net price: $" + cart.getNetPrice() + "\n");

        cart = new DiscountByAmountDecorator(cart, 10);
        System.out.println("Expected Net price (no additional $10 discount should be applied): $117.0");
        System.out.println("Actual Net price: $" + cart.getNetPrice() + "\n");

        cart = new FreeDeliveryDecorator(cart);
        System.out.println("Expected Net price after free delivery: $107.0 (117 - 10)");
        System.out.println("Actual Net price: $" + cart.getNetPrice() + "\n");

        double total = cart.calculateTotal();
        double netPrice = cart.getNetPrice();
        System.out.println("Final Total Price: $" + total);
        System.out.println("Final Net Price: $" + netPrice);
    }
}
