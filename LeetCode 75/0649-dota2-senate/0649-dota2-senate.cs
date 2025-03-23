public class Solution {
    public string PredictPartyVictory(string senate) {
        // 각 진영의 상원의원 큐 생성 (인덱스 저장)
        Queue<int> rQueue = new Queue<int>();  // Radiant 큐
        Queue<int> dQueue = new Queue<int>();  // Dire 큐
        
        // 각 상원의원의 초기 위치를 큐에 저장
        for (int i = 0; i < senate.Length; i++) {
            if (senate[i] == 'R') {
                rQueue.Enqueue(i);
            } else {
                dQueue.Enqueue(i);
            }
        }
        
        int n = senate.Length;  // 전체 상원의원 수
        
        // 한 진영이 전멸할 때까지 반복
        while (rQueue.Count > 0 && dQueue.Count > 0) {
            int rIdx = rQueue.Dequeue();  // Radiant 상원의원
            int dIdx = dQueue.Dequeue();  // Dire 상원의원
            
            // 인덱스가 작은 상원의원이 먼저 행동
            if (rIdx < dIdx) {
                // Radiant 상원의원이 Dire를 금지하고 다음 라운드로
                rQueue.Enqueue(rIdx + n);
            } else {
                // Dire 상원의원이 Radiant를 금지하고 다음 라운드로
                dQueue.Enqueue(dIdx + n);
            }
        }
        
        // 남아있는 진영이 승리
        return rQueue.Count > 0 ? "Radiant" : "Dire";
    }
}