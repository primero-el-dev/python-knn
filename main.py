import math

data = [[1,2], [1,3], [2,3], [5,6], [4,7], [5,6]]
labels = [1,1,1,2,2,1]


def sort_by_nth(arr, nth, reverse=False):
	    l = len(arr)
	    
	    for i in range(0, l):
	        for j in range(0, l-i-1):
	            if (arr[j][nth] > arr[j + 1][nth]) and not reverse:
	                tempo = arr[j]
	                arr[j] = arr[j + 1]
	                arr[j + 1] = tempo
	    return arr


class KNN:

	data = []
	labels = []
	k = 1
	

	def feed(self, data = [], labels = []):
		if len(data) != len(labels):
			raise Exception("Not equal number of data samples and labels.")
		
		self.data += data
		self.labels += labels
	

	def forward(self, credentials):
		result_label = 0
		differences_labels = []
		credentials_length = len(credentials)

		for i in range(0, len(self.data)):
			if len(self.data[i]) != credentials_length:
				raise Exception("Wrong number of params between given training data sample and point.")

			difference = self.__calculate_difference(data[i], credentials)
			differences_labels.append([difference, self.labels[i]])

		labels = list(map(lambda x: x[1], sort_by_nth(differences_labels, 0, False)))
		labels_count = {}
		for i in range(0, self.k):
			if labels[i] in labels_count:
				labels_count[labels[i]] += 1
			else:
				labels_count[labels[i]] = 1

		max_count = 0
		result_label = None
		for label, count in labels_count.items():
			if count > max_count:
				max_count = count
				result_label = label

		return result_label


	def set_k(self, k):
		self.k = k


	def __calculate_difference(self, first, second):
		if len(first) != len(second):
			raise Exception("Not equal number of vector params.")
		
		difference = 0
		for i in range(0, len(first)):
			difference += math.pow(abs(first[i] - second[i]), 2)
		
		return math.sqrt(difference)


knn = KNN()
knn.feed(data, labels)
knn.set_k(6)
print(knn.forward([4,6]))