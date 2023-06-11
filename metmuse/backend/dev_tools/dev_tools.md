## Dev Tools
This folder serves to house any scripts designed to aid in backend development

### building.sh
Run by:
```shell
$ cd dev_tools/
$ ./building.sh
```

This script requires that you:
  - Have a `.venv` folder as your environment 
  - Have the pip requirements installed for running the project

This script _does not_ run the RQ workers, and is meant primarily just for working on the
Back End API.