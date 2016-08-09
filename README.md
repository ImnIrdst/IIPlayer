# iiPlay
A CLI player based on mpv, built for watching tv series easier.

# installation

1. install mpv player

    ```
    sudo apt install mpv
    ```

2. install iiplay
    
    ```
    ./setup.py install
    
    source ~/.bashrc
    ```

3. change the configurations in configs.json

    ```
    nano files/configs.json
    ```

3. change the cur shortcuts in db.json

    ```
    nano files/configs.json
    ```

# usage

add a shortcut (TODO)

```
iiplay add hoc House*of*Cards -s=01 -e=02
```

play current 

```
iiplay cur hoc
```

play next

```
iiplay next hoc
```

play prev

```
iiplay previous hoc
```

see history (last 3) (TODO)

```
iiplay history
```

add the following film to the watching queue (TODO)

```
iiplay add Never*Back*Down*2008
```

print the watching queue (TODO)

```
iiplay queue
```
