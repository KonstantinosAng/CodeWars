# see https://www.codewars.com/kata/515bb423de843ea99400000a/train/python

from math import floor

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
    self.collection = collection
    self.items_per_page = items_per_page
    self.pages = 0
        
  # returns the number of items within the entire collection
  def item_count(self):
    return len(self.collection)
  
  def page_count(self):
    pages = floor(len(self.collection) / self.items_per_page)
    if len(self.collection) % self.items_per_page == 0: self.pages = pages
    else: self.pages = pages + 1
    return self.pages     
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
    if page_index >= self.pages: return -1
    if len(self.collection) % self.items_per_page == 0: return self.items_per_page
    else: return self.items_per_page if page_index < self.pages - 1 else len(self.collection) - self.items_per_page * (self.pages - 1)           

  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
    if item_index >= len(self.collection) or item_index < 0: return -1
    div = floor(item_index / self.items_per_page)
    return div
  
  

from TestFunction import Test

test = Test(None)
collection = range(1,25)
helper = PaginationHelper(collection, 10)

test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')
test.assert_equals(helper.page_item_count(3), 4, 'item_count returned incorrect value')