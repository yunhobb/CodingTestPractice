import java.util.*;
import java.io.*;

public class BOJ11652 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        long card[] = new long[N];

        for (int i = 0; i < N; i++) {
            card[i] = Long.parseLong(br.readLine());
        }
        Arrays.sort(card);
        int cnt = 1, max = 1, maxIdx = 0;
        for (int i = 1; i < N; i++) {
            if (card[i] == card[i - 1]) {
                cnt++;
            } else {
                cnt = 1;
            }

            if (cnt > max) {
                max = cnt;
                maxIdx = i;
            }
        }
        br.close();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(card[maxIdx] + "\n");
        bw.flush();
        bw.close();
    }

}
