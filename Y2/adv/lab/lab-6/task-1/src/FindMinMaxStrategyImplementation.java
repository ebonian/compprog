import java.util.NoSuchElementException;

class UnsortedFindMinMaxStrategy implements FindMinMaxStrategy {

    @Override
    public int findMin(int[] array) {
        if (array.length == 0)
            throw new NoSuchElementException("No element in array");
        int min = Integer.MAX_VALUE;
        for (int a : array) {
            if (a < min)
                min = a;
        }
        return min;
    }

    @Override
    public int findMax(int[] array) {
        if (array.length == 0)
            throw new NoSuchElementException("No element in array");
        int max = Integer.MIN_VALUE;
        for (int a : array) {
            if (a > max)
                max = a;
        }
        return max;
    }

}

class SortedFindMinMaxStrategy implements FindMinMaxStrategy {
    @Override
    public int findMin(int[] array) {
        if (array.length == 0)
            throw new NoSuchElementException("No element in array");
        return array[0];
    }

    @Override
    public int findMax(int[] array) {
        if (array.length == 0)
            throw new NoSuchElementException("No element in array");
        return array[array.length - 1];
    }
}