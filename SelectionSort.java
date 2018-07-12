package SelectionSort;

public class SelectionSort
{
    public static void main(String[] args) {
        int [] unsortedArr = {10, -1, 34, 89, 50, -7, -189};
        int [] sortedArr = selectionSort (unsortedArr);

        for (int i = 0; i < sortedArr.length; i++){
            System.out.println (sortedArr [i]);
        }
    }

    public static int [] selectionSort (int [] unsortedArr){
        int unsortedIndex = unsortedArr.length - 1;
        while (unsortedIndex != 0){
            int maxVal = unsortedArr [0], index = 0;
            for (int i = 1; i <= unsortedIndex; i ++){
                if (unsortedArr [i] > maxVal){
                        index = i;
                        maxVal = unsortedArr [i];
                }
            }
            int temp = unsortedArr [unsortedIndex];
            unsortedArr [unsortedIndex] = maxVal;
            unsortedArr [index] = temp;
            unsortedIndex --;
        }
        return unsortedArr;
    }
}
