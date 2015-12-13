Usage
-----

Assume you are already run the service (see below). Then you can request the API

.. code:: bash

    $ curl -X POST \
           -H 'Content-Type: application/json' \
           -d '{"url": "http://google.com", \
                "callback": "http://my.callback.server.conm:8000/upload/image"}' \
           http://localhost:8765/thumbnail

The **thumbnail** endpoint accepts only *application/json* content type, so request body
should be a valid JSON. Also please pay attention you *CANNOT* use http://localhost as callback server
since it will be try to connect inside of docker container.

Required arguments are:

* **url** — is url to be snapshotted
* **callback** — url where snapshot will be uploaded with **multipart/form-data** POST request

Optional arguments are:

* **delay** — time in microsecond to wait before snapshot


Build image from Dockerfile
---------------------------

Command to build:

.. code:: bash

    $ docker build -t marazmiki/flaskycapt .

For convenience there is make target **build** for these purpose:

.. code:: bash

    $ make build

Run
---

For development purpose better weay to run removeable container with attached
terminal:

.. code:: bash

    $ make dev

Actually this target will following command:

.. code:: bash

    $ docker run
        --rm \
        --name=flaskycapt \
        --publish=8765:8765 \
        -it marazmiki/flaskycapt:latest

    # The same result with "dev" make target:

    $ make dev


For production better way is run container in dettached mode with rest
daemon:

.. code:: bash

    $ docker run \
        --name=flaskycapt \
        --detach=true \
        --publish=8765:8765 \
        --restart=always \
        marazmiki/flaskycapt:latest

    # The same result with "daemon" make target:

    $ make daemon

After that, you can manage this container within docker commands:

.. code:: bash

    $ docker stop flaskycapt
    $ docker start flaskycapt
    $ docker restart flaskycapt

to stop, start and restart the container respectively.
