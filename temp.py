f = open("fruits.txt", "r")

cnt = 0
for line in f.readlines():

  obj_list = []

  if (cnt == 0): 
    # print("TITLE: ", line.strip("\n"))
    title = line.strip("\n")
    title_arr = title.split(",") # when you split, this turns the string into an array
    print("This is title_arr", title_arr)
    # split in python splits the string into different parts using a token 

  else: # start reading data
    new_obj = {} # this is a dictionary
    data_arr = line.strip("\n").split(",")

    for i in range(len(title_arr)): # 0, 1, 2 because title_arr has 3 elements
      field = title_arr[i] 
      new_obj[field] = data_arr[i]

    obj_list.append(new_obj)
  cnt = cnt + 1 

  print(obj_list)
  
  # if ( cnt > 100):
  #   break

  # where can i use file processing? 
  # - read csv data .. UNHCR data, excels, 
  # (advanced) create objects out of this and do your "computation" 

  # find out how many countires there are in the data sheet
  # split data using a delimiter (in this case, it's ",") because CSV stands for "comma seperated values"
