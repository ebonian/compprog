package door;

public class FingerprintModule {
    private String fingerprintSerialNumber;
    private String fingerprint;

    public FingerprintModule(String fingerprintSerialNumber) {
        this.fingerprintSerialNumber = fingerprintSerialNumber;
    }

    public String getFingerprintSerialNumber() {
        return fingerprintSerialNumber;
    }

    public void registerFingerprint(String fingerprint) {
        this.fingerprint = fingerprint;
    }

    public boolean checkFingerprint(String fingerprint) {
        if (this.fingerprint.equals(fingerprint)) {
            return true;
        } else {
            return false;
        }
    }
}
