
import random
import string

def generate_random_sequence(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

def generate_random_quality(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def generate_random_fastq_file(num_sequences, sequence_length):
    with open('random.fastq', 'w') as file:
        for i in range(num_sequences):
            sequence = generate_random_sequence(sequence_length)
            quality = generate_random_quality(sequence_length)

            file.write(f'@SEQ_{i}\n')
            file.write(f'{sequence}\n')
            file.write('+\n')
            file.write(f'{quality}\n')

    print(f'Generated {num_sequences} random sequences of length {sequence_length} in random.fastq')

# Usage
generate_random_fastq_file(num_sequences=100, sequence_length=50)
