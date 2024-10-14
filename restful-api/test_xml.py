from task_03_http_server import serialize_to_xml, deserialize_from_xml

# Test serialization
test_dict = {'name': 'John', 'age': '30', 'city': 'New York'}
serialize_to_xml(test_dict, 'test_data.xml')

# Test deserialization
result = deserialize_from_xml('test_data.xml')
print(result)
