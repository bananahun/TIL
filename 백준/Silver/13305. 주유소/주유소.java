import java.util.Scanner;

public class Main {
	public static void main (String[] args) {
		Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt(); // 도시의 개수
        int[] distances = new int[N - 1]; // 도로의 길이
        int[] prices = new int[N]; // 주유소의 리터당 가격

        // 도로의 길이 입력
        for (int i = 0; i < N - 1; i++) {
            distances[i] = scanner.nextInt();
        }

        // 주유소의 리터당 가격 입력
        for (int i = 0; i < N; i++) {
            prices[i] = scanner.nextInt();
        }

        long totalCost = 0; // 총 비용
        int minPrice = prices[0]; // 최소 가격
        for (int i = 0; i < N - 1; i++) {
            minPrice = Math.min(minPrice, prices[i]); // 이전 도시까지의 최소 가격 업데이트
            totalCost += (long) minPrice * distances[i]; // 주유소 선택 후 이동 비용 계산
        }

        System.out.println(totalCost);
        scanner.close();
    
	}
}
