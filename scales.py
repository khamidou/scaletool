#!/usr/bin/env python

import itertools

# A ring class - we use it to transpose our basic scale : C D E F G A B
class Ring:
    def __init__(self, l):
        if not len(l):
            raise "ring must have at least one element"
        self._data = l

    def __repr__(self):
        return repr(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, i):
    	if i >= len(self._data):
		i = i % len(self._data)

        return self._data[i]
    def __delitem__(self, i):
    	del self._data[i]

    def index(self, i):
    	return self._data.index(i)

    def turn(self):
    	# Scales turn in reverse-order
        first = self._data.pop(0)
        self._data.append(first)

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]

    def turn_until(self, value):
    	while self.first() != value:
		self.turn()

    def turn_ntimes(self, times):
    	i = 0
    	while i < times:
		self.turn()
		i += 1

scales = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
modes = {"Ionian" : "C", "Dorian" : "D", "Phrygian" : "E", "Lydian" : "F",
	 "Mixolydian" : "G", "Aeolian" : "A", "Locrian" : "B"}

class Scale:
	def __init__(self, scale="C", formula=[2, 2, 1, 2, 2, 2, 1]):
		self.start = Ring(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"])
		# We store a modified scale as numbers : 1 means no sharp or flat, 0.5, one flat, 1.5 one sharp
		self.formula = formula
		self.transpose_scale(scale)
		#self.change_mode(mode)
	
	def transpose_scale(self, start_letter):
		self.start.turn_until(start_letter)

	def change_mode(self, mode_letter):
		v = ["C", "D", "E", "F", "G", "A", "B"]
		self.values.turn_ntimes(v.index(mode_letter))

	def __str__(self):
		retscale = self.start[0] + " " 
		notes = self.start
		translation_table = {	"Cb": "B",
					"Db" : "C#",
					"Eb" : "D#",
					"Fb" : "E",
					"Gb" : "F#",
					"Ab" : "G#",
					"Bb" : "A#", 
					"B#" : "C",
					"E#" : "F",
					}

		i = 0
		j = 0
		while i < 11 and j < 6: # reduce(lambda x,y: x+y, self.values)
			n = self.formula[j]
			retscale += notes[i+n]
			i += n 
			j += 1 # Don't forget to increment j to avoid looping.
			retscale += " "
		return retscale

if __name__ == "__main__":
	s = Scale("C", [2, 1, 1, 2, 2, 2, 1])
	print str(s)
