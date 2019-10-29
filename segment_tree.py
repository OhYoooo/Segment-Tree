class SegmentTree:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum_value = {}
        self.length = {}
        self._init(start, end)


    def _init(self, start, end):
        self.sum_value[(start, end)] = 0
        self.length[(start, end)] = 0
        if start < end:
            mid = start + (end - start)//2
            self._init(start, mid)
            self._init(mid+1, end)


    def _add(self, start, end, weight, total_start, total_end):
        key = (total_start, total_end)
        if total_start == total_end:
            self.sum_value[key] += weight
            self.length[key] = 1 if self.sum_value[key] != 0 else 0
            return
        mid = self.start + (self.end - self.start)//2
        # if segment is on the left hand side of mid point
        if mid >= end:
            self._add(start, end, weight, total_start, mid)
        # if segment is on the right hand side of mid point
        elif mid < start:
            self._add(start, end, weight, mid+1, total_end)
        # if segment cross over the mid point
        else:
            self._add(start, mid, weight, total_start, mid)
            self._add(mid+1, end, weight, mid+1, total_end)
        self.sum_value[key] = self.sum_value[(total_start, mid)] + self.sum_value[(mid+1, total_end)]
        self.length[key] = self.length[(total_start, mid)] + self.length[(mid+1, total_end)]


    def _find_sum(self, start, end, total_start, total_end):
        if start == total_start and end == total_end:
            return self.sum_value([start, end])
        mid = total_start + (total_end - total_end)//2
        # if segment is on the left hand side of mid point
        if mid >= end:
            return self._find_sum(start, end, total_start, mid)
        # if segment is on the right hand side of mid point
        if mid < start:
            return self._find_sum(start, end, mid+1, total_end)
        # if segment cross over the mid point
        return self._find_sum(start, mid, total_start, mid) + self._find_sum(mid+1, end, mid+1, total_end)


    def _find_length(self, start, end, total_start, total_end):
        if start == total_start and end == total_end:
            return self.length([start, end])
        mid = total_start + (total_end - total_end)//2
        if mid >= end:
            return self._find_length(start, end, total_start, mid)
        if mid < start:
            return self._find_length(start, end, mid+1, total_end)
        return self._find_length(start, mid, total_start, mid) + self._find_length(mid+1, end, mid+1, total_end)


    def check_bound(self, start, end):
        _start = max(self.start, start)
        _end = min(self.end, end)
        if _start > _end:
            return None, None
        return _start, _end


    def add(self, start, end, weight = 1):
        _start, _end = self.check_bound(start, end)
        if _start == None:
            return False
        self._add(_start, _end, weight, self.start, self.end)
        return True


    def find_sum(self, start, end):
        _start, _end = self.check_bound(start, end)
        if _start == None:
            return 0
        return self._find_sum(_start, _end, self.start, self.end)


    def find_covered_length(self, start, end):
         _start, _end = self.check_bound(start, end)
        if _start == None:
            return 0
        return self._find_length(_start, _end, self.start, self.end)
