# Welcome to MicroflashOS Next! Now in Python!

A port of [MicroflashOS Next](https://github.com/knbn1/mfos-next) to Python.

Originally it was written with Batch but it was a pain to debug and it not being cross platform meant that development was limited by the underlying Windows operating system.

Having switched to Linux for well over 2 years now, I think it's about time I left Windows behind and created a more open MicroflashOS.

## What has been implemented:

- Most of the kernel (all of `cmd.mcm`'s functions are now integrated into `kernel.py`) 
- Most of the core utilities sysmodule (`core.mcm`), this includes commands such as `about`, `clock` and `shutdown`
- Most of the file management tools (`fsutils.mcm`), things like `mkdir`, `rmdir`, `cd`

## What has not:

- Functions for user creation, deletion and switching (`userspace.mcm`)
- MicroflashOS Next Package Manager (`neopkg.mcm`) and by extension all packages in the [mfos-next-packages repository](https://github.com/knbn1/mfos-next-packages)
- MicroflashOS Protector (`proctector.mcm`), needed as an authentication procedure for critical changes
- Developer tools (`devtools.mcm`)
- Help sections. Currently all help sections are hardcoded into `core.py` until I can figure out reading from files.
- Other parts of `core.mcm` and `fsutils.mcm`

## What will not be implemented:

- MicroflashOS Next Consolidations (`compact.mcm`) as to my knowledge there is no way to make that work yet
- Devices (memory sectors, neopkg cache, etc)
