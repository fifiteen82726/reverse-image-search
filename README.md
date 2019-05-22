# README

This is a CBIR system implemented by Rails and Python
Video demo: https://youtu.be/mNyZ0TLwdP0

* Ruby version: 2.5.1
* Configuration image data

Please put your image in the `database` folder like this structure
![image](https://user-images.githubusercontent.com/6240395/58141284-72da4300-7c08-11e9-9612-0dc187a137ae.png)


![image](https://user-images.githubusercontent.com/6240395/58141272-68b84480-7c08-11e9-957c-798269faca34.png)
 
* Prepare cache data for the further search
```
python3 src/resnet.py
```
(This command will generate the cache data in folder `cache` and `data.csv` in the root directory. If you update your image dataset and want to update the cache data, you need to remove `cache` folder and `data.csv`)

* How to run the query test 
```
python3 query.py image-you-want-to-search image-category
```

Example:
```
python3 query.py public/1558249242.jpg effiel
```
Search Result

```bash
Using cache..., config=resnet152-avg, distance=d1, depth=3
{'img': 'public/1558249242.jpg', 'cls': 'effiel', 'hist': array([1.1803220e-03, 1.2102447e-03, 1.8271050e-04, ..., 4.8219634e-05,
       1.0576390e-03, 5.9930864e-04], dtype=float32)}
database/eiffel/paris_eiffel_000000.jpg	0.1455633044242859,	Class eiffel
database/general/paris_general_000084.jpg	0.3631804883480072,Class general
database/general/paris_general_000138.jpg	0.3734038174152374,Class general
database/general/paris_general_000143.jpg	0.3752489686012268,Class general
database/general/paris_general_000021.jpg	0.3753284215927124,Class general
database/eiffel/paris_eiffel_000005.jpg	0.377275288105011,	Class eiffel
database/eiffel/paris_eiffel_000217.jpg	0.37977999448776245,	Class eiffel
database/general/paris_general_000144.jpg	0.38824301958084106,Class general
database/eiffel/paris_eiffel_000136.jpg	0.4028390049934387,	Class eiffel
database/eiffel/paris_eiffel_000128.jpg	0.40601611137390137,	Class eiffel
```

- Reference

https://github.com/ry/tensorflow-resnet 
https://github.com/KaimingHe/deep-residual-networks https://github.com/pochih/CBIR/blob/master/src/resnet.py
http://web.stanford.edu/class/cs276/handouts/EvaluationNew-handout-1-per.pdf
