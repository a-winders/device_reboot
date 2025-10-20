# device_reboot

## Overview

This project showcases an example structure of an Ansible playbook (barring sensitive credentials) that can reboot specified devices by interacting through an MDM and IRM (Infrastructure Resource Modeling) service via APIs.

## Tags
*timezones*
- ```alaska```
- ```cst```
- ```est```
- ```hawaii```
- ```mst```
- ```pst```

*devices*
- ```kds```
- ```kiosks```
- ```pos```

## Example on how to to reboot all devices within a specific timezone
```ansible-playbook tests/test.yml --tags <time_zone>```

Where ```<time_zone>``` refers to the target time zone.

So for example, if you wanted to run an ad-hoc reboot of all devices within the EST timezone, the command to run would be:

```ansible-playbook tests/test.yml --tags est```

## Example on how to reboot all kiosks at specific store(s)
The list of stores are passed as ```extra-vars```

```ansible-playbook tests/test.yml --tags kiosks --extra-vars='{"store_list": []}'```
So for example, if you wanted to reboot all of the kiosks at abc123 and def456:

```ansible-playbook tests/test.yml --tags kiosks --extra-vars='{"store_list": ["abc123","def456"]}'```


:double_exclamation_mark:**Important**:double_exclamation_mark:

Each store ID needs to be placed within quotes, separated by a comma.

##  How it works
Here is an overview of how the playbook works:
1. The role is called for execution via ```tests/test.yml```
2. Commonly reused variables are imported for use across each timezone's script via ```defaults/main.yml```
3. ```tasks/main.yml``` is parsed for matching tags specified in the run command so that only those timezone's devices are rebooted (i.e. ```--tags est```)
4. Once a matching tag is found, the script for that timezone is imported & ran from the ```tasks``` directory.