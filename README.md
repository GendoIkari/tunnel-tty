# tunnel-tty
This is the simplest script possible to create a tunnel between two virtual serial ports.

*Note*: you should be in the ```tty``` group to access to ```/dev/ptmx``` and ```/dev/pts/[..]``` without *sudo*.

```
$ python tunnel_tty.py
```

The output will tell you the pair of devices.
```
/dev/pts/1 -> /dev/pts/20
```

Special thanks to [Pietro](https://github.com/plorefice)!
