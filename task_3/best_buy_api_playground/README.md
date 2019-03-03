|Endpoint| Test                                                               | Link                                                            | Priority  |
|--------| :----------------------------------------------------------------  |:--------------------------------------------------------------- | :---------|
|Products||||
|        | Get product with ID of 9132294 (sku)	                              | <http://localhost:3030/products/9132294>                        | High      |
|        | Get all products              		                              | <http://localhost:3030/products>                                |   $12     |
|        | Get all products, limit to 1 result	                              | <http://localhost:3030/products?$limit=1>                       |    $1     |
|        | Get all products, skip to the 25,001th result                      | <http://localhost:3030/products?$skip=25000>                    |    $1     |
|        | Get all products, sort by highest price (descending)               | <http://localhost:3030/products?$sort[price]=-1>                |    $1     |
|        | Get all products, sort by highest price (ascending)                | <http://localhost:3030/products?$sort[price]=1>                 |    $1     |
|        | Get all products, but only show the name and price in the result   | <http://localhost:3030/products?$select[]=name&$select[]=price> |    $1     |
|        | Get products of type HardGood                                      | <http://localhost:3030/products?type=HardGood>                  |    $1     |
|        | Get products less than or equal to $1.00                           | <http://localhost:3030/products?price[$lte]=1>                  |    $1     |
|        | Get products that have 'star wars' in the name and are under $30   | <http://localhost:3030/products?name[$like]=*star+wars*&price[$lt]=30> |    $1     |
|        | Get products that are either $0.99 or $1.99                        | <http://localhost:3030/products?price[$in]=0.99&price[$in]=1.99> |    $1     |
|        | Get products that have a shipping price of more than $10           | <http://localhost:3030/products?shipping[$gt]=10>                |    $1     |
|        | Get products that are not HardGood or Software                     | <http://localhost:3030/products?type[$nin][]=HardGood&type[$nin][]=Software> |    $1     |
|        | Get products that are in category name "Coffee Pods"               | <http://localhost:3030/products?category.name=Coffee%20Pods>     |    $1     |
|        | Get products that are in category ID "abcat0106004" (TV Mounts)    | <http://localhost:3030/products?category.id=abcat0106004>        |    $1     |

