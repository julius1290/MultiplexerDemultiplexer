import SystemBuilder


class Assembler:

    sysbuilder: SystemBuilder
    command_dict: {}
    register_dict: {}

    def __init__(self, builder: SystemBuilder):
        self.sysbuilder = builder
        self.command_dict = {
            "LD" : "001",
            "LDI" : "010",
            "ADDI" : "011",
            "ST" : "100",
            "COUT" : "101",
            "CP" : "000",
            "EXT" : "111"
        }
        self.register_dict = {
            "R0" : "00",
            "R1" : "01",
            "R2" : "10",
            "R3" : "11"
        }

    def readcommands(self):
        print("Please give command, type 'enter' to run programm:")
        console_input = input()
        input_list = list(console_input.split(','))
        op_code = self.get_command(input_list[0])
        print(op_code)

    def get_command(self, command):
        op_code = self.command_dict[command]
        return op_code