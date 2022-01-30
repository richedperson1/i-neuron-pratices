import logging
logging.basicConfig(filename='list.log', level=logging.INFO,
                    format='%(levelname)s %(asctime)s %(message)s')


class list_modified:
    def __init__(self, lst):
        if type(lst) != list:
            raise Exception("please enter list only")
        try:
            self.list = lst
        except Exception as e:
            logging.error(str(e))
            logging.error(str(e))

    def length(self):
        total = 0
        try:
            for i in self.list:
                total += 1

            return total
        except Exception as e:
            logging.error(str(e))
            logging.exception(str(e))

    def append(self, num):
        try:
            if str(num):
                pass
        except Exception as e:
            return "Please put single value"

        try:
            self.list += [num]
            return self.list

        except Exception as e:
            logging.exception(str(e))
            logging.error(str(e))

    def increase(self, name):
        if type(name) != list:
            raise Exception("Please Enter list : ")
        try:
            for i in name:
                self.list = self.append(i)
                logging.info(f"The value adding in list is : {i}")
            return self.list
        except Exception as e:
            logging.error(str(e))
            logging.exception(str(e))

    def count_value(self, value):
        try:
            total = 0
            for i in self.list:
                if i == value:
                    total += 1
            return total
        except Exception as e:
            logging.error(str(e))
            logging.exception(str(e))

    def popping(self):
        if self.length() == 0:
            return "List doesn't have value...!"
        try:
            self.list = self.list[:-1]
            return self.list
        except Exception as e:
            logging.exception(str(e))

    def clear(self):
        self.list = []
        return self.list

    def __getitem__(self, item):
        return self.list[item]

    def __str__(self):
        try:
            return f"{self.list}"
        except Exception as e:
            logging.exception(str(e))
            logging.info(str(e))

    def __add__(self, num):
        try:
            if type(num) == list:
                self.list += num
            else:
                self.list += [num]

            return self.list
        except Exception as e:
            logging.error(str(e))
            logging.exception(str(e))
            return "please enter string , number or list only "