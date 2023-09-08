public class SimpleTransactionManager implements TransactionManager {
    private String[] wallets;
    private String[] transactions;
    private int walletCount;
    private int transactionCount;

    public SimpleTransactionManager(String[] wallets) {
        this.wallets = new String[10];

        for (int i = 0; i < wallets.length; i++) {
            this.wallets[i] = wallets[i];
        }

        this.transactions = new String[100];
        this.walletCount = wallets.length;
        this.transactionCount = 0;

    }

    public boolean transferFunds(String senderWalletId, String receiverWalletId, double amount) {
        if (!this.isValidWallet(senderWalletId)) {
            throw new IllegalArgumentException("Sender wallet is invalid");
        }

        if (!this.isValidWallet(receiverWalletId)) {
            this.wallets[this.walletCount] = receiverWalletId;
            this.walletCount++;
        }

        if (this.getBalance(senderWalletId) < amount && !senderWalletId.equals("Wallet0")) {
            throw new IllegalArgumentException("Insufficient funds");
        }

        this.transactions[this.transactionCount] = senderWalletId + "|" +
                receiverWalletId + "|" + amount;
        this.transactionCount++;

        return true;
    }

    public double getBalance(String walletId) {
        if (!isValidWallet(walletId)) {
            throw new IllegalArgumentException("Invalid wallet ID.");
        }

        double balance = 0.0;
        for (int i = 0; i < transactionCount; i++) {
            String[] parts = transactions[i].split("\\|");
            if (parts[0].equals(walletId)) {
                balance -= Double.parseDouble(parts[2]);
            }
            if (parts[1].equals(walletId)) {
                balance += Double.parseDouble(parts[2]);
            }
        }

        return balance;
    }

    public boolean isValidWallet(String walletId) {
        for (String wallet : this.wallets) {
            if (walletId.equals(wallet)) {
                return true;
            }
        }

        return false;
    }
}
