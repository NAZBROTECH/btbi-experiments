# virtual_lesion_test.py — to be expanded
def simulate_lesion(user_signal, lesion_type='frontal'):
    if lesion_type == 'frontal':  # Phineas Gage style
        return user_signal * 0.3  # dampen impulse control
    elif lesion_type == 'temporal':  # H.M. style
        return [0] * len(user_signal)  # wipe memory trace
    return user_signal

print("Virtual lesion module ready for integration")
