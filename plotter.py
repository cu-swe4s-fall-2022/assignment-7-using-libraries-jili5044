# Your code to create majestic plots goes in here!
import matplotlib.pyplot as plt
import pandas as pd


iris = pd.read_csv('iris.data', header=None)
iris.columns = ['sepal_width',
                'sepal_length',
                'petal_width',
                'petal_length',
                'species']

# figure 1
measurement_names = ['sepal_width',
                     'sepal_length',
                     'petal_width',
                     'petal_length']
plt.boxplot(iris[measurement_names], labels=measurement_names)
plt.ylabel('cm')
plt.savefig('iris_boxplot.png')
plt.clf()

# figure 2
for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name]
    plt.scatter(iris_subset['sepal_length'],
                iris_subset['sepal_width'],
                label=species_name,
                s=8)
plt.legend()
plt.xlabel('sepal_length(cm)')
plt.ylabel('sepal_width(cm)')
plt.savefig('petal_width_v_length_scatter.png')


# figure 3
fig, axes = plt.subplots(1, 2)
fig.set_size_inches(10, 5)

# left box plot
axes[0].boxplot(iris[measurement_names], labels=measurement_names)
axes[0].set_ylabel('cm')

# right box plot
for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name]
    axes[1].scatter(iris_subset['sepal_length'],
                    iris_subset['sepal_width'],
                    label=species_name,
                    s=8)
axes[1].legend()
axes[1].set_xlabel('sepal_length')
axes[1].set_ylabel('sepal_width')

plt.savefig('multi_panel_figure.png')
