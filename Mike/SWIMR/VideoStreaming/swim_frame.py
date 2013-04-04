

class SwimFrame():
    '''
    class to hold frame data
    '''
    def __init__(self,height,width):
        self.HEIGHT = height
        self.FRAME = width
        self.string = str()
        self.raw = None
        self.matrix = None
        self.compressed = None
        self.rows = 0
        self.cols = 0
        self.step = 0
        self.len = 0
        self.valid = False
        self.data = {}
        self.new = False
        
    def get_frame_data(self):
        self.new = False
        return self.data
        
    def set_frame_data(self, data=dict()):
        try:
            self.frame_data = data
            self.string = data['str']
            self.rows = data['rows']
            self.step = data['step']
            self.cols = data['cols']
            self.len = data['len']
            self.new = True
        except KeyError:
            print "bad dict"

            
            
        
        
        
    
    
        
