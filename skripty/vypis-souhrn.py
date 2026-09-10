#!/usr/bin/env python3

#################################################################################
# functions
#################################################################################

def abbreviateSupervisor(supervisor):

    first_name, surname = supervisor.split()

    return f"{first_name[0].upper()}{surname[0].upper()}"

#################################################################################
# main body
#################################################################################

import sys
import yaml
import glob

project_dirs = sorted(glob.glob("../projekty/*-*"))

# write header
sys.stdout.write("project,title,difficulty,supervisor,keywords,link\n")

for project_dir in project_dirs:

    code, abbrev = project_dir.split("/")[-1].split("-")

    # parse file
    with open(project_dir + "/README.yaml") as stream:
        d = yaml.safe_load(stream)

    # get data
    project = code + "-" + abbrev
    title = d["title"]
    difficulty = d["difficulty"]
    supervisor = d["supervisor"]
    keywords = ", ".join(d["keywords"])
    link = "https://github.com/mhkoscience/pchem/tree/main/projekty/" + project

    # update
    supervisor_abbr = abbreviateSupervisor(supervisor)

    # write out
    sys.stdout.write("\"" + project + "\",")
    sys.stdout.write("\"" + title + "\",")
    sys.stdout.write(f"{difficulty:.0f},")
    sys.stdout.write("\"" + supervisor_abbr + "\",")
    sys.stdout.write("\"" + keywords + "\",")
    sys.stdout.write("\"" + link + "\"\n")
