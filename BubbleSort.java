package BubbleSort;

public class BubbleSort
{
    public static void main(String[] args) {
        int [] unsortedArr = {10, -1, 34, 89, 50, -7, -189};
        int [] sortedArr = bubbleSort (unsortedArr);

        for (int i = 0; i < sortedArr.length; i++){
            System.out.println (sortedArr [i]);
        }
    }

    public static int [] bubbleSort (int [] unsortedArr){
        int unsortedIndex = unsortedArr.length - 1;
        while (unsortedIndex != 0){
            for (int i = 0; i < unsortedIndex; i++){
                if (unsortedArr [i] > unsortedArr [i + 1]){
                    int temp = unsortedArr [i];
                    unsortedArr [i] = unsortedArr [i + 1];
                    unsortedArr [i + 1] = temp;
                }
            }
            unsortedIndex --;
        }

        return unsortedArr;
    }
}

