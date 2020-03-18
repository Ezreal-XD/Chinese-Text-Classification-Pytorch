import os

# python run.py --model TextCNN --embedding random --word True

# plus = ""
# plus = " --word True"
plus = " --word True --embedding random"


print("=============== Training Model: CNN ===============\n")
os.system("python run_2.py --model TextCNN" + plus)
#
# print("=============== Training Model: RNN ===============\n")
# os.system("python run.py --model TextRNN" + plus)
#
# print("=============== Training Model: RNN_ATT ===============\n")
# os.system("python run.py --model TextRNN_Att" + plus)
#
# print("=============== Training Model: RCNN ===============\n")
# os.system("python run.py --model TextRCNN" + plus)

# print("=============== Training Model: FastText ===============\n")
# os.system("python run.py --model FastText --embedding random" + plus)

# print("=============== Training Model: DPCNN ===============\n")
# os.system("python run.py --model DPCNN" + plus)
#
# print("=============== Training Model: Transformer ===============\n")
# os.system("python run.py --model Transformer" + plus)




