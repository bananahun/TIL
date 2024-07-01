import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        sc.close();
        
        int n = s.length();
        int[] leftCount = new int[n];
        
        // Step 1: Count `((` patterns
        for (int i = 1; i < n; i++) {
            leftCount[i] = leftCount[i - 1];
            if (s.charAt(i - 1) == '(' && s.charAt(i) == '(') {
                leftCount[i]++;
            }
        }
        
        int totalCount = 0;
        
        // Step 2: Count `))` patterns and calculate the pairs
        for (int i = 1; i < n; i++) {
            if (s.charAt(i - 1) == ')' && s.charAt(i) == ')') {
                totalCount += leftCount[i];
            }
        }
        
        System.out.println(totalCount);
    }
}
