import sys
import re

def parse_set(s):
    if s == '0':
        return frozenset()
    s = s.strip('{}')
    return frozenset(s.split())

def main():
    input_data = sys.stdin.read().splitlines()
    lines = [l.strip() for l in input_data if l.strip()]
    
    if not lines:
        return
        
    c = int(lines[0])
    idx = 1
    
    for case in range(1, c + 1):
        n = int(lines[idx])
        idx += 1
        
        initial_states = frozenset(lines[idx].split())
        idx += 1
        
        alphabet = lines[idx].split()
        idx += 1
        
        final_states = set(lines[idx].split())
        idx += 1
        
        transitions = {}
        for _ in range(n):
            parts = lines[idx].split(maxsplit=1)
            state = parts[0]
            
            raw_trans = re.findall(r'\{[^}]+\}|0', parts[1])
            
            transitions[state] = {}
            for i, symbol in enumerate(alphabet):
                transitions[state][symbol] = parse_set(raw_trans[i])
                
            idx += 1
            
        dfa_states = {}
        dfa_transitions = {}
        dfa_final = []
        
        start_state = initial_states
        queue = [start_state]
        dfa_states[start_state] = "Q0"
        state_counter = 1
        
        while queue:
            current = queue.pop(0)
            name = dfa_states[current]
            
            if any(q in final_states for q in current) and name not in dfa_final:
                dfa_final.append(name)
                
            dfa_transitions[name] = {}
            
            for symbol in alphabet:
                next_state = set()
                for q in current:
                    next_state.update(transitions[q][symbol])
                    
                next_state = frozenset(next_state)
                
                if next_state not in dfa_states:
                    dfa_states[next_state] = f"Q{state_counter}"
                    state_counter += 1
                    queue.append(next_state)
                    
                dfa_transitions[name][symbol] = dfa_states[next_state]
                
        print(f"--- Case {case} ---")
        print(f"Initial state: {dfa_states[start_state]}")
        
        if dfa_final:
            print(f"Final states: {' '.join(dfa_final)}")
        else:
            print("Final states: None")
            
        header = "State | " + " | ".join(alphabet)
        print(header)
        for state_set, name in dfa_states.items():
            row = [name]
            for symbol in alphabet:
                row.append(dfa_transitions[name][symbol])
            print(" | ".join(row))
        print()

if __name__ == "__main__":
    main()