import java.io.*;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            String[] words = str.split(" "); // 공백 기준으로 단어 분리
            char[] n_str = new char[20];
            int index;

            for (int j = 0; j < words.length; j++) {
                index = 0;
                for (int k = words[j].length() - 1; k >= 0; k--)
                    n_str[index++] = words[j].charAt(k);
                bw.write(String.valueOf(n_str, 0, index));
                n_str = new char[20]; // n_str 초기화
                if (j != words.length - 1) // 마지막 단어가 아니라면 공백 추가
                    bw.write(" ");
            }
            if (i < n - 1) // 마지막 문장이 아니라면 개행 추가
                bw.newLine();
        }
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
 * 출력오류 코드
 * BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 * BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
 * 
 * int n = Integer.parseInt(br.readLine());
 * for (int i = 0; i < n; i++) {
 * String str = br.readLine();
 * char[] n_str = new char[str.length()];
 * int index = 0;
 * 
 * for (int j = 0; j < str.length() - 1; j++) { // 문자열의 길이만큼 반복
 * int k = j;
 * if (str.charAt(j) == ' ' && str.charAt(j) != '\n') { // 공백인 경우 버퍼에 저장, n_str
 * 초기화
 * bw.write(String.valueOf(n_str, 0, index) + " ");
 * n_str = new char[str.length()];
 * } else { // 문자인 경우
 * while (k < str.length() && str.charAt(k) != ' ')
 * k++; // 이때 k는 단어의 index
 * j = --k; // j를 k(단어의 index)로 설정
 * while (k != -1 && str.charAt(k) != ' ') { // 공백을 만날 때까지 n_str에 str의 문자 토큰을
 * 거꾸로 하나씩 추가
 * n_str[index++] = str.charAt(k--);
 * }
 * }
 * }
 * bw.write(String.valueOf(n_str, 0, index)); // 마지막 단어 추가
 * if (i < n - 1)
 * bw.newLine(); // 마지막 문장이 아니면, 개행 추가
 * }
 * bw.flush();
 * bw.close();
 * br.close();
 */