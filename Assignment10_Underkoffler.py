# Carl Underkoffler - Erik Holbrook - Wed 9am - Assignment 10 , 
class Recommender:
	books_dict = {}
	ratings_dict = {}
	avg_dict = {}
####			
	def read_books(self, file_name):
		book_dict = {}
		
		try:
			fl = open(file_name, 'r')
		except:
			return None
		
		nLine = 0
		
		for line in fl:

			info_list = []
			
	#		print (line)
			
			author = line[:line.find(',')]

	#		print (author)
			
			title = line[line.find(',')+1:]
			title = title.rstrip('\n')
			
	#		print (title)
			
			info_list.append(title)
			info_list.append(author)
			
	#		print(info_list)
			
			book_dict[nLine] = info_list	
			nLine += 1

	#	for key in book_dict:
	#		print book_dict[key]	
		
		fl.close()
		return book_dict
####		
	def read_users(self, user_file):
		user_dict = {}
		
		try:
			fl = open(user_file, 'r')
		except:
			return None
			
			
		for line in fl:
			line = line.rstrip('\n')
			
	#		print (line)

			name = line[:line.find(' ')]
			
			line = line[line.find(' '):]
			
	#		print (name)
			
			num_list = []
			
			for i in line:
				index = i
				i = unicode(i)
				
				if i.isnumeric():
					num = int(i)
					if neg_switch:
						num *= -1

	#				print (num)
					
					num_list.append( num )
				
				neg_switch = False
				if i == '-':
					neg_switch = True
							
			user_dict[name] = num_list
			
		
	#	for key in user_dict:
	#		print (key)
	#		print (user_dict[key])
		
	#	print (user_dict)
		
		fl.close()
		return user_dict
####
	def calculate_average_rating(self):
		avg_dict = {}
		avg_info_dict = {}
		
		for user_name in self.ratings_dict:
			book_index = 0
		
			for rating in self.ratings_dict[user_name]:
				
				if rating != 0:
					try:
						avg_info_dict[book_index][0] += rating
						avg_info_dict[book_index][1] += 1
					except:
						first_rating = rating
						num_ratings = 1
						avg_info_dict[book_index] = [first_rating, num_ratings]
				
	#			if book_index == 0:
	#				print('Book:')
	#				print(book_index)
	#				print(user_name)
	#				print(rating)
	#				print(avg_info_dict[book_index])
						
				book_index += 1
			
	#		print (book_index)
			
		for book in avg_info_dict:	
			sum_ratings = avg_info_dict[book][0]
			num_ratings = avg_info_dict[book][1]

			if num_ratings != 0:
				avg = float(sum_ratings) / float(num_ratings)
				avg_dict[book] = avg
			else:
				avg_dict[book] = 0
					
	#		print ('----')
	#		print (book)
	#		print (avg_info_dict[book])
	#		print (avg_dict[book])
	#		print ('----')
			
	#	print (avg_info_dict)	
		
	#	print (avg_dict)
		return avg_dict
####
	def lookup_average_rating(self, index):
		title = self.books_dict[index][0]
		author = self.books_dict[index][1]
		
		avg_rating = self.avg_dict[index]
		
		output_str = '(%s) %s by %s' % (avg_rating, title, author)
	
#		print (output_str)
		
		return output_str
####
	def calc_similarity(self, user1, user2):
		user1_ratings = []
		user2_ratings = []
		
		try:
			user1_ratings = self.ratings_dict[user1]
		except:
			return None
		
		try:
			user2_ratings = self.ratings_dict[user2]
		except:
			return None
		
		if len(user1_ratings) != len(user2_ratings):
			return None
		
		sim_score = 0
		
		for rating1, rating2 in zip(user1_ratings, user2_ratings):
			sim_score += rating1 * rating2
#			print (rating1)
#			print (rating2)
#			print (sim_score)
				
		return sim_score
####	
	def get_most_similar_user(self, current_user_id):
		max_sim_score = 0
		most_sim_user = None
		
		for new_user in self.ratings_dict:
			if new_user != current_user_id:
				sim_score = self.calc_similarity(current_user_id, new_user)
				
				if sim_score > max_sim_score:
					max_sim_score = sim_score
					most_sim_user = new_user
		
		return most_sim_user
####
	def recommend_books(self, current_user_id):
		sim_user = self.get_most_similar_user(current_user_id)
		
		rec_list = []
		
		book_index = 0
		
		
		for cur_rat, sim_rat in zip( self.ratings_dict[current_user_id] , self.ratings_dict[sim_user] ):
			if cur_rat == 0:
				if sim_rat == 3 or sim_rat == 5:
					rec_list.append( self.lookup_average_rating(book_index) )
			
			book_index += 1
			
#		print (rec_list)
		
		return rec_list
####
	def __init__(self, books_filename, ratings_filename):
		self.books_dict = self.read_books(books_filename)
		self.ratings_dict = self.read_users(ratings_filename)
		self.avg_dict = self.calculate_average_rating()
		
		return
#  #
def my_tests():
	bookFileName = 'books.txt'
	userFileName = 'ratings.txt'
	
	test_class = Recommender(bookFileName, userFileName)
	
	test_index = 1
	test_class.lookup_average_rating(test_index)
		
	sim_score = test_class.calc_similarity('Ben', 'Claire')

#	print(sim_score)
		
#	print  (test_class.get_most_similar_user('Ben') )

#	print ( test_class.recommend_books('Ben') )
		
	
	return

def main():
	my_tests()
	return
	
if __name__ == "__main__":
	main()
