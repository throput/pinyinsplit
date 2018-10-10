pinyinsplit
===========

This is a Python library for splitting a Chinese Pinyin phrase into possible 
permutations of valid Pinyin words.

Usage
-----

Some examples of using the library are as follows:

>>> from pinyinsplit import PinyinSplit
>>> pys = PinyinSplit()
>>> pys.split('XiangGangDaXue')
[['Xiang', 'Gang', 'Da', 'Xue'], ['Xiang', 'Gang', 'Da', 'Xu', 'e'], ['Xi', 'ang', 'Gang', 'Da', 'Xue'], ['Xi', 'ang', 'Gang', 'Da', 'Xu', 'e']]
>>> pys.split('shediaoyingxiongchuan')
[['she', 'diao', 'ying', 'xiong', 'chuan'], ['she', 'diao', 'ying', 'xiong', 'chu', 'an'], ['she', 'di', 'ao', 'ying', 'xiong', 'chuan'], ['she', 'di', 'ao', 'ying', 'xiong', 'chu', 'an']]
>>> pys.split('shediaoyingxiongchuanxyz')
[]

Installation
------------

You can install ``pinyinsplit`` as follows:

.. code-block:: sh

   $ pip install pinyinsplit
