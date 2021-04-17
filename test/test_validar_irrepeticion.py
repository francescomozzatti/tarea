from prog.nums_irrepetibles import nums_irrepetibles

def test_nums_irrepetibles():
    mi_carton=((1,2,3,4,5,6,7,8,9,),(10,11,12,13,14,15,0,0,0,),(0,61,0,0,0,70,0,0,0,))     

    assert nums_irrepetibles(mi_carton)==1