# DRF-For-Test
a very simple API for Insert, Delete and Select in SQLs dataBases
---
# Using The project with virtual environment:
first active your virtual environment,

then run:

``` bash
  source start.sh
```
---
# Using The project with Docker:
it is obvious that you'll need `Docker` on your system.

execute this command:

```bash
  docker-compose up
```
---

# Attention:
by default, swagger uses staticfiles for directions of static.Go to site packages and replaces {%staticfiles%} by {%static%} in the templates directory;index.html.

---

***API Usage:***

> /schema

## returns api documentation by swagger interface.


> api/status

## returns api availability under get and post requests

> /api/hero/<primary_key>

## returns a hero by its pk

> /api/hero/?name=''

## returns a hero by its name or alias

> /api/hero/all

## returns all heroes

> /api/hero/search/?q=''

## returns a lis of heroes by your q value

> /api/hero/submit

## submit a new hero By 3 parameters:(name,alias,world_id) - world_id is the pk of the world

> /api/hero/delete

## delete an existing hero by pass 2 parameters:(name,flag) - flag = 1  is delete confirmation

> /api/world//?world_name=''

## returns a world by its name or content

> /api/world/all

## returns all worlds


> /api/auth/login

## returns sign in authentication

> /api/auth/logout

## returns log out function

> /api/product/<id>

## returns product details by its ID

---

***Making Query***

### get products that are in one sub_category

```python
>>> cotumeproducts = Product.objects.filter(sub_category__name="suit's")
>>> cotumeproducts
<QuerySet [<Product: batman's gloves - 4456987>, <Product: Spiderman's mask - 3365479>]>
>>> for name in cotumeproducts:
...     print(name.name)
...
batman's gloves
Spiderman's mask
```
---
## TODO:

- [x] : Dispaly category and sub-category 's name instead of id's

- [x] : Think more about category and sub-category 's Logic

- [ ] : Auto generate barcode
