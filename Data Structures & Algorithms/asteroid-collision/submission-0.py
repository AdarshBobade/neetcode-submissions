class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survivors = []
        for asteroid in asteroids :
            alive = True
            if not survivors :
                survivors.append(asteroid)
                continue

            while survivors and (survivors[-1] > 0 and asteroid < 0) and alive :
                if abs(survivors[-1]) < abs(asteroid) :
                    alive = True
                    survivors.pop()

                elif abs(survivors[-1]) > abs(asteroid):
                    alive = False
                
                else :
                    alive = False
                    survivors.pop()
            if alive :
                survivors.append(asteroid)
            
        return survivors



           
            
            
