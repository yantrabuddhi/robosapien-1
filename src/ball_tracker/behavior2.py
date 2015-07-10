import owyl
from owyl import blackboard
class behavior:
    def __init__(self,bb):
        self.blackboard=bb#blackboard.Blackboard("behavior")
        #rospy.loginfo (self.blackboard["stt"])
        self.main_tree=self.create_main_tree()
        #while not rospy.is_shutdown():
        #    self.main_tree.next()

    def create_main_tree(self):
        tree=owyl.repeatAlways(owyl.sequence(self.printOne(),self.printTwo(),self.printThree()))
        return owyl.visit(tree,blackboard=self.blackboard)
    
    @owyl.taskmethod
    def printOne(self,**kwargs):
        self.one()
        yield True
        
        #yield True
    
    @owyl.taskmethod
    def printTwo(self, **kwargs):
        # yield False
        test=self.two()
        yield test
    
    @owyl.taskmethod
    def printThree(self,**kwargs):
        # yield False
        self.three()
        yield True

    def one(self,**kwargs):
        self.blackboard["x"]=float(raw_input("Please enter x: "))
        self.blackboard["y"]=float(raw_input("please enter y: "))

    def two(self,**kwargs):
        print "I'm now working calculating the sum!"
        try:
            self.blackboard["z"]=self.blackboard["x"]/self.blackboard["y"]
            return True
        except ZeroDivisionError,e:
            self.blackboard["z"]=0.0
            return None
    def three(self,**kwargs):
        print "The sum of "+str(self.blackboard["x"])+ " and " + str(self.blackboard["y"]) + " is: "+str(self.blackboard["z"])


if __name__=="__main__":
    
    board=blackboard.Blackboard(value="behavior")
    board["x"]=0 # 60 seconds
    board["y"]=0
    board["z"]=0
    

    be=behavior(board)
    be_tree=be.main_tree
    
    for i in range(6):
        be_tree.next()
    
        #rate.sleep()
    #rospy.loginfo("bye")
