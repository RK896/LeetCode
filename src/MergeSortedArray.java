import java.util.Arrays;
import java.util.Collections;

public class MergeSortedArray {

    public static void main(String[] args) {
        int[] nums1 = {1,2,3,0,0,0};
        int[] nums2 = {2,5,6};
        merge(nums1, 3, nums2, 3);
    }

    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = 0; i < nums2.length; i++) {
            nums1[m+i] = nums2[i];
        }
        Arrays.sort(nums1);
        Collections.reverse(Arrays.asList(nums1));
        System.out.println(Arrays.toString(nums1));
    }
}
