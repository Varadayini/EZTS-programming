def insert_max_heap(heap, value):
    heap.append(value) 
    index = len(heap) -1
    while index > 0:
        parent_index = (index ) // 2 
        if heap[index] > heap[parent_index]: 
            heap[index],heap[parent_index]=heap[parent_index],heap[index]
            index = parent_index  
        else:
            break
heap=[100,80,90,60,50,70,40]

print("before",heap)

insert_max_heap(heap,85)
insert_max_heap(heap,10)


print("after",heap)