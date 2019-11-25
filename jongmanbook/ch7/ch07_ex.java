package com.milkyway.jongman;

import java.util.List;
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
	
	public static ArrayList<Integer> addTo(ArrayList<Integer> a, ArrayList<Integer> b, int k) {
		// a+= b*(10^k);를 구현
		return a;
	}

	public static ArrayList<Integer> subFrom(ArrayList<Integer> a, ArrayList<Integer> b) {
		// a-= b;를 구현. a>=b를 가정
		return a;
	}
	
	// 두 긴 정수의 곱을 반환.
	public static ArrayList<Integer> karatsuba(ArrayList<Integer> a, ArrayList<Integer> b) {
		int an = a.size();
		int bn = b.size();
		// a가 b보다 짧을 경우 둘을 바꾼다.
		if(an < bn) return karatsuba(b, a);
		// 기저 사례 : a나 b가 비어 있는 경우
		if(an == 0 || bn == 0) return new ArrayList<Integer>();
		// 기저 사례: a가 비교적 짧은 경우 O(n^2) 곱셈으로 변경.
		if (an <= 50) return multiply(a, b);
		int half = an / 2;
		// a와 b를 밑에서 half 자리와 나머지로 분리한다.
		ArrayList<Integer> a0 = new ArrayList(a.subList(0, half));
		ArrayList<Integer> a1 = new ArrayList(a.subList(half, a.size()));
		ArrayList<Integer> b0 = new ArrayList(b.subList(0, Math.min(b.size(), half)));
		ArrayList<Integer> b1 = new ArrayList(b.subList(Math.min(b.size(), half), b.size()));
 		// z2 = a1*b1
		ArrayList<Integer> z2 = karatsuba(a1, b1);
		// z0 = a0*b0
		ArrayList<Integer> z0 = karatsuba(a0, b0);
		// a0 = a0+a1, b0 = b0+b1
		a0 = addTo(a0, a1, 0);
		b0 = addTo(b0, b1, 0);
		// z1 = (z0*b0) - z0 - z2;
		ArrayList<Integer> z1 = karatsuba(a0, b0);
		z1 = subFrom(z1, z0);
		z1 = subFrom(z1, z2);
		// ret = z0 + z1 * 10^half + z2 * 10^(half*2)
		ArrayList<Integer> ret = new ArrayList<Integer>();
		ret = addTo(ret, z0, 0);
		ret = addTo(ret, z1, half);
		ret = addTo(ret, z2, half + half);
		return ret;
	}
	

}
