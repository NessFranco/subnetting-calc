def get_input():
    ip = str(input("Inserte la ip con sufijo que desea subnetear :P\n>>>"))
    subnets = str(input("Ingrese la cantidad de subredes que necesita :P\n>>>"))
    num_hots = str(input("Inserte la cantidad de hosts que desea por subnet ;P\n>>>"))

    #We process the strings to get more refined and segmented data to use later
    octs = ip.split(".", 4)
    loct = octs[3].split("/",1)
    sfx = loct[1]
    octs[3] = loct[0]
    octs = list(map(int,octs))
    errors = 0

    #We validate the inputs from the user
    for i in range(0,3):
        if octs[i] > 255:
            print("El octeto ", i+1, " es inválido")
            errors+=1
        
    if errors == 0:
        #We show back the data back for the user to verify
        print("_"*100,"\n\n")
        print("\tIP -------> " +  ip + "\n\n\tHOST -----> " + num_hots + "\n\n\tSUBNETS --> " + subnets)
        print("\n\tOctetos -->",octs)
        print("\n\tSufijo --->",sfx,"\n\n")
        print("_"*100)
    else:
        print("Vuelva a intentarlo...\n\n")