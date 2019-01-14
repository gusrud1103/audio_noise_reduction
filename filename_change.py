import os

path = '/Users/jw/Downloads/taeyun/'

def main():
   i = 0

   for filename in os.listdir(path):
       dst = "taeyun_" + str(i) + ".wav"
       src = path + filename
       dst = path + dst

       os.rename(src, dst)
       i += 1

if __name__ == '__main__':
   main()