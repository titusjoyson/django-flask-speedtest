### 1000000

#### workers: 4
#### total db rec: 10,00,000
#### total req: 2000
#### concurrency: 10 

 |                  | Django |  Flask  |
 |------------------|--------|---------|
 | Pre defined data | 870.41 | 1613.45 |
 | nested iteration |  45.52 |   48.46 |
 | count            |  22.42 |   24.35 |
 | list from db     |  19.69 |   20.06 |
 | pagination       |  11.04 |   12.46 |
 | aggregate        |  13.36 |   14.05 |
 | create           | 275.29 |  526.81 |
 | save             | 232.61 |  559.55 |
 | update           | 262.07 |  991.19 |