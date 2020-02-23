FIZZ_ON = 3
BUZZ_ON = 5
FIZZ = 'Fizz'
BUZZ = 'Buzz'


def fiz(seq):
    for i in seq:
        if i % (FIZZ_ON * BUZZ_ON) == 0:
            yield f'{FIZZ}{BUZZ}'
        if i % FIZZ_ON == 0:
            yield FIZZ
        elif i % BUZZ_ON == 0:
            yield BUZZ
        else:
            yield i


def stringify_seq(seq):
    return ','.join([str(i) for i in seq])


class Solution:
    def run(self, N, M):
        sequence = range(N, M + 1)
        sequence = ([i for i in fiz(sequence)])
        return stringify_seq(sequence)

print(Solution().run(1,10))
