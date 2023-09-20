public interface TransactionManager {
    public boolean transferFunds(String senderWalletId, String receiverWalletId, double amount) throws Exception;

    public double getBalance(String walletId) throws Exception;

    public boolean isValidWallet(String walletId);
}
