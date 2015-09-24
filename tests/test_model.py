import unittest
from pusher.model import Model
import math
import numpy as np

class TestModel(unittest.TestCase):
    def test_fk(self):
        links = [1,1]
        m = Model(links)
        # test joint 1-1 
        X = m.forward_kinematic([0,0])
        np.testing.assert_almost_equal(X,[2,0,0])
        # test joint 1-2
        X = m.forward_kinematic([math.pi/2.,0])
        np.testing.assert_almost_equal(X,[0,2,0])
        # test joint 1-3
        X = m.forward_kinematic([-math.pi/2.,0])
        np.testing.assert_almost_equal(X,[0,-2,0])
        #test joint 2-1
        X = m.forward_kinematic([0,math.pi/2.])
        np.testing.assert_almost_equal(X,[1,1,0])
        #test joint 2-1
        X = m.forward_kinematic([0,-math.pi/2.])
        np.testing.assert_almost_equal(X,[1,-1,0])
        #test coupled 1
        X = m.forward_kinematic([math.pi/2.,math.pi/2.])
        np.testing.assert_almost_equal(X,[-1,1,0])
        #test coupled 2
        X = m.forward_kinematic([-math.pi/2.,math.pi/2.])
        np.testing.assert_almost_equal(X,[1,-1,0])
        #test coupled 3
        X = m.forward_kinematic([math.pi/2.,-math.pi/2.])
        np.testing.assert_almost_equal(X,[1,1,0])
        #test coupled 4
        X = m.forward_kinematic([-math.pi/2.,-math.pi/2.])
        np.testing.assert_almost_equal(X,[-1,-1,0])

    def test_ik(self):
        links = [1,1]
        m = Model(links)
        for i in range(100):
            # create end effector random pose
            X = np.random.uniform(-1,1,2)
            X = np.append(X,0)
            # calculate inverse kinematic
            q = m.inverse_kinematic(X)
            # calculate forward kinematic from obtained q
            X2 = m.forward_kinematic(q)
            # assert equality between X and X2
            np.testing.assert_almost_equal(X,X2,decimal=3)

    def test_plot(self):
        links = [2,3]
        m = Model(links)
        m.set_current_joints([math.pi/2.,math.pi/2.])
        m.plot_model()
        
    # def test_random_model(self):
    #     nb_joints = np.random.randint(5)
    #     links = np.random.uniform(0,1,nb_joints)
    #     # create the model and check the ik
    #     m = Model(links)
    #     for i in range(100):
    #         # create end effector random pose
    #         X = np.random.uniform(-1,1,2)
    #         X = np.append(X,0)
    #         # calculate inverse kinematic
    #         q = m.inverse_kinematic(X)
    #         # calculate forward kinematic from obtained q
    #         X2 = m.forward_kinematic(q)
    #         # assert equality between X and X2
    #         np.testing.assert_almost_equal(X,X2,decimal=3)

if __name__ == '__main__':
    unittest.main()