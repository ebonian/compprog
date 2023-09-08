public interface TransactionManager {
    public boolean transferFunds(String senderWalletId, String receiverWalletId, double amount);

    public double getBalance(String walletId);

    public boolean isValidWallet(String walletId);
}
