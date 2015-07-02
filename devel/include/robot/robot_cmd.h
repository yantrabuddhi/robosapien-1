// Generated by gencpp from file robot/robot_cmd.msg
// DO NOT EDIT!


#ifndef ROBOT_MESSAGE_ROBOT_CMD_H
#define ROBOT_MESSAGE_ROBOT_CMD_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace robot
{
template <class ContainerAllocator>
struct robot_cmd_
{
  typedef robot_cmd_<ContainerAllocator> Type;

  robot_cmd_()
    : cmd()
    , duration_10ms(0)  {
    }
  robot_cmd_(const ContainerAllocator& _alloc)
    : cmd(_alloc)
    , duration_10ms(0)  {
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _cmd_type;
  _cmd_type cmd;

   typedef uint8_t _duration_10ms_type;
  _duration_10ms_type duration_10ms;




  typedef boost::shared_ptr< ::robot::robot_cmd_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robot::robot_cmd_<ContainerAllocator> const> ConstPtr;

}; // struct robot_cmd_

typedef ::robot::robot_cmd_<std::allocator<void> > robot_cmd;

typedef boost::shared_ptr< ::robot::robot_cmd > robot_cmdPtr;
typedef boost::shared_ptr< ::robot::robot_cmd const> robot_cmdConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robot::robot_cmd_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robot::robot_cmd_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robot

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/jade/share/std_msgs/cmake/../msg'], 'robot': ['/home/abeni/rob/src/robot/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robot::robot_cmd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robot::robot_cmd_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot::robot_cmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot::robot_cmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot::robot_cmd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot::robot_cmd_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robot::robot_cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0dc039100dce1fd03db0d90732bfee7d";
  }

  static const char* value(const ::robot::robot_cmd_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0dc039100dce1fd0ULL;
  static const uint64_t static_value2 = 0x3db0d90732bfee7dULL;
};

template<class ContainerAllocator>
struct DataType< ::robot::robot_cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robot/robot_cmd";
  }

  static const char* value(const ::robot::robot_cmd_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robot::robot_cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string cmd\n\
uint8 duration_10ms\n\
";
  }

  static const char* value(const ::robot::robot_cmd_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robot::robot_cmd_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.cmd);
      stream.next(m.duration_10ms);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct robot_cmd_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robot::robot_cmd_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robot::robot_cmd_<ContainerAllocator>& v)
  {
    s << indent << "cmd: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.cmd);
    s << indent << "duration_10ms: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.duration_10ms);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOT_MESSAGE_ROBOT_CMD_H
