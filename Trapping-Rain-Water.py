array = [ 3 , 0 , 0 , 2 , 0 , 4 ]

array2 = array .copy ()
array2 .remove ( max ( array2 ) )
water_collected = [ max ( array2 ) ] * len ( array )

for index in range ( 0 , len ( array ) ) :
    water_collected [ index ] -= array [ index ]
    if water_collected [ index ] < 0 : water_collected [ index ] = 0
    
print ( sum ( water_collected ) )