# boost

# download boost src pkg
link: https://www.boost.org/users/download/

```
./bootstrap.sh
sudo ./b2 install --with-system --with-thread --with-date_time --with-regex --with-serialization --with-python link=static runtime-link=shared threading=multi debug
```

```
sudo apt-get install libboost-all-dev
```

