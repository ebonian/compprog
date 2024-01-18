public abstract class PythonList {
    protected int[] array;
    private FindMinMaxStrategy findMinMaxStrategy;

    public abstract void append(int v);

    public PythonList(int[] array) {
        this.array = array;
    }

    public void setFindMinMaxStrategy(FindMinMaxStrategy findMinMaxStrategy) {
        this.findMinMaxStrategy = findMinMaxStrategy;
    }

    public void sort() {
        for (int lastIndex = array.length - 1; lastIndex >= 1; lastIndex--) {
            for (int i = 0; i < lastIndex; i++) {
                if (array[i] > array[i + 1]) {
                    int temp = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = temp;
                }
            }
        }
    }

    public int findMin() {
        return findMinMaxStrategy.findMin(array);
    }

    public int findMax() {
        return findMinMaxStrategy.findMax(array);
    }

    public boolean contains(int v) {
        for (int a : array) {
            if (a == v)
                return true;
        }
        return false;
    }

    public String toString() {
        if (array.length == 0)
            return "[]";
        String out = "[";
        for (int a : array) {
            out += a + ", ";
        }
        out = out.substring(0, out.length() - 2) + "]";
        return out;
    }
}

class SortedList extends PythonList {
    public SortedList(int[] array) {
        super(array);
        sort();
        setFindMinMaxStrategy(new SortedFindMinMaxStrategy());
    }

    public void append(int v) {
        int[] a = new int[array.length + 1];
        int i = 0;
        while (v > array[i]) {
            a[i] = array[i];
            i++;
        }
        a[i++] = v;
        for (int j = i - 1; j < array.length; j++) {
            a[i++] = array[j];
        }
        array = a;
    }

    @Override
    public boolean contains(int v) {
        int left = 0;
        int right = array.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;

            // If the middle element is equal to v, return true
            if (array[mid] == v) {
                return true;
            }

            // If v is less than the middle element, search in the left half
            if (array[mid] > v) {
                right = mid - 1;
            }
            // If v is greater than the middle element, search in the right half
            else {
                left = mid + 1;
            }
        }

        // If the loop finishes without finding v, return false
        return false;
    }
}

class UnsortedList extends PythonList {
    public UnsortedList(int[] array) {
        super(array);
        setFindMinMaxStrategy(new UnsortedFindMinMaxStrategy());
    }

    public void append(int v) {
        int[] a = new int[array.length + 1];
        for (int i = 0; i < array.length; i++) {
            a[i] = array[i];
        }
        a[array.length] = v;
        array = a;
    }
}
