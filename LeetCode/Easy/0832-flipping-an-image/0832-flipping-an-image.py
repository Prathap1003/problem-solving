class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in range(len(image)):
            image[row]=image[row][::-1]
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
        return image