package com.kakaointern2020;

import java.util.ArrayList;

public class kakaointern03 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	static int N;
	static ArrayList<ArrayList<Integer>> cand = new ArrayList<ArrayList<Integer>>();
	
	public static int solution(String[] user_id, String[] banned_id) {
		int answer = 0;
		ArrayList<ArrayList<Integer>> banned_dict = new ArrayList<ArrayList<Integer>>();
		for (int ban=0 ; ban<banned_id.length ; ban++) {
			String banid = banned_id[ban];
			ArrayList<Integer> newban = new ArrayList<Integer>();
			for (int user=0 ; user<user_id.length ; user++) {
				String userid = user_id[user];
				if(userid.length() != banid.length()) continue;
				boolean ismatched = true;
				for (int pos=0 ; pos<banid.length() ; pos++) {
					if(banid.charAt(pos)=='*') continue;
					if(banid.charAt(pos)!=userid.charAt(pos)) {
						ismatched = false;
						break;
					}
				}
				if(ismatched) {
					newban.add(user);
				}
			}
			
			N = banned_id.length;
			matching(banned_dict, 0, new ArrayList<Integer>());
			answer = cand.size();
			return answer;
			
		}
		
		// temp라는 int[banned_id.length]를 만들고 answerlis(ArrayList)에 계속 추가시켜나감 (이떄 sort)
		// 단 중복된 리스트라면 추가하지 않는다.
		
		
		return answer;
	}
	
	public static void matching(ArrayList<ArrayList<Integer>> banned_dict, int next_ban, ArrayList<Integer> check) {
		if(next_ban == N) {
			check.sort(null);
			if(!cand.contains(check)) {
				cand.add((ArrayList<Integer>) check.clone());
				return;
			}
		}
		for(int user : banned_dict.get(next_ban)) {
			if(!check.contains(user)) {
				check.add(user);
				matching(banned_dict, next_ban+1, check);
				check.remove(check.size() -1);
			}
		}
	}

}
