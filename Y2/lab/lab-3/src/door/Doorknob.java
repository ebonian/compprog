package door;

public class Doorknob {
    private String doorknobID;

    public Doorknob(String doorknobID) {
        this.doorknobID = doorknobID;
    }

    public String getDoorknobID() {
        return doorknobID;
    }

    public boolean canUnlock(Key key) {
        if (key.getKeyID().equals(this.doorknobID)) {
            return true;
        } else {
            return false;
        }
    }
}
