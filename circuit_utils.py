# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:01:58 2022

@author: owner



"""

import numpy as np

def creation_op(N):
#bosonic creation operator in matrix truncated to NxN    
    vec = [np.sqrt(n) for n in range(1,N)]
    return np.diag(vec,-1)

def annihilation_op(N):
#bosonic creation operator in matrix truncated to NxN    
    vec = [np.sqrt(n) for n in range(1,N)]
    return np.diag(vec,1)

def ID(N):
# identity matrix on N qubits
    return np.identity(2**N)    

def pauli_x():
    return np.array([[0,1],[1,0]])

def pauli_z():
    return np.array([[1,0],[0,-1]])

def pauli_y():
    return np.array([[0,-1j],[1j,0]])
def cx():
    return np.array([[1,0,0,0],[0,1,0,0], [0,0,0,1],[0,0,1,0]])


def pauli(a):
    if a==1:
        return pauli_x()
    if a==2:
        return pauli_y()
    if a==3:
        return pauli_z()

    

def sigma_plus():
    return pauli_x() + 1j*pauli_y()
def sigma_minus():
    return pauli_x() - 1j*pauli_y()


def multi_kron(*args):
    
    #take care of degenerate case
    if len(args)==1:
        return args[0]
        
        
    output = np.kron(args[0],args[1])
    if len(args)>2:
        for i in range(2,len(args)):
            output = np.kron(output, args[i])
    return output
    

def product_operator(local_operators, qubits, number_of_qubits):
    
    # take care of degenerate cases:
    if not type(qubits)== list:
        qubits = [qubits]
    if  not type(local_operators) == list:
        local_operators = [local_operators]
        
            
    # check where we have a two-qubit operator
    two_qubit_gate_indices = []
    for i, loc_op in enumerate(local_operators):
        if loc_op.shape == (4, 4):
            two_qubit_gate_indices.append(qubits[i])
    
    
    # create a list of unity operators
    op_list = []
    for i in range(number_of_qubits):
        op_list.append(np.identity(2))
        
    # change desired entries to desired matrices
    for i,qubit in enumerate(qubits):
        op_list[qubit]=local_operators[i]
        
    # remove excess id(2) matrices due to two-qubit-gates
    for i in two_qubit_gate_indices:
        del op_list[i+1]
   
    matrix = multi_kron(*op_list)
    return matrix       



