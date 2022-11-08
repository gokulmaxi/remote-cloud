#!/usr/bin/env python3

import docker
import csv

client = docker.from_env()
with open("data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)
        client.containers.run(
            "kishoredurai/ubuntu-desktop:prog-1.01.0",
            # ports={"6901/tcp": row[4]},
            network="containers",
            name="remote_" + row[1],
            volumes={row[1]: {"bind": "/home", "mode": "rw"}},
            environment={"VNC_PW": row[1]},
            shm_size=512,
            remove=True,
            detach=True,
        )
