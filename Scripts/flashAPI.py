''' LOOKUP EXAMPLE
from amazon.api import AmazonAPI
>>> amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
>>> product = amazon.lookup(ItemId='B00EOE0WKQ')
>>> product.title
'Amazon Fire Phone, 32GB (AT&T)'
>>> product.price_and_currency
(199.0, 'USD')
>>> product.ean
'0848719035209'
>>> product.large_image_url
'http://ecx.images-amazon.com/images/I/51BrZzpkWrL.jpg'
>>> product.get_attribute('Publisher')
'Amazon'
>>> product.get_attributes(['ItemDimensions.Width', 'ItemDimensions.Height'])
{'ItemDimensions.Width': '262', 'ItemDimensions.Height': '35'}
'''


''' CREATE AND MANIPULATE SHOPPPING bCARTS EXAMPLE
from amazon.api import AmazonAPI
>>> amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
>>> product = amazon.lookup(ItemId="B0016J8AOC")
>>> item = {'offer_id': product.offer_id, 'quantity': 1}
>>> cart = amazon.cart_create(item)
>>> fetched_cart = amazon.cart_get(cart.cart_id, cart.hmac)
>>> another_product = amazon.lookup(ItemId='0312098286')
>>> another_item = {'offer_id': another_product.offer_id, 'quantity': 1}
>>> another_cart = amazon.cart_add(another_item, cart.cart_id, cart.hmac)
>>> cart_item_id = None
>>> for item in cart:
>>>     cart_item_id = item.cart_item_id
>>> modify_item = {'cart_item_id': cart_item_id, 'quantity': 3}
>>> modified_cart = amazon.cart_modify(item, cart.cart_id, cart.hmac)
>>> cleared_cart = amazon.cart_clear(cart.cart_id, cart.hmac)
'''
import bottlenose
amazon = bottlenose.Amazon("AKIAJXA5GIJNO3U2A65", "aDQYVdQ7ZMCBA2m40XoFYcOg+bz9Yrz2edNgIe8c","needthisforsc-20")
