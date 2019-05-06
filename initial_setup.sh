/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

echo 'export PATH=/usr/local/bin:$PATH' >>~/.bash_profile

brew install readline xz

curl https://pyenv.run | bash

echo 'export PATH=$HOME/.pyenv/bin:$PATH' >> ~/.bash_profile
echo 'eval $(pyenv init -)' >> ~/.bash_profile
echo 'eval $(pyenv virtualenv-init -)' >> ~/.bash_profile


exec "$SHELL" 

source ~/.bash_profile

pyenv install -v 3.7.3