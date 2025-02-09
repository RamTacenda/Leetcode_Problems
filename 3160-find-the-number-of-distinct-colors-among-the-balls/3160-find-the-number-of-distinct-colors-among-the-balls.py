class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        res = list()
        ball_map, color_map = dict(), dict()

        for q in queries:
            ball, color = q
            if ball in ball_map:
                prev_color = ball_map[ball]
                color_map[prev_color] -= 1

                if(color_map[prev_color] == 0):
                    del color_map[prev_color]

            ball_map[ball] = color
            color_map[color] = color_map.get(color, 0)+1
            res.append(len(color_map))
        
        return res