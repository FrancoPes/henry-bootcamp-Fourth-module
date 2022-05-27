

#? QUE ES HIVE?
# Hive is a data warehousing infrastructure based on Apache Hadoop
# Hadoop provides massive scale out and fault tolerance capabilities for data storage and processing on commodity hardware.
# Hive is designed to enable easy data summarization
#It provides SQL which enables users to do ad-hoc querying, summarization and data analysis easily.
# Hive's SQL gives users multiple places to integrate their own functionality to do custom analysis, such as User Defined Functions (UDFs).

#? QUE NO ES HIVE?
#Hive is not designed for online transaction processing. 
# It is best used for traditional data warehousing tasks.

#? HIVE ORGANIZACION
### >>> Databases:  Namespaces function to avoid naming conflicts for tables, views, partitions, columns, and so on. 
# Databases can also be used to enforce security for a user or group of users.

### >>> Tables: Homogeneous units of data which have the same schema. 

### >>> Partitions: Each Table can have one or more partition Keys which determines how the data is stored. 
#allow the user to efficiently identify the rows that satisfy a specified criteria
#for example, a date_partition of type STRING and country_partition of type STRING. Each unique value of the partition keys defines 
# a partition of the Table. For example, all "US" data from "2009-12-23" is a partition of the page_views table. Therefore,
# if you run analysis on only the "US" data for 2009-12-23, you can run that query only on the relevant partition of the table, 
# thereby speeding up the analysis significantly.
#Note however, that just because a partition is named 2009-12-23 does not mean that it contains all or only data from that date; partitions are named after dates for convenience; it is the user's job to guarantee the relationship between partition name and data content
#Partition columns are virtual columns, they are not part of the data itself but are derived on load.

### >>> Buckets (or Clusters):  Data in each partition may in turn be divided into Buckets based on the value of a hash function
# of some column of the Table
# For example the page_views table may be bucketed by userid,
# which is one of the columns, other than the partitions columns, of the page_view table
# These can be used to efficiently sample the data

#! Note that it is not necessary for tables to be partitioned or bucketed, but these abstractions allow the system to prune large quantities of data during query processing, resulting in faster query execution

#? TIPOS DE DATOS
# Estan los simnples y los complejos
# simples; mismos de siempre

# Complex Types
### >>> structs: the elements within the type can be accessed using the DOT (.) notation. 
# For example, for a column c of type STRUCT {a INT; b INT}, the a field is accessed by the expression c.a


### >>> Maps (key-value tuples): The elements are accessed using ['element name'] notation. 
# For example in a map M comprising of a mapping from 'group' -> gid the gid value can be accessed using M['group']


### >>> Arrays (indexable lists): The elements in the array have to be in the same type.
# Elements can be accessed using the [n] notation where n is an index (zero-based) into the array.
# For example, for an array A having the elements ['a', 'b', 'c'], A[1] retruns 'b'.



#? LANGUAGE
#




#MODOS DE HIVE
# UN SOLO NODO
# VARIOS NODOS >> MAS EFICIENTE

#














