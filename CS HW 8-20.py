# CS HW 8-20

fh = open("census.csv", "r")
def cen_stats(filehandle):
    lines = filehandle.readlines()
    for i in range(len(lines)):
        if i >=2:
            file_list = lines[i].split(",")
            state_pop = [file_list[2], file_list[8]]
            state_pop[1] = state_pop[1].split("\n")
            del state_pop[1][1]
            state_pop[1] = "".join(state_pop[1])
        else:
            continue
        print(state_pop[0] + ": " + state_pop[1])
cen_stats(fh)
