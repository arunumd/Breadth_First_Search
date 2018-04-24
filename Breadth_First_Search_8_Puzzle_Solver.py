#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 01:26:11 2018

@author: arunkumar
"""
from __future__ import print_function
import csv
import random
#import pdb; pdb.set_trace()
"""This function initiates the board"""
def puzzle_initiator():
    board = [0,1,2,3,4,5,6,7,8] #Assign a board state
    if (board == [1,2,3,4,5,6,7,8,0] or board == board):
        random.shuffle(board) #Shuffle the board
    else:
        pass
    return board

"""This function moves the zero up"""
def move_up(gameboard):
    new_board1 = []
    for i in gameboard:
        if (gameboard[i]==0 and gameboard[0]!=0 and gameboard[1]!=0 and gameboard[2]!=0):
            new_board1 = list(gameboard)
            new_board1[i]=new_board1[i-3]
            new_board1[i-3]=0
            break
        else:
            pass
    return new_board1


"""This function moves the zero right"""
def move_right(gameboard):
    new_board2 = []
    for i in gameboard:
        if (gameboard[i]==0 and gameboard[2]!=0 and gameboard[5]!=0 and gameboard[8]!=0):
            new_board2 = list(gameboard)
            new_board2[i]=new_board2[i+1]
            new_board2[i+1]=0
            break
        else:
            pass
    return new_board2

            
"""This function moves the zero down"""
def move_down(gameboard):
    new_board3 = []
    for i in gameboard:
        if (gameboard[i]==0 and gameboard[6]!=0 and gameboard[7]!=0 and gameboard[8]!=0):
            new_board3 = list(gameboard)
            new_board3[i]=new_board3[i+3]
            new_board3[i+3]=0
            break
        else:
            pass
    return new_board3 
            
"""This function moves the zero left"""
def move_left(gameboard):
    new_board4 = []
    for i in gameboard:
        if (gameboard[i]==0 and gameboard[0]!=0 and gameboard[3]!=0 and gameboard[6]!=0):
            new_board4 = list(gameboard)
            new_board4[i]=new_board4[i-1]
            new_board4[i-1]=0
            break
        else:
            pass
    return new_board4

"""The action suite combines all the four actions and returns a list of daughters"""
def action_suite(board_new):
    # Apply all four actions on initial state and concatenate output states to a list
    up1 = move_up(board_new)
    down1 = move_down(board_new)
    left1 = move_left(board_new)
    right1 = move_right(board_new)
    daughters = []
    daughters.append(up1)
    daughters.append(down1)
    daughters.append(left1)
    daughters.append(right1)
    new_daughters = [x for x in daughters if x]
    return new_daughters

def dict_updater(parent,member,dict,counter):
    perm = tuple(member)
    print(perm)
    print("The dict is :", dict)
    if dict.has_key(perm) is False:
        access = tuple(parent)
        access_value = dict.get(access)
        assign_parent = access_value[0]
        counter += 1
        new_value = [counter, assign_parent, 0]
        dict.update({perm: new_value})
        print("The updated dict is :", dict)
        return
    else:
        pass

    
"""This is the main function"""    
def main():
    #Calling the board initiator
    shuff_board = puzzle_initiator()
    #Creating key value pair dict for first node
    nodekey1 = tuple(shuff_board)
    node_no = 1
    parent_no = 0
    cost = 0
    nodevalue1 = [1,0,0]
    nodes_dict = {nodekey1: nodevalue1}
    parent_nodes = [shuff_board]
    print(nodes_dict)
    print(parent_nodes)
    swap_list = []

    while (node_no <100000):
        for each in parent_nodes:
            new_members = action_suite(each)
            for everyone in new_members:
                perm = tuple(everyone)
                if nodes_dict.has_key(perm) is False:
                    access = tuple(each)
                    access_value = nodes_dict.get(access)
                    assign_parent = access_value[0]
                    node_no += 1
                    new_value = [node_no, assign_parent, cost]
                    nodes_dict.update({perm: new_value})
                    swap_list.append(everyone)
                else:
                    pass
        parent_nodes = list(swap_list)

    #for k in nodes_dict.keys():
     #   print("For state ",k," the value is ",nodes_dict[k])
    #print("The total no. of nodes generated is :",node_no)
    w = csv.writer(open("output.csv", "w"))
    for key, val in nodes_dict.items():
        w.writerow([key, val])

    return 0

    
    
main()
    