# asymlink

Symlink project files into place with a single command. Great for
setting up development or shared test environments.

## Getting started

1. Create `.asymlink` in the directory containing the files you wish
to symlink.
0. Use relative paths as the keys in our `.asymlink` configuration
file. These define the source files we will link to.
0. Use absolute paths as the values. These define the links that will
point to our source files.

The following `.asymlink` example shows a simple executable and an
associated configuration file.

```
{
  "config.json": "/etc/sample/config.json",
  "sample":      "/usr/bin/sample"
}
```

Running `asymlink` from within the directory containing this example
will attempt to create symlinks to the local configuration and
executable.

Symlinking will proceed when:

1. File locations do not already exist
0. File locations exist and are of type **symlink**

Symlinking will fail when:

1. Any of the symlink file locations exist and are of type
**directory** or **file**.

To override existing files of any type use `asymlink -f`.
