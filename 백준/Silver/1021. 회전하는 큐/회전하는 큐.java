import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int M = scanner.nextInt();

        Deque<Integer> deque = new ArrayDeque<>();
        int count = 0;

        for (int i = 1; i <= N; i++)
            deque.add(i);

        for (int i = 0; i < M; i++) {
            int target = scanner.nextInt();
            int leftDistance = 0;

            while (deque.peekFirst() != target) {
                deque.addLast(deque.pollFirst());
                leftDistance++;
            }

            int rightDistance = deque.size() - leftDistance;

            count += Math.min(leftDistance, rightDistance);
            deque.pollFirst();
        }

        System.out.println(count);
        scanner.close();
    }
}
