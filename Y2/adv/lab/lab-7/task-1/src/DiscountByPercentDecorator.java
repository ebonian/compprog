public class DiscountByPercentDecorator extends ShoppingCartDecorator {
    private double percentage;

    private boolean active;

    public DiscountByPercentDecorator(ShoppingCart cart, double percentage) {
        super(cart);
        this.percentage = percentage;

        boolean[] status = cart.getDiscountStatus();
        
       
        this.active = !status[0];
        
        status[0] = true;
        this.cart.setDiscountStatus(status);
    }

    @Override
    public double getNetPrice() {
        if (!this.active) {
            return this.cart.getNetPrice();
        }

        return this.cart.getDeliveryFee() + (this.cart.calculateTotal() * (1 - this.percentage / 100));
    }
}