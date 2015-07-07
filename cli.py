# Main class for this project

# It should have the ability to take a string and parse out which function to call, with arguments.
# Has a member function for adding a function call, and the number of arguments that it takes. Maybe done automatically?
# Has a help function, that prints out all of the named commands, and maybe small help message
# Has some built in commands that will execute by default wheter or not the user has added them. The include: help, quit, exit, etc...
# Example:
    # cli = CLI();
    ## where the function "addNumbers", that takes 2 arguments is defined elsewhere
    # cli.addFunction("add", addNumbers, 2)
    # users_input = input('>? ')
    ## Sees if the users input matches the syntax for a command and calls it if it matches. For example, if the user types in "add 2 3", the execute command will return the result of addNumbers(2, 3). Which is most likely 5.
    # result = cli.executeCommand(users_input)



class CLI:
    def __init__(self):
        self.functions = {}

        self.addFunction("quit", self.quitFunction, 0)
        pass

    def addFunction(self, name, function_ptr, number_of_args):
        self.functions[name] = function_ptr
        pass

    def executeCommand(self, command_str):
        return self.functions[command_str]()
        pass

    def quitFunction(self):
        pass