import SystemBuilder


class Assembler:

    sysbuilder: SystemBuilder
    command_dict: {}
    register_dict: {}
    input_list: []
    op_code: str
    options: {}

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
        self.options = {
            "001" : self.build_ld,
            "010" : self.build_ldi,
            "011" : self.build_addi,
            "100" : self.build_st,
            "101" : self.build_cout,
            "000" : self.build_cp,
            "111" : self.build_ext
        }

    def readcommands(self):
        print("Please give command, type 'enter' to run programm:")
        console_input = input()
        self.input_list = list(console_input.split(','))
        self.op_code = self.get_command(self.input_list[0])
        command = self.options[self.op_code]()
        self.sysbuilder.flashcommand(command)
        if self.op_code != "111":
            self.readcommands()

    def get_command(self, command):
        op_code = self.command_dict[command]
        return op_code

    def build_ld(self):
        register = self.register_dict[self.input_list[1]]
        number = self.input_list[2]
        number = bin(int(number))[2:].zfill(8)
        command = self.op_code + register + "000" + number
        print(command)
        return command

    def build_ldi(self):
        register = self.register_dict[self.input_list[1]]
        data = self.input_list[2]
        highbit = "1"
        if data.isdigit():
            highbit = "0"
            data = highbit + bin(int(data))[2:].zfill(7)
            print(data)
        else:
            data = highbit + bin(ord(data))[2:].zfill(7)
            print(data)
        command = self.op_code + register + "000" + data
        print(command)
        return command

    def build_addi(self):
        register = self.register_dict[self.input_list[1]]
        number = self.input_list[2]
        number = bin(int(number))[2:].zfill(8)
        command = self.op_code + register + "000" + number
        print(command)
        return command

    def build_st(self):
        register = self.register_dict[self.input_list[1]]
        number = int(self.input_list[2])
        if number > 63:
            print("Number to high, max storage number is 63, please enter new storage number")
            self.input_list[2] = input()
            self.build_st()
        number = bin(int(number))[2:].zfill(8)
        command = self.op_code + register + "000" + number
        print(command)
        return command

    def build_cout(self):
        register = self.register_dict[self.input_list[1]]
        command = self.op_code + register + "00000000000"
        print(command)
        return command

    def build_cp(self):
        register = self.register_dict[self.input_list[1]]
        register_two = self.register_dict[self.input_list[2]]
        command = self.op_code + register_two + register + "000000000"
        print(command)
        return command

    def build_ext(self):
        command = self.op_code + "0000000000000"
        return command