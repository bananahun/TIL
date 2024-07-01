import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.nextLine();
        System.out.println(reverse(S));
        sc.close();
    }

    public static String reverse(String S) {
        StringBuilder result = new StringBuilder();
        int i = 0;
        int n = S.length();
        
        while (i < n) {
            if (S.charAt(i) == '<') {
                // 태그 시작, 그대로 result에 추가
                int j = i;
                while (j < n && S.charAt(j) != '>') {
                    j++;
                }
                j++; // '>' 포함
                result.append(S.substring(i, j));
                i = j;
            } else if (Character.isLetterOrDigit(S.charAt(i))) {
                // 단어 시작, 단어를 뒤집어서 result에 추가
                int j = i;
                while (j < n && Character.isLetterOrDigit(S.charAt(j))) {
                    j++;
                }
                result.append(new StringBuilder(S.substring(i, j)).reverse());
                i = j;
            } else {
                // 공백 그대로 result에 추가
                result.append(S.charAt(i));
                i++;
            }
        }
        
        return result.toString();
    }
}

