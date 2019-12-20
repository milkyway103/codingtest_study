package com.milkyway.jongman;

import java.util.Scanner;

public class bruteforte6_1 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		int ret = 0;
		for (int idx=1 ; idx<=n ; idx++) {
			ret += idx;
		}

	}
	
	public static int sum(int n) {
		if (n == 0) {
			return 0;
		}
		else {
			return n + sum(n-1);
		}
	}

}
