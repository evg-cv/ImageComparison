# Image Comparison

## Overview

This project is to estimate similarity of two images, one of which is an newly uploaded image from site and other of which is an image in the database.

Comparing the newly uploaded image with all the images in the database one by one, the image with the highest similarity and it's similarity degree are extracted.

Then the result is displayed in http://imgcompare2.crevisio.com/, and if there is no similar image, it will display none result.

## Structure

- source
    
    There are several kinds of algorithms and modules to compare two images to estimate the similarity.
    
- utils

    Tools concerned with image processing, file management and database credential are contained.

- main

    This is the main execution file.

- requirements
    
    All the dependencies to execute project are inserted.

- settings

    Several settings are conducted in this file

## Installation

- Python 3.6 environment

- This project must be in the parent directory in php server.

- The database credential file containing host name, database name, username and password should be added in utils directory. This file name can be either "mysql_credential.json" or changed in settings file.

- Dependency installation
    
    ```
     pip3 install -r requirements.txt
    ```

## Execution

When uploading new file, you must execute this python file with the newly uploaded image path. For example,
    
```
$result = shell_exec('python /path/main.py ' . escapeshellarg(json_encode($data))); // $data: image frame path
```

Then after estimating similarity of images, project returns the result. In the corresponding php file, the result will be able to be received.

```
$resultData = json_decode($result, true);
var_dump($resultData);
```
