def count_word(w):
    w=0
    space=False
    for i in a:
      if i == ' ':
          if space == False:
            w = w + 1
            space = True
            
          else:
            space = False  
            
        
a=input("enter your sentence:")
print(count_word(w))
        

