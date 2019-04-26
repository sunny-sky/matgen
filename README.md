# 绘制能带图 
参考[案例](http://matgenb.materialsvirtuallab.org/2017/09/03/Analyze-and-plot-band-structures.html)
获取一个band structure，如bs,再使用
```python
plotter = BSPlotter(bs)
plotter.get_plot().show()
```
绘制图形，样例为
![Alt text](./img/myplot.png)

bs类型为
```python
<class 'pymatgen.electronic_structure.bandstructure.BandStructureSymmLine'>
```
计划使用
```python
BandStructureSymmLine.from_dict(d)
```
函数获取一个BandStructureSymmLine类，其中d为字典类。

下一步使用excel中的数据构造d。
