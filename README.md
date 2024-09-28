# DynAI: Bridging Dynamical Systems and Artificial Intelligence

Description of the repo:

[ADD]

# General Description of a Dynamical System

## Definition

A **dynamical system** is a mathematical framework used to describe the evolution of a system over time. It comprises a set of rules or equations that govern how the state of the system changes in response to time or other inputs.

A dynamical system can be represented mathematically as:

\[
\frac{d\mathbf{x}}{dt} = \mathbf{f}(\mathbf{x}, t)
\]

- \( \mathbf{x} \in \mathbb{R}^n \): State vector representing the system's state.
- \( t \): Time variable.
- \( \mathbf{f} \): Function defining the dynamics of the system, which may depend on the current state \( \mathbf{x} \) and possibly time \( t \).


## Components

1. **State Space**: 
   - The set of all possible states the system can occupy. The state is often represented as a vector in \( \mathbb{R}^n \), where \( n \) is the number of state variables.

2. **State Variables**: 
   - Quantities that describe the state of the system. They can represent physical properties (e.g., position, velocity) or abstract quantities (e.g., population sizes).

3. **Dynamics**: 
   - The rules governing how the state evolves over time, typically described by differential equations (continuous time) or difference equations (discrete time).

4. **Time**: 
   - The independent variable that represents the progression of the system. It can be continuous (real numbers) or discrete (integers).

## Types of Dynamical Systems

1. **Linear vs. Nonlinear**:
   - **Linear**: The equations governing the system are linear functions of the state variables.
   - **Nonlinear**: The equations involve nonlinear relationships, leading to more complex behavior.

2. **Continuous vs. Discrete**:
   - **Continuous**: The state changes smoothly over time, described by differential equations.
   - **Discrete**: The state changes at specific intervals, described by difference equations.

3. **Autonomous vs. Non-autonomous**:
   - **Autonomous**: The system's rules do not explicitly depend on time.
   - **Non-autonomous**: The rules include time-dependent terms.

## Behavior and Analysis

1. **Equilibrium Points**: 
   - Points in the state space where the system remains constant over time. Stability analysis helps determine whether small perturbations will grow or decay.

2. **Periodic Solutions**: 
   - Solutions that repeat over time, often found in oscillatory systems.

3. **Chaos**: 
   - Complex behavior arising in certain nonlinear systems, characterized by sensitivity to initial conditions and unpredictable long-term behavior.

4. **Phase Portraits**: 
   - Visual representations of trajectories in the state space, illustrating how the system evolves over time.


# Methods

1) Neural Ordinary Differential Equations (NeuralODE)
