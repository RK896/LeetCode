import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class IntersectionOf2Arrays {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(intersect(new int[]{1, 2, 2, 1}, new int[]{2, 2})));
    }

    public static int[] intersect(int[] nums1, int[] nums2) {
        List<Integer> numbers = new ArrayList<>();


        for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                if (nums1[i] == nums2[j]) {
                    numbers.add(nums2[j]);
                    nums2[j] = Integer.MIN_VALUE;
                    break;
                }
            }

        }

        int[] out = new int[numbers.size()];
        for (int i = 0; i < numbers.size(); i++) {
            out[i] = numbers.get(i);
        }
        return out;
    }
}
