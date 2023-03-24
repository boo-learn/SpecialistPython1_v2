# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой


#Если одна окружность лежит внутри другой, то расстояние между центрами меньше разности их радиусов:
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def round_inside(round1, round2):
    print(f"Round 1 (x1,y1,r1) is: {round1}")
    print(f"Round 2 (x2,y2,r2) is: {round2}")
    dist = distance(round1[0], round1[1], round2[0], round2[1])
    r_difference = abs(round1[2] - round2[2])
    # print(dist)
    # print(r_difference)
    #print((round1[2] - round2[2]) ** 2 > (round1[0] - round2[0]) ** 2 + (round1[1] - round2[1]) ** 2)
    return r_difference > dist


print(round_inside((10, 12, 3), (14, 18, 11)))  # (x1,y1,r1),(x2,y2,r2)
print("#"*50)
print(round_inside((10, 12, 3), (14, 18, 10)))  # (x1,y1,r1),(x2,y2,r2)
print("#"*50)
print(round_inside((10, 12, 3), (14, 18, 3)))  # (x1,y1,r1),(x2,y2,r2)
print("#"*50)
