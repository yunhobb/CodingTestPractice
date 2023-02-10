import java.util.Scanner;

public class BOJ14916 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int count = 0;

        while (n > 0) {
            if (n % 5 == 0) {
                count = count + n / 5;
                break;
            }
            n = n - 2;
            count = count + 1;
        }
        if (n < 0) {
            System.out.println(-1);
        }
        if (n >= 0) {
            System.out.println(count);
        }
    }
}