import java.util.Scanner;

public class Main {
    static int N, M;
    static int[] selected;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        N = scanner.nextInt();
        M = scanner.nextInt();

        selected = new int[M];

        backtracking(1, 0);

        System.out.println(sb.toString());

        scanner.close();
    }

    static void backtracking(int start, int depth) {
        if (depth == M) {
            for (int num : selected) {
                sb.append(num).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = start; i <= N; i++) {
            selected[depth] = i;
            backtracking(i, depth + 1);
        }
    }
}
