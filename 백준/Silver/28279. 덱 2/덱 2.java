import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());

            switch (command) {
                case 1: // 정수 X를 덱의 앞에 넣는다.
                    int X = Integer.parseInt(st.nextToken());
                    deque.addFirst(X);
                    break;
                case 2: // 정수 X를 덱의 뒤에 넣는다.
                    X = Integer.parseInt(st.nextToken());
                    deque.addLast(X);
                    break;
                case 3: // 맨 앞의 정수를 빼고 출력한다.
                    if (!deque.isEmpty()) {
                        System.out.println(deque.pollFirst());
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case 4: // 맨 뒤의 정수를 빼고 출력한다.
                    if (!deque.isEmpty()) {
                        System.out.println(deque.pollLast());
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case 5: // 덱에 들어있는 정수의 개수를 출력한다.
                    System.out.println(deque.size());
                    break;
                case 6: // 덱이 비어있으면 1, 아니면 0을 출력한다.
                    if (deque.isEmpty()) {
                        System.out.println(1);
                    } else {
                        System.out.println(0);
                    }
                    break;
                case 7: // 맨 앞의 정수를 출력한다.
                    if (!deque.isEmpty()) {
                        System.out.println(deque.peekFirst());
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case 8: // 맨 뒤의 정수를 출력한다.
                    if (!deque.isEmpty()) {
                        System.out.println(deque.peekLast());
                    } else {
                        System.out.println(-1);
                    }
                    break;
            }
        }

        br.close();
    }
}
