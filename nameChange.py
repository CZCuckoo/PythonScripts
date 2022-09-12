import os

toc=[
"m01_s01_t01",
"m01_s01_t02",
"m01_s01_t03",
"m01_s01_t04",
"m01_s01_t05",
"m01_s01_t06",
"m01_s01_t08",
"m01_s01_t09",
"m01_s01_t10",
"m01_s01_t11",
"m01_s01_t12",
"m01_s01_t15",
"m01_s01_t16",
"m01_s01_t20",
"m01_s01_t21",
"m01_s01_t22",
"m01_s01_t23",
"m01_s01_t24",
"m01_s01_t25",
"m01_s01_t26",
"m01_s01_t27",
"m01_s01_t28",
"m01_s01_t29",
"m01_s01_t30"
]

directory = os.scandir("./")

counter = 0

for image in directory:
    os.rename(image.name,toc[counter]+".jpg")
    counter +=1