
file_path = 'C:\\test'
action = "rename"


class Handler():

    def rename(d):
        dif = []
        if len(d) > 1:
            for i in d:
                dif.append(list(i.split('.')))
        if dif[0][0] != dif[1][0]:
            print(str(d[0]) + " was renamed to " + str(d[1]))
        else:
            pass

    def convert(d):
        if len(d) > 1:
            dif = []
            for i in d:
                dif.append(list(i.split('.')))
        if dif[0][-1] != dif[1][-1]:
            print(str(dif[0][:]) + " was converted to ." + str(dif[1][len(dif)-1]))
        else:
            pass

    def create(d):
        if len(d) == 1:
            print(str(d[0]) + " was created")
        else:
            pass

    choose_handler = create


