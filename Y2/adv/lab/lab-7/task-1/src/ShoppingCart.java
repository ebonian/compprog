import java.util.ArrayList;
import java.util.List;

public class ShoppingCart {
    private List<String> items;
    private double deliveryFee;
    private boolean[] discountStatus;

    public ShoppingCart() {
        this.items = new ArrayList<>();
        this.discountStatus = new boolean[] {false, false, false};
    }

    public void addItem(String item) {
        this.items.add(item);
    }

    public double calculateTotal() {
        double total = 0.0;
        
        for (String item : items) {
            String[] parts = item.split(":");
            double quantity = Double.parseDouble(parts[1]);
            double price = Double.parseDouble(parts[2]);
            
            total += quantity * price;
        }
        
        return total;
    }

    public void setDiscountStatus(boolean[] status) {
        this.discountStatus = status;
    }

    public boolean[] getDiscountStatus() {
        return this.discountStatus;
    }

    public void addDeliveryFee(int fee) {
        this.deliveryFee = fee;
    }

    public double getDeliveryFee() {
        return this.deliveryFee;
    }

    public double getNetPrice() {
        return calculateTotal() + this.deliveryFee;
    }
}