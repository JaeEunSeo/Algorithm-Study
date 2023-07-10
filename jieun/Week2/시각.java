package jieun.Week2;

import java.io.*;

public class 시각 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int count = 0;

        for (int a = 0; a <= n; a++) {
            if (a % 10 == 3) {
                count += 3600;
                continue;
            }
            for (int b = 0; b < 60; b++) {
                if (b % 10 == 3 || (b >= 30 && b <= 39)) {
                    count += 60;
                    continue;
                }
                for (int c = 0; c < 60; c++) {
                    if (c % 10 == 3 || (c >= 30 && c <= 39)) {
                        count += 1;
                    }
                }
            }
        }
        bw.write(Integer.toString(count));
        bw.flush();
        bw.close();
        br.close();
    }
}
