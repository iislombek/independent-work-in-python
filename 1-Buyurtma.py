# --------------------------------------------- Erkin ish

# Mijozdan buyurtma olib ro'yxat ga qoshadigon va nechta ligini kirsatadigon dastur

buyurtmalar = []
for mijoz in range(1,4):
    mijoz = user = input(f"{mijoz} - Buyurtma bering::")
    if user:
        buyurtmalar.append(user)
        print(len(buyurtmalar)," - buyurtma qo'shildi")
        print(buyurtmalar,'\n')
    else:
        print("bo'sh keldi ")
print(f"Jami:{len(buyurtmalar)} ta buyurtma berildi\n{buyurtmalar}")
print("15-daqiqada keladi inshaaAlloh")

# --------------------------------------- erkin ish yakunlangan qoshimcha qoshish kerak
# ------------------------------- o'zgartrish kiritildi
# buyurtma = []
# try:
#     for xorranda in range(1, 4):
#         buyurtma.append(input(f"{xorranda + 0}- Buyurtmani bering::"))
#         print(f"{xorranda}-buyurtma qo'shildi\n{buyurtma}")
#     print(f"Jami: {len(buyurtma)} ta buyurtma berildi")
#     print(f"Biroz kutib turing")
# except:
#     print(f"Uzur dastur ishdan chiqdi")
