package inserctionsort;
import java.util.Arrays;
public class InserctionSort {

	    public static void insertionSort(int[] listToSort) {
	        for (int i = 1; i < listToSort.length; i++) {
	            System.out.println("\ni = " + i);
	            for (int j = i; j > 0; j--) {
	                if (listToSort[j] < listToSort[j - 1]) {
	                    swap(listToSort, j, j - 1);
	                    System.out.print("Swapping: " + j + " and " + (j - 1) + " ");
	                    System.out.println(Arrays.toString(listToSort));
	                } else {
	                    break;
	                }
	            }
	        }
	    }

	    public static void swap(int[] arr, int i, int j) {
	        int temp = arr[i];
	        arr[i] = arr[j];
	        arr[j] = temp;
	    }

	    public static void main(String[] args) {
	        int[] arr = {5, 3, 8, 1, 2, 7};
	        insertionSort(arr);
	        System.out.println(Arrays.toString(arr));
	    }
	}



