public class FreeDeliveryDecorator extends ShoppingCartDecorator {
    private boolean active;

  
    public FreeDeliveryDecorator(ShoppingCart cart) {
        super(cart);

        boolean[] status = cart.getDiscountStatus();
        
        this.active = !status[2];
        
        
        status[2] = true;
        this.cart.setDiscountStatus(status);
    }

    @Override
    public double getNetPrice() {
        if (!this.active) {
            return this.cart.getNetPrice();
        }
        
        return this.cart.getNetPrice() - this.cart.getDeliveryFee();
    }
}