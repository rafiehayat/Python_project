ItemsInCart = 0

if ItemsInCart!=2:
    # raise Exception("Products Cart count is not matching")
    pass


assert(ItemsInCart==0)


try:
    with open("file.txt","r") as reader:
        reader.read()

# except:
#     print("Somehow i reached this block because try block is failed")
except Exception as e:
    print(e)

finally:
    print("always called no matter try or except block is called")
