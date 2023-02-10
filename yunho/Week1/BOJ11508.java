import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class BOJ11508 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt();
        Integer[] numList = new Integer[len];

        for (int i = 0; i < len; i++) {
            numList[i] = sc.nextInt();
        }

        Arrays.sort(numList, Collections.reverseOrder());

        int sum = 0;
        for (int i = 0; i < len; i++) {
            if (i % 3 == 2) {
                continue;
            }
            sum = sum + numList[i];
        }
        System.out.println(sum);
    }
}