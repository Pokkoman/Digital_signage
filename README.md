Instructions to set up RabbitMQ

Setting up RabbitMQ can be done in many ways. One of them is by manually downloading the Installer(Binary build also could be run) and running it or by using community Docker image :
# for RabbitMQ 3.9, the latest series
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management

# for RabbitMQ 3.8,
# 3.8.x support timeline: 
https://www.rabbitmq.com/versions.html
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.8-management

Refer link for other OS : https://www.rabbitmq.com/download.html

Note : Using the Windows Installer certain pre-requirements :
There must be only one Erlang version installed at a time
Erlang must be installed using an administrative account
It is highly recommended that RabbitMQ is also installed as an administrative account
Installation path must only contain ASCII characters
It may be necessary to manually copy the shared secret file used by CLI tools
CLI tools require Windows console to operate in UTF-8 mode


Using a Virtual Environemnt 

Install Virtual Environments using the following command : $pip install virtualenv

Creation of Virutal Enviroments can be done using the following commands :
$python3 -m virtualenv /path/<envname>

Activation of Virutal Enviroments can be done using the command :
$python -m ../path/<envname>/Scripts/activate

Now you be in the virtual environment as stated in the terminal with a env prefix to your directory.
Select the ../path/<envname>/Scripts/python as your interpreter to execute the python files.


Cloning the Repository

Open GitHub and go to the GitHub repository that you want to clone.
Click “Code” and copy the given URL.
Open “Git Bash” and change the current working directory to the location where you want the cloned directory.
Type git clone in the terminal, paste the URL you copied earlier, and press “enter” to create your local clone.

Url : https://github.com/Pokkoman/Digital_signage.git


Running the project :

To install all the required packages, use the following command :
$ pip install -r requirements.txt

Run the receiveimage.py file to start the server. This opens up a port that waits for input messages. 
Run senderimage.py file to start sending the image file. 
Run the pyqt5app.py to display the image.
