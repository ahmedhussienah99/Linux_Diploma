def create_header(class_name):
    class_header=f'''
        
    #ifndef {class_name.upper()}_H
    #define{class_name.upper()}_H
    
    class {class_name}
    {{
        public:
                {class_name}();
                ~{class_name}();

    
    
    }}


    #endif  
    '''
    return class_header

def create_cpp(class_name):
    class_cpp=f'''
        
    #include "{class_name}.h"
    #include <iostream>
    using namespace std;
    {class_name}::{class_name}() {{
    cout << "constructor" ;
    }}

    {class_name}::~{class_name}() {{
    cout << "Destructor" ;
    }}

    '''
    return class_cpp

def create_header_file(class_name,data):
    with open(f"{class_name}.h", 'w') as header:
        header.write(data)

def create_cpp_file(class_name,data):
    with open(f"{class_name}.cpp", 'w') as cpp:
        cpp.write(data)

class_name = input("the name of the class: ")

header_data=create_header(class_name)
cpp_data=create_cpp(class_name)

create_header_file(class_name,header_data)
create_cpp_file(class_name,cpp_data)