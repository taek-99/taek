package boj1978;

import java.util.Scanner;

public class Main {
	
	static boolean isPrime(int x) {
		if(x < 2) return false;
		
		for(int i = 2; i * i <= x; i++) {
			if(x % i == 0) return false;
		}
		return true;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] num = new int[n];

		for(int i = 0 ; i < n; i++) {
			num[i] = sc.nextInt();
		}
		
		int cnt = 0;
		
		for (int x : num) {
			if (isPrime(x)) {
				cnt++;
			}		

	}
	
		System.out.println(cnt);
		sc.close();	
	}
	
}
