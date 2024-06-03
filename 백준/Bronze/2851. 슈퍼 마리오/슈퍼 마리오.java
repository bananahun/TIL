import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] arr = new int[10];
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 10; i++) {
            arr[i] = sc.nextInt();
        }
        int answer = arr[0];
        for (int i = 1; i < 10; i++) {
            if (Math.abs(100 - (arr[i] + arr[i - 1])) < Math.abs(100 - arr[i])) {
                arr[i] = arr[i] + arr[i - 1];
                if (Math.abs(100 - arr[i]) <= Math.abs(100 - answer)) {
                    answer = arr[i];
                }
            }
        }
        System.out.println(answer);
    }
}
