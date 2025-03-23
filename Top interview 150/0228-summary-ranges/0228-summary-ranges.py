class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 결과를 저장할 리스트 초기화
        result = []
        # 현재 검사 중인 숫자의 인덱스
        i = 0
        
        # 배열의 모든 숫자를 검사
        while i < len(nums):
            # 현재 범위의 시작 숫자를 저장
            start = nums[i]
            
            # 연속된 숫자를 찾기 위해 다음 숫자 검사
            # i + 1이 배열 범위 내에 있고, 현재 숫자+1이 다음 숫자와 같으면 계속 진행
            while i + 1 < len(nums) and (nums[i] + 1 == nums[i+1]):
                i += 1
            
            # 시작 숫자와 현재 숫자가 다르다면 범위가 존재하는 것
            if start != nums[i]:
                # "시작->끝" 형태의 문자열로 범위를 저장 (예: "1->3")
                result.append(str(start) + "->" + str(nums[i]))
            else:
                # 시작 숫자와 현재 숫자가 같다면 단일 숫자이므로
                # 숫자만 문자열로 저장 (예: "1")
                result.append(str(nums[i]))
            
            # 다음 숫자 검사를 위해 인덱스 증가
            i += 1
        
        return result