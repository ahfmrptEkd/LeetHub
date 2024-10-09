from itertools import chain, zip_longest

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        l = 0 # index
        res = []
        

        while l < len(words):
            length = maxWidth   # 남은 공간
            container = []  # 초기화
            line_length = 0

            # 현재 라인 단어 추가
            while l < len(words) and length >= len(words[l]):         
                container.append(words[l])
                length -= len(words[l]) + 1 # (단어, 공백)
                line_length += len(words[l])
                l += 1

            # 단어가 1개 또는 마지막 줄 => 왼쪽 정렬
            if l == len(words) or len(container) == 1:
                line = " ".join(container).ljust(maxWidth) 
                res.append(line)
            else:
                # pad_length 가 홀 수 인 경우 처리가 필요.
                pad_count = len(container) - 1
                total_pad = maxWidth - line_length
                
                base_pad = total_pad // pad_count
                extra_pad = total_pad % pad_count
                
                ### -> 1
                # pads = [" " * base_pad for _ in range(pad_count)]

                # # 홀 수 인 경우
                # if extra_pad:
                #     for i in range(extra_pad):
                #         pads[i] += " "
                ###
                ### -> 2
                pads = [" " * (base_pad + (1 if i < extra_pad else 0)) for i in range(pad_count)]

                #line = list(chain(*zip(container, pads + [''])))[:-1]
                line = list(chain(*zip_longest(container, pads, fillvalue='')))
                line_str = "".join(line)
                res.append(line_str)
        
        return res


    
