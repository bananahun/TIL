import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        
        // 최대 힙 구현을 위해 PriorityQueue를 사용
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            if (x == 0) {
                if (maxHeap.isEmpty()) {
                    sb.append(0).append("\n");
                } else {
                    sb.append(maxHeap.poll()).append("\n");
                }
            } else {
                maxHeap.add(x);
            }
        }
        
        System.out.print(sb.toString());
        sc.close();
    }
}
