#  Class Diagram in UML

"""How could we represent some system/task?
● Natural text (Functional Requirements) to describe it!
● Just code the system (Like AskMe Projects)
● Draw a diagram for it!"""

"""Unified Modeling Language (UML)
● Standardized modeling language for Software visualization purposes
● Imagine a system that consists of 
    3 subsystems, 
    each sub-system consists of ~10 components, 
    each component has ~100 classes
● We need different ways to communicate this system details with others
○ Written documents are one aspect
○ Another is diagrams to visualize different aspects of the system
● Class Diagram is one of the important UML diagrams"""

"""UML Tools
● lucidchart (online)
● Diagrams (online)
● ArgoUML
● Visual Paradigm
● StarUML
● Microsoft visio"""

# Classes Relationship

"""Classes Relationship
● In a complex systems, we have several classes that have relationships
● There are 4 types of relations
○ Association
■ User borrows a book
■ User add_item to shopping cart
○ Aggregation
■ Department has employes
○ Composition
■ Car has an engine / wheels
■ University has departments
○ Generalization (Inheritance)
■ Circle is a shape
■ Bicycle is a vehicle"""

# Composition Relationship

"""Composition Relationship
● A car has an engine
○ Engine has no value to be used independently!
■ If used, then by a car
○ Same for wheels
● A room has walls / ceiling / floor
○ If there is a used wall, it must be in a specific room"""

"""Composition Relationship
● It is a strong “has a” relationship (consists of)
○ Whole vs Part relationship, but strong (ownership)
○ The whole creates/destroys the parts. 
■ Car object creates engine/wheel objects
○ Part is used only by the whole
■ The engine is not shared between 2 cars
○ The part has no life of itself 
● Composition allows reusability"""

# Aggregation Relationship

"""Aggregation Relationship
● It is a weak “has a” relationship
○ Whole vs Part relationship, but weak (no ownership)
■ E.g. Department has professors. If department is shutdown, they are still 
professors/exist
○ Whole class or some other class can create the part object
○ If whole object is destroyed, the part may still be in use by others"""

# Generalization Relationship

"""Generalization (Inheritance)
● It represents Is-a relationship
● Student is-a person. Teacher is-a person. Dean is-a person
○ So some common variables/functions + some unique variables/functions
● Circle is-a shape. 
○ Rectangle is-a shape. Triangle is-a shape. 
● Software Engineer is-an employee. 
○ Manager is-an employee. 
○ Office Boy is-an employee
● Apple is-a fruit. Orange is-a fruit. Watermelon is-a fruit
● (Wagon / Bicycle / Motor vehicle / Railed vehicle) is-a vehicle"""

# Multiplicity

"""Multiplicity
● Multiplicity = Specify cardinality 
(number of elements)
○ Each center will have only 1 lobby
○ But there is at least 1 bathroom
● We can enhance diagram with such information"""

"""Back to Associations
● One-to-one Associations     
○ Each citizen has a single national ID
● One-to-many Associations
○ Car class has 4 wheels
○ Customer has Bank Account(s)
● Many-to-many Associations 
○ Student has vector<courses>
○ Course has vector<students>
● Optional reading"""

# Relationships & Multiplicity

"""Multiplicity: University Example
Img Src
● Notice the diagram consistency between relationships and multiplicity
● University is composed of a department
○ This means a department must belong to a single whole
○ Multiplicity must be exactly 1
● Department is aggregated of professors
○ This means some professor may not belong to a department
○ Multiplicity must be at least zero
● Tip: Put 1 beside black diamond and at least zero at the empty diamond. Check logic"""

"""Think about relationships & multiplicity
● Student, Course
○ Student registers in course: Many-to-Many Relationship
■ Student registers in many courses. Course is attended by many students
● Customer, Bank Account, Saving Account, Checking Account
● Vehicle, Car, Seat, Engine, Door, Driver, Passenger, Gasoline, Garage
● Google Forms, Question, Answer, Options
● Computer, CPU, motherboard, Cache, Memory, 
● Person, Student, Professor
● Patient,  Patient Record
● Food Order, line items
● Project, Project Manager"""

# UML in Practice

"""Class Diagram: UML Best Practice
● Many diagrams can be so useless / hard to get
● Future: 
reading 
reading
● 5 Tips
○ Less is more     (Providing a lot just confuse)
○ No Crossings    (Don’t cross lines)
○ Orthogonality    (All lines vertical or horizontal)
○ Parents Up       (Inheritance parent always above)
○ Tidy Up             (Clean view, e.g. alignments)"""

"""UML in Practice
● Some companies never/rarely use
○ Just use a whiteboard. Team brainstorms and draws to communicate thoughts
○ New employee? A bit trouble. Some high level explanation + code deep dive
● In many small projects (3-6 month), maybe no diagrams
● Big projects: create some high level diagrams
○ Most important: [Class - Sequence - State - Activity] Diagrams
● Agile challenge: Diagrams will be outdated soon due to rapid changes
● Tips
○ Learn the notations & diagrams. Think twice before creating diagram. Focus on high level
● Future readings
○ Reading reading reading"""

# Improving Design Skills

"""Class Diagram and Design skills
● Class Diagram helps seeing the big picture
● Sketch your initial UML diagram
● Start coding your system
○ You will notice a lot is missing: Critical variables and functions
● Redraw your final UML
○ Compare and notice differences
○ Ask yourself why I missed them
○ Iteratively learn from your mistakes
○ You are good = when you bridge the gap between your first & last design
○ It will take time!"""

