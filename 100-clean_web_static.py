#!/usr/bin/python3
def do_clean(number=0):
    """ Do clean """
    if (int(number) >= 0):
        if (int(number) < 2):
            number = 2
        else:
            number = int(number)+1
        r_path = "/data/web_static/releases/"
        l_path = "./versions/"
        with cd(r_path):
            run("ls -1t | tail -n +{} | xargs rm -rf --".format(number))
        with lcd(l_path):
            local("ls -1t | tail -n +{} | xargs rm -rf --".format(number))
