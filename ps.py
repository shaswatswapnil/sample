
min_req = {
    "Ingredient 1": 5,
    "Ingredient 2": 3,
    "Ingredient 3": 4,
    "Ingredient 4": 2
}


balls_stats = {
    "Total Number of Balls": 0,
    "Unique Colour Ball Count": 0,
    "Unique Colour Ball Names": set()
}


ball_counts = {}

def create_new_balls(color, ingredient1, ingredient2, ingredient3, ingredient4):
 
    if (
        ingredient1 >= min_req["Ingredient 1"] and
        ingredient2 >= min_req["Ingredient 2"] and
        ingredient3 >= min_req["Ingredient 3"] and
        ingredient4 >= min_req["Ingredient 4"]
    ):
        max_balls = min(
            ingredient1 // min_req["Ingredient 1"],
            ingredient2 // min_req["Ingredient 2"],
            ingredient3 // min_req["Ingredient 3"],
            ingredient4 // min_req["Ingredient 4"]
        )
        
     
        balls_stats["Total Number of Balls"] += max_balls
        balls_stats["Unique Colour Ball Count"] += 1
        balls_stats["Unique Colour Ball Names"].add(color)
        
        
        if color in ball_counts:
            ball_counts[color] += max_balls
        else:
            ball_counts[color] = max_balls
        
        return f"{color} {max_balls}"
    else:
        return f"{color} 0"

def Display_ball_statics():
    print("- Total Number of Balls:", balls_stats["Total Number of Balls"])
    print("- Unique Colour Ball Count:", len(balls_stats["Unique Colour Ball Names"]))
    print("- Unique Colour Ball Names:", ", ".join(balls_stats["Unique Colour Ball Names"]))

def Display_sortedd_balls():
    sorted_balls = sorted(ball_counts.items(), key=lambda x: x[1])
    for color, count in sorted_balls:
        print(f"- {color}: {count}")

while True:
    print("Enter input (color, ingredient1, ingredient2, ingredient3, ingredient4) or type 'quit' to exit:")
    user_input = input().strip()
    
    if user_input.lower() == 'quit':
        break
    
    input_params = user_input.split(",")
    
    if len(input_params) != 5:
        print("Invalid input. Please enter input in the format: color, ingredient1, ingredient2, ingredient3, ingredient4")
        continue
    
    color, ingredient1, ingredient2, ingredient3, ingredient4 = input_params
    color = color.strip()
    
    try:
        ingredient1 = int(ingredient1.strip())
        ingredient2 = int(ingredient2.strip())
        ingredient3 = int(ingredient3.strip())
        ingredient4 = int(ingredient4.strip())
    except ValueError:
        print("Invalid input. Ingredient quantities must be integers.")
        continue
    
    result = create_new_balls(color, ingredient1, ingredient2, ingredient3, ingredient4)
    print(result)

print("Enter 'stats' to view statistics or 'sort' to sort the balls by count:")
user_choice = input().strip().lower()

if user_choice == 'stats':
    Display_ball_statics()
    
elif user_choice == 'sort':
    Display_sortedd_balls()
else:
    print("Invalid choice. Exiting.")
