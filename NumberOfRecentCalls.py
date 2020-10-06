#    You have a RecentCounter class which counts the number of recent
#    requests within a certain time frame.
#
#    Implement the RecentCounter class:
#
#    RecentCounter() Initializes the counter with zero recent requests.
#    int ping(int t) Adds a new request at time t, where t represents some
#    time in milliseconds, and returns the number of requests that
#    has happened in the past 3000 milliseconds (including the new request).
#    Specifically, return the number of requests that have happened in the
#    inclusive range [t - 3000, t].
#    It is guaranteed that every call to ping uses a strictly larger
#    value of t than the previous call.


class RecentCounter:

    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        left = 0
        right = len(self.times)

        while left < right:
            mid = int((left + right) / 2)
            if t - self.times[mid] <= 3000:
                right = mid
            else:
                left = mid + 1
        return len(self.times) - left


if __name__ == "__main__":
    testinput = 100
    print(RecentCounter.ping(RecentCounter, testinput))
