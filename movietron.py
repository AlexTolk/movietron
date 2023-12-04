from dataset import *
from linked_list import LinkedList
from welcome_msg import welcome_message

welcome_message()

# code to insert movie genres into the linked list

def insert_movie_genres():
    movie_genre_list = LinkedList()

    for genre in movie_genres:
        movie_genre_list.insert_beginning(genre)
    return movie_genre_list


# code to insert movie data into the linked list

def insert_movie_data():
    movie_data_list = LinkedList()
    for genre in movie_genres:
        movie_sublist = LinkedList()
        for movie in movie_list:
            if movie[0] == genre:
                movie_sublist.insert_beginning(movie)
        movie_data_list.insert_beginning(movie_sublist)
    return movie_data_list


my_genre_list = insert_movie_genres()
# print(my_genre_list.stringify_list())
my_movie_list = insert_movie_data()


selected_genre = ""

# Code for user interaction

while len(selected_genre) == 0:
    user_input = str(input(
        "\nWhich movie genre would you like to watch?\nType the beginning of that genre and press enter to see if "
        "it's here.\n")).capitalize()
    # Search for user_input in food types data structure here
    matching_genres = []
    genre_list_head = my_genre_list.get_head_node()
    while genre_list_head is not None:
        if str(genre_list_head.get_value()).startswith(user_input):
            matching_genres.append(genre_list_head.get_value())
        genre_list_head = genre_list_head.get_next_node()
    # print list of matching genres
    for genre in matching_genres:
        print(genre)
    # check if only one genre was found, ask user if that's what they want
    if len(matching_genres) == 1:
        select_genre = str(input(
            "\nThe only matching genre is " + matching_genres[0] + ". \nDo you want to look at " +
            matching_genres[0] + " movies? Enter y for yes and n for no\n")).lower()

        #  code for retrieving data
        if select_genre == "y":
            selected_genre = matching_genres[0]
            print("Selected Genre: " + selected_genre)
            movie_list_head = my_movie_list.get_head_node()
            while movie_list_head.get_next_node() is not None:
                sublist_head = movie_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_genre:
                    while sublist_head.get_next_node() is not None:
                        print(")________________________________(")
                        print(")________________________________(")
                        print(")Title: " + sublist_head.get_value()[1] + "  (")
                        print(")Description: " + sublist_head.get_value()[2] + "  (")
                        print(")________________________________(")
                        print(")________________________________(")
                        sublist_head = sublist_head.get_next_node()
                movie_list_head = movie_list_head.get_next_node()
            # Ask user if they want to look for a different genre
            repeat_loop = str(input("\nDo you want to see other genres? Enter y for yes and n for no.\n")).lower()
            if repeat_loop == "y":
                selected_genre = ""
