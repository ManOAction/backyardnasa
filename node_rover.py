"""This is the ROS rover node for a twin motor rover managed with a PWM motor controller.

# changelog
2021-11-29, JDL: Converting from full robot loop to just locomotion node.
2020-02-15, JDL: Creating stable loops and move commands
2019-11-24, JDL: First draft.

"""

from gpiozero import LED, Motor
from time import sleep

# ROS 2 Related Imports
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


# # Constants (move externaly to a config when you have time)
# ####################################################
vPinMotorWake = 17
vPinRMotF = 20
vPinRMotR = 21
vPinLMotF = 19
vPinLMotR = 26


# ___  ___                                    _
# |  \/  |                                   | |
# | .  . | _____   _____ _ __ ___   ___ _ __ | |_
# | |\/| |/ _ \ \ / / _ \ '_ ` _ \ / _ \ '_ \| __|
# | |  | | (_) \ V /  __/ | | | | |  __/ | | | |_
# \_|  |_/\___/ \_/ \___|_| |_| |_|\___|_| |_|\__|
#################################################

class MotionController:

    def __init__(self, PinMotorWake, PinRMotF, PinRMotR, PinLMotF, PinLMotR):
        self.RMotor = Motor(PinRMotF, PinRMotR)
        self.LMotor = Motor(PinLMotF, PinLMotR)
        self.MotorWake = LED(PinMotorWake)
        super().__init__()

    def move_forward(self, MoveTime, MoveSpeed=float("1")):
        print('Moving forward.')
        self.MotorWake.on()
        self.RMotor.forward(MoveSpeed)
        self.LMotor.forward(MoveSpeed)
        sleep(MoveTime)
        self.RMotor.stop()
        self.LMotor.stop()
        self.MotorWake.off()
        print('End moving forward.')
        return True

    def move_reverse(self, MoveTime, MoveSpeed=float("1")):
        print('Moving backwards.')
        self.MotorWake.on()
        self.RMotor.backward(MoveSpeed)
        self.LMotor.backward(MoveSpeed)
        sleep(MoveTime)
        self.RMotor.stop()
        self.LMotor.stop()
        self.MotorWake.off()
        return True

    def move_turnleft(self, MoveTime, MoveSpeed=float("1")):
        print('Turning left.')
        self.MotorWake.on()
        self.RMotor.forward(MoveSpeed)
        self.LMotor.backward(MoveSpeed)
        sleep(MoveTime)
        self.RMotor.stop()
        self.LMotor.stop()
        self.MotorWake.off()
        return True

    def move_turnright(self, MoveTime, MoveSpeed=float("1")):
        print('Turning right.')
        self.MotorWake.on()
        self.LMotor.forward(MoveSpeed)
        self.RMotor.backward(MoveSpeed)
        sleep(MoveTime)
        self.RMotor.stop()
        self.LMotor.stop()
        self.MotorWake.off()
        return True

    def stop(self):
        print('Motor controller shut off...')        
        self.MotorWake.off()
        return True


class MinimalSubscriber(Node):
    def __init__(self) -> None:
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'move',
            self.listener_callback,
            10
        )
        # self.subscription   arning  # What is this?  Is it a typo?

        self.rover = MotionController(vPinMotorWake, vPinRMotF, vPinRMotR, vPinLMotF, vPinLMotR)

    def listener_callback(self, msg):
        command = msg.data
        if command == 'forward':
            print('moving forward')
            self.rover.move_forward(1)
        elif command == 'backward':
            print('moving backward')
            self.rover.move_reverse(1)
        elif command == 'left':
            print('turning left')
            self.rover.turnleft(1)
        elif command == 'right':
            print('turning right')
            self.rover.turnright(1)



def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    minimal_subscriber.rover.stop()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()

    rclpy.shutdown()

    return True


if __name__ == '__main__':
    main()

print('I think we\'re done here.')
