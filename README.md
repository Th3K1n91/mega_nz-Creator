# Download/Install
[Download Here (Python)](https://github.com/Th3K1n91/mega_nz-Creator/archive/refs/heads/main.zip) (Both WIN and Unix)<br>[Download Here (WIN-EXE)](https://github.com/Th3K1n91/mega_nz-Creator/releases)<br>or Clone this Repo

## Install For Unix (Linux Mac OSX)
install python3, qt5 and megatools binary(already in repo)

# Start
**Unix:**
```
python3 accr.py
```
<hr>

**Windows:**
```
python accr.py
```
```
or double click accr.py or double click start.bat
```
<hr>

Done!

Accounts saved in **accounts.txt!**

# Usage
- <p>In Field Username you type in anything you want which will be the login after creating [<strong>string</strong>]</p>
    <p><em>>>> It will generate [Your_input_in_username]+[Random_letters]@xitroo.de</em></p><br>

- <p>In Field Count you type in how many accounts should be generated [<strong>integer</strong>]</p><br>

- <p>The Password field is as same the Username field but it will apply to all generated accounts [<strong>string</strong>]</p>
  - <strong>Must be 8 characters long</strong><br>
  - <strong>Must contain upper and lowercase letters</strong>
    <p><em>>>> The Login would be [Your_input_in_username]+[Random_letters]@xitroo.de:[Your_input_in_password]</em></p><br>
  
- <p>In Threads field you will enter how many Accounts at once will be created [<strong>integer</strong>]</p>
    <p><em>>>> It will open a Browser each thread so be careful which number you will input</em></p><br>
  
After everything is filled click on Button "Start" and wait at least 5 seconds, if nothing happens please check if every field is filled up

# Example
![/images/example.png](https://github.com/Th3K1n91/mega_nz-Creator/blob/main/images/example.PNG)

### Output
```
EMAIL:PASSWORD

somethingHArIP@xitroo.de:SomeThing1
somethingUk@xitroo.de:SomeThing1
somethingrmUja@xitroo.de:SomeThing1
somethingrmssx@xitroo.de:SomeThing1
```

# Solve not start problem on Unix

for Ubuntu/Debian with apt

```
sudo apt-get -y install python3 python3-request python3-pyqt5 qt5
pip3 install importlib_metadata unofficial-xitroo-api==0.7
python3 accr.py
```

if not work use python 3.12 with ppa for Ubuntu Online

```
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get -y install python3.12 qt5
wget https://bootstrap.pypa.io/get-pip.py
python3.12 get-pip.py
rm -rf /usr/local/bin/pip /usr/local/bin/pip3
/usr/local/bin/pip3.12 install importlib_metadata pyqt5 request unofficial-xitroo-api==0.7
python3.12 accr.py
```

for Fedora/RedHat with dnf

```
sudo yum -y install python3 python3-request python3-pyqt5 qt5
pip3 install importlib_metadata unofficial-xitroo-api==0.7
python3 accr.py
```

if it still doesn't work you will need to compile python 3.12 from sources

install build dependency for Ubuntu/Debian

```
sudo apt-get -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget qt5-dev
```

install build dependency for Fedora/RedHat

```
sudo yum -y install epel-release
sudo yum -y group install "C Development Tools and Libraries" "Development Tools"
sudo yum -y install zlib-devel openssl-devel ncurses-devel gdbm-devel readline-devel libffi-devel qt5 wget
```

build python 3.12 from source and start

```
wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz
tar -xvf Python-3.12.0.tgz
rm -f Python-3.12.0.tgz
cd Python-3.12.0
./configure --enable-optimizations
make
sudo make altinstall
/usr/local/bin/pip3.12 install importlib_metadata pyqt5 request unofficial-xitroo-api==0.7
python3.12 accr.py
```

