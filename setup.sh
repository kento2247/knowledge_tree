# pyenv install 3.10.0
# pyenv virtualenv 3.10.0 kg
# pyenv local kg

# brew install graphviz #for mac
sudo apt-get install graphviz #for ubuntu
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
pip install -r requirements.txt