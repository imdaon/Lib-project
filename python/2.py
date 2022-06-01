class score():
    def get_sum(self):
        return self.korean + self.En + self.math + self.science

    def get_avr(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avr())

