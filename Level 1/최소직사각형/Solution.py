def solution(sizes): 
    sizes = [sorted(size, reverse=True) for size in sizes] 
    
    widths = [size[0] for size in sizes] 
    heights = [size[1] for size in sizes] 
    
    width, height = max(widths), max(heights) 
    result = width * height 
    
    return result