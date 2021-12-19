
# Naddaha
Naddaha is a python script that can be used in downloading screenshots of list of urls to be used in blue team investigations and SOC "Security operation centers" daily work.


## Installation

To use Naddaha, you need to have python 3.x installed and the required modules.
Use pip to install any missing modules
```bash
  pip install -r requirements.txt
```
To use Naddaha, you need to create an Urlscan API key to use it while scanning.
This is a one time task and you will add the key to the conf.ini file.
To create Urlscan API Key. 

- You will need to create free account on urlscan.
- Go to your profile > settings & API > Create new API Key
- Add a Description then click on "Create API key".
- API key will be created.
- Now copy it and add it "with dashes" to your conf.ini file. 

## Usage

```javascript
python naddaha.py <list of urls file>
```



## Authors

- [@Hosney](https://www.github.com/mohamedhossam07)

