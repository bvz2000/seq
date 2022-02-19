# seq

Very basic command line utility to list sequences in a directory.

For example: If you have the following set of frames in a directory:

```
test2.1.jpg
test2.2.jpg
test2.3.jpg
test_name.1.jpg
test_name.2.jpg
test_name.3.jpg
test_name.5.jpg
test_name.7.jpg
test_name.9.jpg
```

and you run this tool, it will print:

```
> seq
test_name.1-3,5-9x2.jpg
test2.1-3.jpg
```

If you want to see any missing frames, you can use the -m option:

```
> seq . -m
test_name.1-3,5-9x2.jpg missing: [4, 6, 8]
test2.1-3.jpg missing: []
```
This tool requires that you first install bvzframespec (also available on github).

This tool is relatively simple-minded at the moment. 

The underlying library that this tool relies on (bvzframespec) is fairly robust, but this tool itself could use a bit of polish. Even so, for the moment this tool does actually work well and given its minimal amount of needed utility, should do just fine.