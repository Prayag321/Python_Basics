
"""
    @Author: Prayag Bhoir
    @Date: 25-07-2024
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 25-07-2024
    @Title : Python program to calculate change in vending machine

"""
def find_minimum_notes(change):
    """
    Description:
        This function finds the minimum notes to be return
    Parameters:
        change(int):Amount entered by the user to exchange in change
    Returns:
        count(int):Number of notes to return
        note_count(list):list of notes in change
        
    """
    # List of available notes in descending order
    notes = [2000, 500, 100, 50, 10, 5, 2, 1]
    note_count = []
    count = 0
    
    # Recursive function to find the minimum notes
    def get_notes(change):
        """
        Description:
            This function finds the minimum notes to be return
        Parameters:
            change(int):Amount entered by the user to exchange in change
        Returns:
            Recursive call get_notes(change - note)
        
        """
        nonlocal count
        for note in notes:
            if change >= note:
                count += 1
                note_count.append(note)
                return get_notes(change - note)
    
    # Call the recursive function
    get_notes(change)
    
    return count, note_count

def main():
    # Input the change to be returned
    change = int(input("Enter the change to be returned: "))
    minimum_notes, notes_list = find_minimum_notes(change)

    # Output the result
    print("Minimum number of notes needed:", minimum_notes)
    print("Notes to be returned:", notes_list)

if __name__=="__main__":
    main()