public abstract class ShoppingCartDecorator extends ShoppingCart {
    protected ShoppingCart cart;

    public ShoppingCartDecorator(ShoppingCart cart) {
        this.cart = cart;
    }

    @Override
    public boolean[] getDiscountStatus() {
        return this.cart.getDiscountStatus();
    }

    @Override
    public void setDiscountStatus(boolean[] status) {
        this.cart.setDiscountStatus(status);
    }

    @Override
    public double getDeliveryFee() {
        return this.cart.getDeliveryFee();
    }

    @Override
    public double getNetPrice() {
        return this.cart.getNetPrice();
    }

    @Override
    public double calculateTotal() {
        return this.cart.calculateTotal();
    }
}