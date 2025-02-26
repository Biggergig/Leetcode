class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, val=None) -> List[List[int]]:
        if not (0<=sr<len(image) and 0<=sc<len(image[0])): return
        val = val if val is not None else image[sr][sc]
        if image[sr][sc] != val or image[sr][sc] == color:return image
        image[sr][sc] = color
        self.floodFill(image, sr+1, sc, color, val)
        self.floodFill(image, sr-1, sc, color, val)
        self.floodFill(image, sr, sc+1, color, val)
        self.floodFill(image, sr, sc-1, color, val)
        return image