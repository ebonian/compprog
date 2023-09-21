public class App {
    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();

        Item item1 = new Item("Widget", 3, 10.99);
        Item item2 = new Item("Gadget", 2, 19.99);

        cart.addItem(item1);
        cart.addItem(item2);

        // Your cart should set different discount strategies and display the total cost
        // after discount.

        // SampleDiscountStrategy
        cart.setDiscountStrategy(new SampleDiscountStrategy());
        System.out.printf("Total cost after SampleDiscountStrategy: %.2f\n", cart.calculateTotal());

        // PercentageDiscountStrategy
        cart.setDiscountStrategy(new PercentageDiscountStrategy(0.1));
        System.out.printf("Total cost after PercentageDiscountStrategy: %.2f\n", cart.calculateTotal());

        // FixedDiscountStrategy
        cart.setDiscountStrategy(new FixedDiscountStrategy(10));
        System.out.printf("Total cost after FixedDiscountStrategy: %.2f\n", cart.calculateTotal());
    }
}