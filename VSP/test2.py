class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __sub__(self, other):
        sh, sm, ss = self.h, self.m, self.s
        oh, om, os = other.h, other.m, other.s
        s = ss-os
        if s < 0:
            s += 60
            sm -= 1
        m = sm-om
        if m < 0:
            m += 60
            sh -= 1
        h = sh-oh
        return Time(h, m, s)

    def __add__(self, other):
        sh, sm, ss = self.h, self.m, self.s
        oh, om, os = other.h, other.m, other.s
        s = ss+os
        if s > 59:
            s -= 60
            sm += 1
        m = sm+om
        if m > 59:
            m -= 60
            sh += 1
        h = sh+oh
        return Time(h, m, s)

    def __le__(self, other):
        if self.h < other.h:
            return True
        elif self.h == other.h:
            if self.m < other.m:
                return True
            elif self.m == other.m:
                if self.s <= other.s:
                    return True
        return False

    def __lt__(self, other):
        if self.h < other.h:
            return True
        elif self.h == other.h:
            if self.m < other.m:
                return True
            elif self.m == other.m:
                if self.s < other.s:
                    return True
        return False

    def __str__(self):
        return '{:0>2}:{:0>2}:{:0>2}'.format(self.h, self.m, self.s)


def solution(play_time, adv_time, logs):
    answer = ''
    if play_time <= adv_time:
        return '00:00:00'
    adv_time = Time(int(adv_time[0:2]), int(
        adv_time[3:5]), int(adv_time[6:8]))
    real_log = []
    play_time=Time(int(play_time[0:2]), int(
        play_time[3:5]), int(play_time[6:8]))
    for time in logs:
        start, end = time.split('-')
        start_time = Time(int(start[0:2]), int(start[3:5]), int(start[6:8]))
        end_time = Time(int(end[0:2]), int(end[3:5]), int(end[6:8]))
        real_log.append((start_time, end_time))
    # for i, j in real_log:
    #     print(i, j)
    max_adv = Time(0, 0, 0)
    real_log.sort()
    for start, end in real_log:
        stack_adv = Time(0, 0, 0)
        # print(start)
        adv_start = Time(start.h, start.m, start.s)
        adv_end = adv_start+adv_time
        for s, e in real_log:
            if adv_start <= s <= adv_end:
                if adv_end <= e:
                    # print(adv_end, s, adv_end-s)
                    stack_adv = stack_adv+(adv_end-s)
                else:
                    # print(adv_end, s, adv_end-s)
                    stack_adv = stack_adv+(e-s)
        print(stack_adv)
        if max_adv < stack_adv:
            if adv_end<=play_time:
                max_adv = Time(stack_adv.h, stack_adv.m, stack_adv.s)
                answer = '{:0>2}:{:0>2}:{:0>2}'.format(
                    adv_start.h, adv_start.m, adv_start.s)

    return answer


print(solution("02:03:55", "00:14:15", [
      "01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
