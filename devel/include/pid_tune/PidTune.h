// Generated by gencpp from file pid_tune/PidTune.msg
// DO NOT EDIT!


#ifndef PID_TUNE_MESSAGE_PIDTUNE_H
#define PID_TUNE_MESSAGE_PIDTUNE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pid_tune
{
template <class ContainerAllocator>
struct PidTune_
{
  typedef PidTune_<ContainerAllocator> Type;

  PidTune_()
    : Kp(0)
    , Kd(0)
    , Ki(0)
    , Kp_z(0)  {
    }
  PidTune_(const ContainerAllocator& _alloc)
    : Kp(0)
    , Kd(0)
    , Ki(0)
    , Kp_z(0)  {
  (void)_alloc;
    }



   typedef int16_t _Kp_type;
  _Kp_type Kp;

   typedef int16_t _Kd_type;
  _Kd_type Kd;

   typedef int16_t _Ki_type;
  _Ki_type Ki;

   typedef int16_t _Kp_z_type;
  _Kp_z_type Kp_z;





  typedef boost::shared_ptr< ::pid_tune::PidTune_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pid_tune::PidTune_<ContainerAllocator> const> ConstPtr;

}; // struct PidTune_

typedef ::pid_tune::PidTune_<std::allocator<void> > PidTune;

typedef boost::shared_ptr< ::pid_tune::PidTune > PidTunePtr;
typedef boost::shared_ptr< ::pid_tune::PidTune const> PidTuneConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pid_tune::PidTune_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pid_tune::PidTune_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace pid_tune

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'pid_tune': ['/home/akio/catkin_ws/src/pid_tune/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::pid_tune::PidTune_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pid_tune::PidTune_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pid_tune::PidTune_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pid_tune::PidTune_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pid_tune::PidTune_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pid_tune::PidTune_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pid_tune::PidTune_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0c2da60e6140b798a4857caa11a7c01a";
  }

  static const char* value(const ::pid_tune::PidTune_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0c2da60e6140b798ULL;
  static const uint64_t static_value2 = 0xa4857caa11a7c01aULL;
};

template<class ContainerAllocator>
struct DataType< ::pid_tune::PidTune_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pid_tune/PidTune";
  }

  static const char* value(const ::pid_tune::PidTune_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pid_tune::PidTune_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 Kp\n\
int16 Kd\n\
int16 Ki\n\
int16 Kp_z\n\
\n\
";
  }

  static const char* value(const ::pid_tune::PidTune_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pid_tune::PidTune_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Kp);
      stream.next(m.Kd);
      stream.next(m.Ki);
      stream.next(m.Kp_z);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PidTune_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pid_tune::PidTune_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pid_tune::PidTune_<ContainerAllocator>& v)
  {
    s << indent << "Kp: ";
    Printer<int16_t>::stream(s, indent + "  ", v.Kp);
    s << indent << "Kd: ";
    Printer<int16_t>::stream(s, indent + "  ", v.Kd);
    s << indent << "Ki: ";
    Printer<int16_t>::stream(s, indent + "  ", v.Ki);
    s << indent << "Kp_z: ";
    Printer<int16_t>::stream(s, indent + "  ", v.Kp_z);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PID_TUNE_MESSAGE_PIDTUNE_H