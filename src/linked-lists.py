
class Link:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

	def link(self, value):
		new_link = Link(value)
		self.next = new_link
		return new_link

	def __repr__(self):
		return "Link({0!r},{1!r})".format(self.value, self.next)


class LinkedList:
	def __init__(self, llist = None):
		self.head = llist

	def prepend(self, value):
		self.head = Link(value, self.head)

	def __repr__(self):
		return "LinkedList({!r})".format(self.head)

llist = LinkedList()
for val in "ABCD"[::-1]:
	llist.prepend(val)
print(llist)

def reverse_llist(llist):
	links = llist.head
	res = None
	while links is not None:
		head = links
		links = head.next
		head.next = res
		res = head
	return LinkedList(res)

x = reverse_llist(llist)
print(x)
