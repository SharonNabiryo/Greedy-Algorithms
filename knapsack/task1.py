#calculating volume
def volumeCalc(h, w, d):
    # Calculate and return the volume of an item given its height, width, and depth.
    vol = h * w * d
    return vol

def readfile(file_path):
    # Read items from the file and store their names, values, and volumes.
    names = []
    values = []
    volumes = []

    with open(file_path, 'r') as file:
        for line in file:
            row = line.split()
            if len(row) != 5: # Skip rows that don't have the expected number of values
                continue
            name, value, height, width, depth = row
            value = int(value)  # Convert value to an integer
            height = int(height) # Convert height to an integer
            width = int(width) # Convert width to an integer
            depth = int(depth) # Convert depth to an integer
            volume = volumeCalc(height, width, depth) # Calculate the volume of an item
            names.append(name) # store item name
            values.append(value) # store item value
            volumes.append(volume) # store item volume
    return names, values, volumes

def knapsack(v, volumes, cap):
    rwv = []
    for i in range(len(v)):
        rwv.append([v[i]/volumes[i], volumes[i], v[i], i])
    rwv.sort(reverse=True)
    ans = []
    total_volume = 0
    found = True
    while (found):
        found = False
        for t in rwv:
            if (t[1] + total_volume) <= cap:
                ans.append(t[3])
                total_volume += t[1]
                found = True
                break
    return ans

def main():
    file_path = "data.txt"

    # Get the maximum volume from the user
    try:
        max_volume = int(input("Enter the maximum volume in cubic inches: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Read items from the TXT file
    names, values, volumes = readfile(file_path)

    # Call the knapsack function to find the optimal solution
    selected_items_indices = knapsack(values, volumes, max_volume)

    # Calculate the total value of the selected items and the leftover volume
    total_value = sum(values[i] for i in selected_items_indices)
    total_volume = sum(volumes[i] for i in selected_items_indices)
    leftover_volume = max_volume - total_volume

    # Group identical items
    item_count = {}
    for i in selected_items_indices:
        item_name = names[i]
        if item_name in item_count:
            item_count[item_name] += 1
        else:
            item_count[item_name] = 1

    # Format the result message
    item_description = []
    for item, count in item_count.items():
        if count == 1:
            item_description.append(f"1 {item}")
        else:
            item_description.append(f"{count} {item}")

    # Print the results
    if selected_items_indices:
        result = " and ".join(item_description)
        print(
            f"The suggested items are: {result} with a total value of ${total_value}. "
            f"There were {leftover_volume} cubic inches left unused."
        )
    else:
        print("No items could be selected within the given volume limit.")

if __name__ == "__main__":
    main()





