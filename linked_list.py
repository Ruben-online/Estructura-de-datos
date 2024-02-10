class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print('None')

    def insert_into_empty_list(self, element):
        newNode = Node(element)
        newNode.next = self.head
        self.head = newNode

    def replace_element(self, old_element, new_element):
        current = self.head
        while current is not None:
            if current.data == old_element:
                current.data = new_element
                break
            current = current.next

    def delete_from_beginning(self):
        if self.head is None:
            print('La lista simplemente enlazada esta vacia, no se puede eliminar')
        else:
            node = self.head
            self.head = self.head.next
            del node

    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return current_node.data
            current_node = current_node.next
        return None

class Customer:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Sale:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

costumers_list = LinkedList()

costumers_list.insert_into_empty_list(Customer('Rene', 'Mancilla', '12345678'))
costumers_list.insert_into_empty_list(Customer('Maria', 'Lopez', '87654321'))
costumers_list.insert_into_empty_list(Customer('Irma', 'Perez', '11223344'))

products_list = LinkedList()

products_list.insert_into_empty_list(Product('Lampara', '450'))
products_list.insert_into_empty_list(Product('Cortina', '200'))
products_list.insert_into_empty_list(Product('Mesa de noche', '300'))

print('Clientes')
costumers_list.print_list()

print('Productos')
products_list.print_list()

