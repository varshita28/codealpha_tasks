import random

class HangmanGame:
    def __init__(self, word_dict, max_incorrect_guesses=6):
        self.word_dict = word_dict
        self.max_incorrect_guesses = max_incorrect_guesses
        self.word, self.hint = self.select_random_word_and_hint()
        self.guessed_letters = set()
        self.incorrect_guesses = 0

    def select_random_word_and_hint(self):
        word, hint = random.choice(list(self.word_dict.items()))
        return word, hint

    def display_current_state(self):
        display = ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        print('Current word: ' + ' '.join(display))

    def get_guess(self):
        while True:
            guess = input('Guess a letter: ').lower()
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid input. Please guess a single letter.')
            elif guess in self.guessed_letters:
                print('You have already guessed that letter. Try again.')
            else:
                return guess

    def play(self):
        print('Welcome to Hangman!')
        print(f'Hint: {self.hint}')
        while self.incorrect_guesses < self.max_incorrect_guesses:
            self.display_current_state()
            guess = self.get_guess()
            self.guessed_letters.add(guess)

            if guess in self.word:
                print(f'Good guess! {guess} is in the word.')
                if all(letter in self.guessed_letters for letter in self.word):
                    print(f'Congratulations! You have guessed the word: {self.word}')
                    break
            else:
                self.incorrect_guesses += 1
                print(f'Incorrect guess. You have {self.max_incorrect_guesses - self.incorrect_guesses} guesses left.')

            if self.incorrect_guesses == self.max_incorrect_guesses:
                print(f'Sorry, you have used all your guesses. The word was: {self.word}')
                break

if __name__ == '__main__':
    word_dict = {
        'python': 'Popular programming language.',
        'hangman': 'The game you are playing.',
        'challenge': 'A difficult task.',
        'programming': 'Writing computer code.',
        'developer': 'Creates software.',
        'algorithm': 'Step-by-step procedure.',
        'function': 'Code block for a task.',
        'variable': 'Storage for data.',
        'syntax': 'Rules for coding.',
        'loop': 'Repeats code.',
        'condition': 'True or false check.',
        'string': 'Sequence of characters.',
        'integer': 'Whole number.',
        'float': 'Decimal number.',
        'boolean': 'True or false value.',
        'list': 'Ordered collection.',
        'tuple': 'Immutable collection.',
        'dictionary': 'Key-value pairs.',
        'set': 'Unique items collection.',
        'module': 'Python file.',
        'package': 'Collection of modules.',
        'library': 'Precompiled routines.',
        'framework': 'Platform for apps.',
        'software': 'Programs for computers.',
        'hardware': 'Physical computer parts.',
        'network': 'Connected computers.',
        'database': 'Structured data storage.',
        'server': 'Provides resources.',
        'client': 'Requests resources.',
        'protocol': 'Rules for data exchange.',
        'security': 'Protection from threats.',
        'encryption': 'Securing data.',
        'decryption': 'Decoding data.',
        'authentication': 'Verifying identity.',
        'authorization': 'Permission to access.',
        'firewall': 'Network security system.',
        'malware': 'Harmful software.',
        'virus': 'Malicious code.',
        'trojan': 'Disguised malware.',
        'worm': 'Self-replicating malware.',
        'spyware': 'Secretly monitors activity.',
        'adware': 'Displays ads.',
        'ransomware': 'Holds data for ransom.',
        'phishing': 'Fraudulent information request.',
        'hacking': 'Unauthorized access.',
        'bug': 'Programming error.',
        'debug': 'Fixing errors.',
        'testing': 'Evaluating software.',
        'deployment': 'Releasing software.',
        'virtualization': 'Creating virtual resources.',
        'container': 'Package of software.',
        'docker': 'Container platform.',
        'kubernetes': 'Manages containers.',
        'cloud': 'Internet computing.',
        'aws': 'Amazon cloud service.',
        'azure': 'Microsoft cloud service.',
        'google': 'Search engine giant.',
        'microservices': 'Small, autonomous services.',
        'monolithic': 'Tightly coupled system.',
        'scalability': 'Handles growth.',
        'performance': 'Efficiency of system.',
        'optimization': 'Improving efficiency.',
        'cache': 'Fast data storage.',
        'memory': 'Quick access storage.',
        'disk': 'Storage device.',
        'cpu': 'Computer processor.',
        'bandwidth': 'Data transfer rate.',
        'latency': 'Delay in data transfer.',
        'throughput': 'Data processing rate.',
        'api': 'Application interface.',
        'rest': 'Web service design.',
        'graphql': 'Query language for APIs.',
        'soap': 'Protocol for web services.',
        'json': 'Data format.',
        'xml': 'Markup language.',
        'html': 'Web page language.',
        'css': 'Styles web pages.',
        'javascript': 'Web programming language.',
        'typescript': 'JavaScript superset.',
        'react': 'JavaScript library.',
        'angular': 'Web application framework.',
        'vue': 'JavaScript framework.',
        'node': 'JavaScript runtime.',
        'express': 'Node.js framework.',
        'django': 'Python web framework.',
        'flask': 'Micro web framework.',
        'spring': 'Java framework.',
        'laravel': 'PHP framework.',
        'ruby': 'Programming language.',
        'rails': 'Ruby framework.',
        'php': 'Web development language.',
        'java': 'Object-oriented language.',
        'kotlin': 'Java alternative.',
        'swift': 'Apple programming language.',
        'objective': 'Previous Apple language.',
        'csharp': 'Microsoft language.',
        'golang': 'Google language.',
        'rust': 'Systems programming language.',
        'scala': 'JVM language.',
        'elixir': 'Erlang-based language.',
        'haskell': 'Functional programming language.',
        'clojure': 'Lisp on JVM.',
        'perl': 'Scripting language.',
    }
    game = HangmanGame(word_dict)
    game.play()
