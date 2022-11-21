class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        numbers = [0] * 10
        for i, val in enumerate(secret):
            s = int(secret[i])
            g = int(guess[i])
            if s == g:
                bulls += 1
            else:
                if numbers[s] < 0:
                    cows += 1
                if numbers[g] > 0:
                    cows += 1
                numbers[s] += 1
                numbers[g] -= 1
        return str(bulls) + "A" + str(cows) + "B"
