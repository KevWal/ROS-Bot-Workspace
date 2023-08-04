#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include <sensor_msgs/JointState.h>
#include <geometry_msgs/Twist.h>

double vx = 0.0;
double vth = 0.0;


void odomCallback( const geometry_msgs::TwistConstPtr& cmd_vel) {
	vx = cmd_vel->linear.x;
	vth = cmd_vel->angular.z;
}


int main( int argc, char** argv) {

	ros::init(argc, argv, "fake_odom");

	ros::NodeHandle n;
	ros::Publisher odom_pub = n.advertise<nav_msgs::Odometry>("odom", 50);
	ros::Subscriber sub = n.subscribe("cmd_vel", 1000, odomCallback);

	double x = 0.0;
	double y = 0.0;
	double th = 0.0;

	ros::Time current_time, last_time;
	current_time = ros::Time::now();
	last_time = ros::Time::now();

	ros::Rate rate (500);
  
	while (n.ok()) {
		current_time = ros::Time::now();

		double dt = (current_time - last_time).toSec();
		double delta_x = vx * cos(th) * dt;
		double delta_y = vx * sin(th) * dt;
		double delta_th = vth * dt;

		x += delta_x ;
		y += delta_y ;
		th += delta_th;

		geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(th);

		// publis /odom
		nav_msgs::Odometry odom;
		odom.header.stamp = current_time;
		odom.header.frame_id = "odom";
		odom.child_frame_id = "base_link";
		odom.pose.pose.position.x = x;
		odom.pose.pose.position.y = y;
		odom.pose.pose.position.z = 0.0;
		odom.pose.pose.orientation = odom_quat;
		odom.twist.twist.linear.x = vx;
		odom.twist.twist.angular.z = vth;
		odom_pub.publish(odom);
		
		last_time = current_time;
		
		ros::spinOnce();
		rate.sleep();
	}
}
