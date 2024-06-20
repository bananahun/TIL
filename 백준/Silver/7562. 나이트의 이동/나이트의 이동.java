import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main { // 클래스 이름을 Main으로 변경해야 합니다.

    // 나이트가 움직이는 경우를 모두 정해 보겠습니다.
    static int[] dx = {1, 1, -1, -1, 2, 2, -2, -2};
    static int[] dy = {2, -2, 2, -2, 1, -1, 1, -1};

    public static int bfs(int sx, int sy, int ex, int ey, int size) {
        int[][] visited = new int[size][size]; // 방문 여부를 기록하는 배열
        Queue<int[]> queue = new LinkedList<>(); // BFS를 위한 큐
        queue.add(new int[]{sx, sy}); // 시작 위치를 큐에 추가
        visited[sx][sy] = 1; // 시작 위치 방문 표시

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];

            if (x == ex && y == ey) {
                return visited[x][y] - 1; // 목적지에 도달하면 이동 횟수 반환
            }

            for (int i = 0; i < 8; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && ny >= 0 && nx < size && ny < size && visited[nx][ny] == 0) {
                    visited[nx][ny] = visited[x][y] + 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        }

        return -1; // 목적지에 도달할 수 없는 경우
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt(); // 테스트 케이스의 수

        for (int t = 0; t < T; t++) {
            int size = scanner.nextInt(); // 체스판의 크기
            int sx = scanner.nextInt(); // 시작 x 좌표
            int sy = scanner.nextInt(); // 시작 y 좌표
            int ex = scanner.nextInt(); // 종료 x 좌표
            int ey = scanner.nextInt(); // 종료 y 좌표

            int result = bfs(sx, sy, ex, ey, size);
            System.out.println(result); // 결과 출력
        }

        scanner.close();
    }
}
