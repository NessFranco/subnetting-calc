from decoder import decoder

def main():
    ip = str(input("Inserte la ip con sufijo que desea subnetear :P\n>>>"))
    numHosts = str(input("Inserte la cantidad de hosts que desea por subnet ;P\n>>>"))
    mainstring = "\tIP -------> " +  ip + "\n\n\tHOST -----> " + numHosts
    octs = ip.split(".", 4)
    loct = octs[3].split("/",1)
    sfx = loct[1]
    octs[3] = loct[0]
    ##D = decoder(mainstring)
    ##print(D)
    print("_"*100,"\n\n")
    print(mainstring)
    print("\n\tOctetos -->",octs)
    print("\n\tSufijo --->",sfx,"\n\n")
    print("_"*100)

if __name__ == '__main__':
    main()

