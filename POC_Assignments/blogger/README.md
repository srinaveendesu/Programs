Running the program

`cd blogger`

Install docker in your machine and run following commands

Build the docker image:

`docker build --tag flask-blog-container:1.0 .`

Run the image:

`docker run --rm --name blogger -it --env-file env -p 8888:5050 -d flask-blog-container:1.0`
