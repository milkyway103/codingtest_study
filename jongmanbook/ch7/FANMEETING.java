package com.milkyway.jongman;

import java.util.ArrayList;

public class FANMEETING {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public static int hugs(String members, String fans) {
		
		String strA = members.replace('F', '0').replace('M', '1');
		String strB = fans.replace('F', '0').replace('M', '1');
		
		if (strA.length() > strB.length()) {
			String temp = "";
			temp = strA;
			strA = strB;
			strB = temp;
		}
		
		int A = Integer.parseInt(strA, 2);
		int B = Integer.parseInt(strB, 2);
		
		int result = 0;
		
		for(int i=0 ; i < strB.length() - strA.length() + 1 ; i++) {
			if ((A&B) == 0) {
				result += 1;
			}
			B = (B>>1);
		}
		
		return result;
		
	}

}
