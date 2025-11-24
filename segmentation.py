
# Dictionary of valid words
little_dictionary = [
    "a",
    "afternoon",
    "airport",
    "an",
    "and",
    "anywhere",
    "at",
    "because",
    "become",
    "before",
    "behind",
    "beside",
    "between",
    "breakfast",
    "broadcast",
    "but",
    "daylight",
    "deadline",
    "everywhere",
    "for",
    "forecast",
    "handbook",
    "hardware",
    "he",
    "headline",
    "her",
    "him",
    "homework",
    "i",
    "in",
    "income",
    "inside",
    "into",
    "it",
    "keyboard",
    "me",
    "midnight",
    "network",
    "notebook",
    "of",
    "offline",
    "on",
    "online",
    "or",
    "outcome",
    "outline",
    "outside",
    "overcome",
    "oversee",
    "password",
    "saturn",
    "she",
    "software",
    "somewhere",
    "suitcase",
    "sunlight",
    "takeover",
    "textbook",
    "the",
    "them",
    "therefore",
    "they",
    "to",
    "understand",
    "undertake",
    "upon",
    "us",
    "we",
    "whatever",
    "whenever",
    "wherever",
    "whoever",
    "within",
    "without",
    "you",
]


def binary_search(word_list: list[str], target: str) -> int:
    """Performs binary search on a sorted list of words.
    Returns the index of target if found, otherwise -1.
    To preserve memory, this implementation is iterative."""
    low: int = 0
    high: int = len(word_list) - 1

    while low <= high:
        mid: int = (low + high) // 2
        guess: str = word_list[mid]

        if guess == target:
            return mid  # Target found
        if guess > target:
            high = mid - 1  # Search in the lower half
        else:
            low = mid + 1  # Search in the upper half

    return -1  # Target not found


def is_word(word_list: list[str], word: str) -> bool:
    """Boolean helper for binary searchReturns True if word is in 
    word_list, False otherwise."""
    return binary_search(word_list, word) != -1


def can_segment_dp(A: str) -> list[str] | None:
    """Determine (using dynamic programming) if A can be segmented into
    valid tokens from little_dictionary.
    
    Returns:
        A list of segmented words if the string is segmentable, None otherwise.
    
    Example:
        can_segment_dp("anywherethesuitcasebehindoversee")
        returns ['anywhere', 'the', 'suitcase', 'behind', 'oversee']
    """
    n = len(A)
    
    # Initialize the dp array to track if prefix A[:i] is segmentable
    dp  = [False] * (n + 1)
    
    # parent array keeps track of the index where the last word starts
    parent = [-1] * (n + 1)
    
    # Base case: empty string is segmentable
    dp[0] = True

    # Consider every prefix A[:i] for i in 1..n
    for i in range(1, n + 1):
        j = 0
        # we continue until we either find a valid split or exhaust j
        while j < i and not dp[i]:
            if dp[j] and is_word(little_dictionary, A[j:i]):
                dp[i] = True
                parent[i] = j  # record where the last word starts
            j += 1

    # Reconstruct the segmentation by backtracking through parent array
    segmentation = None
    if dp[n]:
        segmentation = []
        i = n
        while i > 0:
            j = parent[i]
            segmentation.append(A[j:i])
            i = j
    
    return segmentation


# Test the function
if __name__ == "__main__":
    # Test cases
    test_strings = [
        "anywherethesuitcasebehindoversee",
        "homeworkkeyboardpassword",
        "thesoftwareoutcome",
        "unsegmentablestring",
        "ittothemandus",
        "forecastsunlightmidnight"
    ]
    
    print("Testing can_segment_dp function:\n")
    print("-" * 80)
    
    for test_str in test_strings:
        result = can_segment_dp(test_str)
        if result:
            print(f"✓ '{test_str}'")
            print(f"  Segmentation: {result}\n")
        else:
            print(f"✗ '{test_str}'")
            print(f"  Cannot be segmented\n")
