# iiPlay
A CLI player based on mpv, personalized for watching tv series

# installation

1. you need mpv player

```
sudo apt install mpv
```

2. run setup-iiplay (Todo)

```
./setup-iiplay.py install
```

3. change the configurations in configs.json

```
nano configs.json
```

# usage

listing all mkv files in a directory

```
iiplay -f ls
```

see history (last 3) (Todo)

```
iiplay history
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
iiplay prev hoc
```

add the following film to the watching queue (Todo)

```
iiplay add Never*Back*Down*2008
```

print the watching queue (Todo)

```
iiplay queue
```
