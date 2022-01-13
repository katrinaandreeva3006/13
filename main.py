teksts = input("Ievadiet skaitļus: ")
def replaceTwos(teksts):
  if teksts.count("2")>0:
    teksts = teksts.replace("2","divi")
    print(teksts)
  else: 
      teksts = "Nekas netika aizvietos."
      print(teksts)
  return teksts
replaceTwos(teksts)