package boj2609;

import java.util.Scanner;

public class main {
	
	static int gcd(int a, int b) {
		while( b!= 0) {
			int r = a % b;
			a = b;
			b = r;
		}
		return a;
	}
	
	
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		int g = gcd(a, b);
		int l = (a * b)/ g;
		
		
		System.out.println(g);
		System.out.println(l);
	}
}
