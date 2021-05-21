#!/usr/bin/env python3
from os import system as sys
from sys import argv

running_total = 1
counter = 0

counter = int(argv[1])
sys(f"sed -i '6s/[0-9]\+/{counter}/' {argv[0]}")
sys(f'sed -i "8,12s/\(.\)/#\\1/" {argv[0]}')
sys(f'sed -i "14,22s/#//" {argv[0]}')
sys(f"./{argv[0]}")
    
#if counter > 0:
#    sys(f"sed -i '5s/[0-9]\+/{running_total*counter}/' {argv[0]}")
#    sys(f"sed -i '6s/[0-9]\+/{counter-1}/' {argv[0]}")
#    sys(f"./{argv[0]}")
#else:
#    sys(f"echo {running_total}")
#    sys(f"sed -i '5s/[0-9]\+/1/' {argv[0]}")
#    sys(f'sed -i "8,12s/#//" {argv[0]}')
#    sys(f'sed -i "14,22s/\(.\)/#\\1/" {argv[0]}')
