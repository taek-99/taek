package boj2869;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		
        int A = sc.nextInt();
        int B = sc.nextInt();
        int V = sc.nextInt();

        int day = (V - B - 1) / (A - B) + 1;
        System.out.println(day);
	}
}
