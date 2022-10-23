# Project Title
Assignment 7: Using Libraries

## Objectives
Use popular python libraries to accomplish common tasks.

## Description
In the file data_processor.py, there's a function called get_random_matrix(), which create and return an N x M matrix of random floating point numbers sampled from a uniform. get_file_dimensions() function, which takes in the name for a csv file. Then, read in the file and return the dimensions of the tabular data. write_matrix_to_file() function creates an N x M matrix of random numbers from a uniform distribution and then write it to a csv file. The file plotter.py produces three figures, which contained one box for each of the four measurements in the data set and a scatter plot of sepal width vs sepal length.

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

Use the [link](https://github.com/cu-swe4s-fall-2022/assignment-7-using-libraries-jili5044.git) here to install package.

### Executing program


```
# How to use data_processor.For example
import data_processor as dp
dp.get_random_matrix(num_rows, num_columns)
dp.get_file_dimensions(file_name)
dp.write_matrix_to_file(num_rows, num_columns, file_name)
```


```
# plot with iris.data. The figure stored in totally 3 files, iris_boxplot.png,
# petal_length_v_width_scatter.png and multi_panel_figure.png

python plotter.py
```

```
# run tests by using run.sh
bash run.sh
```


## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Jiaxin Liu
ex. [@Jiaxin](https://twitter.com/Jiaxin3479) - jili5044@colorado.edu

## Version History
   
* 1.0
    * Initial Release

## Contributing

1. Fork it (<https://github.com/cu-swe4s-fall-2022/assignment-7-using-libraries-jili5044.git/fork>)
2. Create your feature branch (`git checkout -b feature`)
3. Commit your changes (`git commit -am 'Add some message'`)
4. Push to the branch (`git push origin feature`)
5. Create a new Pull Request


