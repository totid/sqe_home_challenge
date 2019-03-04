|Endpoint| Test                                                               | Expected response                                                            | Priority  |
|--------| :----------------------------------------------------------------  |:--------------------------------------------------------------- | :---------|
|Products||||
|        | Get all products              		                              | 200 | High   	 |
|        | Get all products, limit to 1 result	                              | 200 | High       |
|        | Get all products, skip to the 25,001th result                      | 200 | High       |
|        | Create new Product with valid data							      | 200 | High       |
|        | Create new Product with invalid length for mandatory field name 	  | 400 | High       |
|        | Create new Product with invalid length for mandatory field type 	  | 400 | High       |
|        | Create new Product with invalid length for mandatory field price   | 400 | High       |
|        | Delete a product with a valid id 	  							  | 200 | High       |
|        | Delete a product with an invalid id 	  							  | 400 | High       |
|        | Get a product with a valid id 	  							      | 200 | High       |
|        | Get a product with an invalid id 	  							  | 400 | High       |
|        | Update a product with a valid id and field data	  				  | 200 | High       |
|        | Update a product with an invalid id and valid field data           | 400 | High       |
|        | Update a product with a valid id and invalid field data            | 400 | High       |
