#!/usr/bin/env python
import os
import sys

import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", 
                                                "scripts")))
from topic_compare import ROSTopicCompare

import rospy
import time

def eps_equal(a, b, err=0.001):
    return abs(a - b) < err

# subscribing three topics
#   * /origin
#   * /origin (the same topic)
#   * /half
class TestTopicCompare(unittest.TestCase):
    def test_same_topic(self):
        current_time = time.time()
        self.assertTrue(eps_equal(tc.getTotalBytes(0) / (current_time - tc.getStartTime(0)),
                                  tc.getTotalBytes(1) / (current_time - tc.getStartTime(1)), 1))
    def test_half_topic(self):
        current_time = time.time()
        rospy.loginfo(tc.getTotalBytes(0) / (current_time - tc.getStartTime(0)))
        rospy.loginfo(tc.getTotalBytes(2) * 2 / (current_time - tc.getStartTime(2)))

        self.assertTrue(eps_equal(tc.getTotalBytes(0) / (current_time - tc.getStartTime(0)),
                                  tc.getTotalBytes(2) * 2 / (current_time - tc.getStartTime(2)), 1))

if __name__ == "__main__":
    import rostest
    rospy.init_node("test_topic_compare")
    tc = ROSTopicCompare()
    tc.registerTopic("/origin")
    tc.registerTopic("/origin")
    tc.registerTopic("/half")
    rospy.loginfo("wait 30sec to acuumulate topics...")
    rospy.sleep(30)
    rostest.rosrun("jsk_topic_tools", "test_topic_compare", TestTopicCompare)


