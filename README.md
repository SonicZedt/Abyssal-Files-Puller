# Abyssal-Files-Puller
Move files from deep subdirectories into single folder. For example you have a bunch of files in messy directories:
```bash
abyssal_dir
│
├── subdir0
│   ├── subdir00
│   │   ├── file21.ext
│   │   ├── file22.ext
│   │   └── file23.ext
│   └── subdir01
│       ├── file21.ext
│       ├── file22.ext
│       └── file23.ext
│
├── subdir1
│   ├── file21.ext
│   ├── file22.ext
│   └── file23.ext
│
├── subdirn
│
└── file_n.ext
```

## Move destination
The files are moved to folder called *files from abyss* which will created automatically where the script or program executed if it not available.
```bash
project_dir
│
├── files from abyss
├── other stuffs
└── AFP.exe or abyss.py
```

## Usage
### App
1. Download the app from the [release page](https://github.com/SonicZedt/Abyssal-Files-Puller/releases).
2. Launch the AFP.exe
3. Wait a couple second, file explorer will open automatically
4. Select the *abyssal_dir*
5. Moving process will started after *abyssal_dir* selected

### Script
`Pull_From_Abyss(abyssal_dir, extension = 'all')`
*extension can not be defined if using AFP.exe, so it would moves all found files*

| Argument    | Type  | description |
| :--         | :--   | :--         |
| abyssal_dir | str   | Files parent directory |
| extension   | str   | Files extension \n default: 'all' |

## Example
for example the project directory is like this:
```bash
project_dir
│
├── data
│   ├── images
│   │   ├── car.jpg
│   │   ├── bike.jpg
│   │   └── bird.jpg
│   └── doc
│       ├── report.pdf
│       └── guide.pdf
│
└── script
```

### 1st example
```
from abyss import Pull_From_Abyss

abyssal_dir = '../project_dir/data/'

Pull_From_Abyss(abysall_dir, 'jpg')
```
This code will move all files ended with *jpg* to *files from abyss*, so the result would be like:
```bash
project_dir
│
├── files from abyss
│   ├── car.jpg
│   ├── bike.jpg
│   └── bird.jpg
│
├── data
│   ├── images
│   └── doc
│       ├── report.pdf
│       └── guide.pdf
│
└── script
```
### 2st example
```
from abyss import Pull_From_Abyss

abyssal_dir = '../project_dir/data/'

Pull_From_Abyss(abysall_dir)
```
This code will move all files to *files from abyss*, so the result would be like:
```bash
project_dir
│
├── files from abyss
│   ├── car.jpg
│   ├── bike.jpg
│   ├── bird.jpg
│   ├── report.pdf
│   └── guide.pdf
│
├── data
│   ├── images
│   └── doc
│
└── script
```

The origin directory will remain empty after operation.
