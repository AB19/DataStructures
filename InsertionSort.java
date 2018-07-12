package InsertionSort;

public class InsertionSort
{
    public static void main(String[] args) {
        int [] unsortedArr = {10, -1, 34, 89, 50, -7, -189};
        int [] sortedArr = insertionSort (unsortedArr);

        for (int i = 0; i < sortedArr.length; i++){
            System.out.println (sortedArr [i]);
        }
    }

    public static int [] insertionSort (int [] unsortedArr){
        for (int sortedIndex = 1; sortedIndex < unsortedArr.length; sortedIndex++){
            for (int i = sortedIndex; i > 0; i--){
                if (unsortedArr [i] < unsortedArr [i - 1]){
                    int temp = unsortedArr [i];
                    unsortedArr [i] = unsortedArr [i - 1];
                    unsortedArr [i - 1] = temp;
                }

                else
                    break;
            }
        }

        return unsortedArr;
    }
}