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
|Stores||||
|        | Get all stores              		                                  | 200 | High   	 |
|        | Get all stores, limit to 1 result	                              | 200 | High       |
|        | Get all stores, skip to the 25,001th result                        | 200 | High       |
|        | Create new store with valid data							          | 200 | High       |
|        | Create new store with invalid length for mandatory field name 	  | 400 | High       |
|        | Create new store with invalid length for mandatory field address   | 400 | High       |
|        | Create new store with invalid length for mandatory field city      | 400 | High       |
|        | Create new store with invalid length for mandatory field state     | 400 | High       |
|        | Create new store with invalid length for mandatory field zip       | 400 | High       |
|        | Delete a store with a valid id 	  							      | 200 | High       |
|        | Delete a store with an invalid id 	  							  | 400 | High       |
|        | Get a store with a valid id 	  							          | 200 | High       |
|        | Get a store with an invalid id 	  							      | 400 | High       |
|        | Update a store with a valid id and field data	  				  | 200 | High       |
|        | Update a store with an invalid id and valid field data             | 400 | High       |
|        | Update a store with a valid id and invalid field data              | 400 | High       |
|Services||||
|        | Get all services              		                              | 200 | High   	 |
|        | Get all services, limit to 1 result	                              | 200 | High       |
|        | Get all services, skip to the 3rd result                           | 200 | High       |
|        | Create new service with valid data							      | 200 | High       |
|        | Create new service with invalid data							      | 400 | High       |
|        | Delete a service with a valid id 	  							  | 200 | High       |
|        | Delete a service with an invalid id 	  							  | 400 | High       |
|        | Get a service with a valid id 	  							      | 200 | High       |
|        | Get a service with an invalid id 	  							  | 400 | High       |
|Categories||||
|        | Get all categories              		                              | 200 | High   	 |
|        | Get all categories, limit to 1 result	                          | 200 | High       |
|        | Get all categories, skip to the 10,001th result                    | 200 | High       |
|        | Create new category with valid data							      | 200 | High       |
|        | Create new category with invalid length for mandatory field name   | 400 | High       |
|        | Create new category with invalid length for mandatory field id 	  | 400 | High       |
|        | Delete a category with a valid id 	  							  | 200 | High       |
|        | Delete a category with an invalid id  							  | 400 | High       |
|        | Get a category with a valid id 	  							      | 200 | High       |
|        | Get a category with an invalid id 	  							  | 400 | High       |
|        | Get a category with a valid name 	  							  | 200 | High       |
|        | Get a category with an invalid name 	  							  | 400 | High       |
|        | Update a category with a valid id and field data	  				  | 200 | High       |
|        | Update a category with an invalid id and valid field data          | 400 | High       |
|        | Update a category with a valid id and invalid field data           | 400 | High       |
|Utilities||||
|        | Get current version of the API Playground being run               | 200 | High   	 |
|        | Get positive healthcheck status                                   | 200 | High   	 |
|        | Get negative healthcheck status                                   | 200 | High   	 |