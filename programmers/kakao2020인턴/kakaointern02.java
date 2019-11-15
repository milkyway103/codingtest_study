package com.kakaointern2020;

import java.util.ArrayList;

public class kakaointern02 {

	public static void main(String[] args) {
		solution("{{2},{2,1},{2,1,3},{2,1,3,4}}");

	}
	
	public static int[] solution(String s) {
		int[] answer;
		s = s.substring(2, s.length()-2);
		String[] input;
		input = s.split("\\}\\,\\{");
		ArrayList<Integer[]> sets = new ArrayList<Integer[]>();
		for(int idx=0 ; idx<input.length ; idx++) {
			String[] temp;
			temp = input[idx].split(",");
			Integer[] tempset = new Integer[temp.length];
			for(int jdx=0 ; jdx<temp.length ; jdx++) {
				tempset[jdx] = Integer.parseInt(temp[jdx]);
			}
			sets.add(tempset);
			
		}
		
		answer = new int[sets.size()];
		int cur = 1;
		while(!sets.isEmpty()) {
			int thisint = -1;
			Integer[] thisset;
			for(int idx=0 ; idx<sets.size(); idx++) {
				if(sets.get(idx).length == cur) {
					thisint = idx;
					break;
				}
			}
			thisset = sets.get(thisint);
			answer[cur-1] = thisset[thisset.length - 1];
			sets.remove(thisint);
			cur++;
			
		}
		for(int idx=0 ; idx<answer.length ; idx++) {
			System.out.println(answer[idx]);
		}
		return answer;
	}
	

}
