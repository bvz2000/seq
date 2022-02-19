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

This tool is very crude at the moment. The underlying library that it relies on (bvzframespec) is fairly robust, but this tool itself needs a fair bit of polish. For example, you must supply the directory (you cannot leave that portion blank). And if you use the -m option, it must come after the directory.

These things will be improved in time. But for the moment, this tool does actually work.