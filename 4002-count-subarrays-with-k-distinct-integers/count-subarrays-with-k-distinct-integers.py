class Solution:
    def countSubarrays(self, nums, k, m):
        pos = defaultdict(list)
        last_m_pos = {}
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        ptr1 = 0
        ptr2 = 0
        ans = 0
        heap = []
        distinct1 = 0
        distinct2 = 0
        
        for R, val in enumerate(nums):
            pos[val].append(R)
            if len(pos[val]) >= m:
                last_m_pos[val] = pos[val][-m]
            else:
                last_m_pos[val] = -1
                
            heapq.heappush(heap, (last_m_pos[val], val))
            
            if freq1[val] == 0:
                distinct1 += 1
            freq1[val] += 1
            
            while distinct1 > k:
                left_val = nums[ptr1]
                freq1[left_val] -= 1
                if freq1[left_val] == 0:
                    distinct1 -= 1
                ptr1 += 1
                
            if freq2[val] == 0:
                distinct2 += 1
            freq2[val] += 1
            
            while distinct2 > k - 1:
                left_val = nums[ptr2]
                freq2[left_val] -= 1
                if freq2[left_val] == 0:
                    distinct2 -= 1
                ptr2 += 1
                
            while heap:
                m_pos, x = heap[0]
                if freq1[x] == 0:
                    heapq.heappop(heap)
                elif m_pos != last_m_pos[x]:
                    heapq.heappop(heap)
                else:
                    break
                    
            if distinct1 == k:
                M = heap[0][0] if heap else -1
                valid_left_max = min(ptr2 - 1, M)
                if valid_left_max >= ptr1:
                    ans += valid_left_max - ptr1 + 1
                    
        return ans
        """
        :type nums: List[int]
        :type k: int
        :type m: int
        :rtype: int
        """
        