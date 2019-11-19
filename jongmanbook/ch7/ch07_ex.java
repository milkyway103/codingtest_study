package com.milkyway.jongman;

import java.util.ArrayList;

public class ch07_ex {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		ArrayList<Integer> nums = new ArrayList<Integer>();
		nums.add(3);
		nums.add(2);
		nums.add(1);
		
		System.out.println(multiply(nums, nums).toString());

	}
	
	// 필수 조건 : n은 자연수
	// 1+2+...n을 반환한다.
	public static int fastSum(int n) {
		// 기저 사례
		if(n==1) return 1;
		// n이 홀수인 경우에는 짝수인 n-1까지의 합을 재귀 호출로 계산하고 n을 더해 답을 구한다.
		if(n%2 == 1) return fastSum(n-1)+n;
		return 2*fastSum(n/2) + (n/2)*(n/2);
	}
	
	// 코드 7.3 두 큰 수를 구하는 O(n^2) 시간 알고리즘
	// num[]의 자릿수 올림을 처리
	public static ArrayList<Integer> normalize(ArrayList<Integer> num) {
		num.add(0);
		// 자릿수 올림 처리
		for (int i = 0 ; i+1 < num.size(); ++i) {
			if(num.get(i) < 0) {
				int borrow = (Math.abs(num.get(i)) + 9) / 10;
				num.set(i+1, num.get(i+1) - borrow);
				num.set(i, num.get(i) + borrow*10);
			}
			else { 
				num.set(i+1, num.get(i+1) + (num.get(i) / 10));
				num.set(i, num.get(i) % 10);
			}
		}
		while(num.size() > 1 && num.get(num.size()-1) == 0) num.remove(num.size()-1);
		
		return num;
	}
	// 두 긴 자연수의 곱을 반환한다.
	// 각 배열에는 각 수의자릿수가 1의 자리에서부터 시작해 저장되어 있다.
	// 예: multiply([3, 2, 1], [6, 5, 4]) = 123*456 = 56088 = [8, 8, 0, 6, 5]
	public static ArrayList<Integer> multiply(ArrayList<Integer> a, ArrayList<Integer> b) {
		ArrayList<Integer> c = new ArrayList<Integer>();
		for (int i = 0; i < a.size() + b.size(); i++) {
			c.add(0);
		}
		for (int i = 0; i < a.size(); ++i) {
			for (int j = 0; j <  b.size(); ++j) {
				c.set(i+j, c.get(i+j) + a.get(i)*b.get(j));
			}
		}
		c = normalize(c);
		return c;
	}
	

}
