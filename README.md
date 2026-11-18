# Welcome to MicroflashOS Next! Now in Python!

A port of [MicroflashOS Next](https://github.com/knbn1/mfos-next) to Python.

## Why?

Originally it was written with Batch but it was a pain to debug and it not being cross-platform meant that development was limited by the underlying Windows operating system, which we all know absolutely sucks nowadays.

I've been using Wine to develop it on Linux, which was fine for all intents and purposes but there were a decent amount of compatibility problems when switching between Windows and Wine.

Having switched to Linux for well over 2 years now, I think it's about time I left Windows behind to create a more open and cross-platform MicroflashOS.

Also I've started to take Python classes at school and this sounds like a good place to improve my skills.

## Progress Report

What has been implemented:

- Most of the kernel (all of `cmd.mcm`'s functions are now integrated into `kernel.py`) 
- Core utilities (`core.mcm`), this includes commands such as `about`, `clock` and `shutdown`
- File management tools (`fsutils.mcm`), things like `mkdir`, `rmdir`, `cd`
- MicroflashOS Protector (`proctector.mcm`)
- Loading help sections with `help`

What has not:

- Functions for user creation, deletion and switching (`userspace.mcm`)
- MicroflashOS Next Package Manager (`neopkg.mcm`) and by extension all packages in the [mfos-next-packages repository](https://github.com/knbn1/mfos-next-packages)
- Logging and command history functions

What will not be implemented:

- MicroflashOS Next Consolidations (`compact.mcm`) as to my knowledge there is no way to make that work yet
- Devices (memory sectors, neopkg cache, etc)
- Developer tools (`devtools.mcm`), where we're going we won't need them.

To-do (priority sorted from highest to lowest):

- Implement `userspace.mcm`
- ~~Implement loading/reading help sections~~
- ~~Implement `proctector.mcm`~~

Note that this time round I'm willing to sacrifice a bit of the lore for a more functional system. My stubbornness ruined a few things in the original mfos-next project.

## Installation Instructions

### For the latest commit:
Download `kernel.py` and all other Python scripts you see in the main repository.

Then run `kernel.py`. It should find all the necessary sysmodules and boot to MicroflashOS Next.

### For releases:
Download `mfos-next-py.zip` and extract it somewhere. Then run `kernel.py`.

## Uninstalling

Delete all the Python scripts.

# My stance on the usage of AI

I think it's fine *as a learning tool*. 

I myself have consulted Google Gemini a few times while developing this project to help with some things I had no clue of how to make, such as the command parser (which recursively generates a list of variables from the user input to use as arguments).

However, I strictly believe that you should take the time to de-slop or "humanize" your code. How? Try rewriting it, doing your due research so you actually understand how it works and can write it by yourself the next time.

You cannot simply copy paste an AI's output and put it into your pull request or build your code from scratch with AI assistance.
