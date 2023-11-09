public class DiscountByAmountDecorator extends ShoppingCartDecorator {

    private double amount;

    
    private boolean active;

   
    public DiscountByAmountDecorator(ShoppingCart cart, double amount) {
        super(cart);
        this.amount = amount;

        boolean[] status = cart.getDiscountStatus();
        
      
        this.active = !status[1];
        
        
        status[1] = true;
        this.cart.setDiscountStatus(status);
    }

   
    @Override
    public double getNetPrice() {
        if (!this.active) {
            return this.cart.getNetPrice();
        }

        return this.cart.getNetPrice() - this.amount;
    }
}