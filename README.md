# 📅 Day 43 - Count Pairs with Given Sum
## 🧩 Problem Statement:
Given an array arr[] and an integer target, the task is to find the number of pairs in the array whose sum is equal to the target value.

## 📥 Input:
- An integer array arr[] of size n.

- An integer target.

## 🎯 Output:
- An integer representing the count of valid pairs (i, j) such that arr[i] + arr[j] == target and i != j.

## Explanation:
There are two pairs with sum 6: (1,5) and (5,1). Since arr[0] and arr[3] are both 1s, and arr[1] is 5, we get 2 such pairs.

## 🧠 Approach:
- Use a hashmap (dictionary) to keep track of frequency of elements.

- For each element, compute complement = target - current_element.

- If the complement exists in the hashmap, it contributes to the pair count.

- Update frequency map accordingly.

## 🧮 Time & Space Complexity:
- Time Complexity: O(n) — single pass through the array.

- Space Complexity: O(n) — for the frequency dictionary.

## 🛠️ Language Used:
Python 🐍

