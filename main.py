from Assembler import Assembler
from SystemBuilder import ProcessorSystem


sysbuilder = ProcessorSystem()
assembler = Assembler(sysbuilder)
assembler.readcommands()
sysbuilder.run()