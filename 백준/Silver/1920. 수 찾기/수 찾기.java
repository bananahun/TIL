import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

        // 배열의 크기와 배열 입력 받기
        int N = scanner.nextInt();
        int[] array = new int[N];
        for (int i = 0; i < N; i++) {
            array[i] = scanner.nextInt();
        }

        // 배열 정렬
        Arrays.sort(array);

        // 찾고자 하는 숫자의 개수와 해당 숫자들 입력 받기
        int M = scanner.nextInt();
        int[] targets = new int[M];
        for (int i = 0; i < M; i++) {
            targets[i] = scanner.nextInt();
        }

        // 각 숫자에 대해 이진 탐색 수행하여 결과 출력
        for (int i = 0; i < M; i++) {
            if (binarySearch(array, targets[i])) {
                System.out.println(1); // 존재하면 1 출력
            } else {
                System.out.println(0); // 존재하지 않으면 0 출력
            }
        }

        scanner.close();
    }

    // 이진 탐색 구현
    public static boolean binarySearch(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (array[mid] == target) {
                return true;
            } else if (array[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
	}
}
