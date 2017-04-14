import java.util.PriorityQueue;
import java.util.Collections;
import java.util.Scanner;
public class Bathroom {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int times = Integer.parseInt(sc.nextLine());

        for (int i = 1; i <= times; i++) {
            String[] tupleLine = sc.nextLine().split(" ");

            int stalls = Integer.parseInt(tupleLine[0]);
            int people = Integer.parseInt(tupleLine[1]);

            int max = stalls;
            int min = stalls;
            
            PriorityQueue<Integer> bath = new PriorityQueue<Integer>(1, Collections.reverseOrder());
            
            bath.offer(stalls);

            for (int j = 1; j <= people; j++) {
                int temp = bath.poll();
                max = temp / 2;
                min = temp % 2 == 0 ? temp / 2 - 1 : temp / 2;

             bath.offer(max);
             bath.offer(min);
            }

            System.out.println("Case #" + i + ": " + max + " " + min);
        }
    }
}