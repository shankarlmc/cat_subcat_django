# Tree Structure of Categories, Subcategories and subsubcategories

``` 
In this tutorial i am going to use django-mptt for categories, subcategories and subsubcategories 
```

## What is Modified Preorder Tree Traversal?
```
MPTT is a technique for storing hierarchical data in a database. The aim is to make retrieval operations very efficient. The trade-off for this efficiency is that performing inserts and moving items around the tree is more involved, as there’s some extra work required to keep the tree structure in a good state at all times. Here’s a good article about MPTT to whet your appetite and provide details about how the technique itself works: 
```

- Trees in SQL
- Storing Hierarchical Data in a Database
- Managing Hierarchical Data in MySQL

## What is django-mptt?
``` 
Django-mptt is a reusable Django app which aims to make it easy for you to use MPTT with your own Django models. 

It takes care of the details of managing a database table as a tree structure and provides tools for working with trees of model instances.
```
