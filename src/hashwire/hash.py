# %%
import secrets
from hashlib import sha256
import math


__ENCODING__ = 'ascii'

# %%


# helper to get seed
def get_seed():
    return secrets.token_hex()


# num_len is the length of the hash chain
def get_hash_chain(num_len, seed=None):
    if seed is None:
        seed = get_seed()
    commitment = seed

    # update chain
    hash_chain = []
    for _ in range(num_len):
        commitment = sha256(commitment.encode(__ENCODING__)).hexdigest()
        hash_chain.append(commitment)
    return hash_chain, seed


# %%

# Hash multichains is an hash chain per digit position.
def get_hash_multichain(int_value):
    num_digits = math.ceil(math.log10(int_value+1))

    # generate seed and multi_hash_chain using dictionary comprehension
    seed = [get_seed() for _ in range(num_digits)]
    hash_multichain = {i: get_hash_chain(10, seed[i])[0] for i in range(num_digits)}

    return hash_multichain, seed


# MDP
def mdp(x, base=10):
    # this does the same as: len(str(x))
    num_digits = math.ceil(math.log(x+1, base))

    # init
    mdp_vector = [x]

    # we can be lucky
    xp = (x+1) % (base ** (num_digits-1))
    if not xp:
        # return vector if it's zero
        return mdp_vector

    # save minimum value
    minx = (x - xp)

    for i in range(1, num_digits-1):
        xp = (x+1) % (base ** i)
        diff = x - xp
        if diff not in mdp_vector:
            if diff != minx:
                mdp_vector.append(diff)
            else:
                break

    # add minimum value to the end
    mdp_vector.append(minx)
    return mdp_vector


# From hash multichain create the optimized hashwire
def __generate_hash_wire_commitment(mdp_value, multi_hash_chain):
    # convert mdp_value to a list of digits
    digits = [int(d) for d in str(mdp_value)]
    # one mdp value can be shorter than the other
    diff = len(multi_hash_chain) - len(digits)

    return [multi_hash_chain[i + diff][digit] for i, digit in enumerate(digits)]


# create list of hash wire for every mdp value
def get_commitment_hash_wire(mdp_vector, multi_hash_chain):
    return {value: __generate_hash_wire_commitment(value, multi_hash_chain) for value in mdp_vector}


# number to prove geq
# hash_zero public hash
# proof_digest_n hash used to prove it's larger than n
def geq_hash_proof(n, hash_zero, proof_digest_n):
    # sanity check
    if (len(proof_digest_n) != 64) or \
        (not isinstance(n, int)) or \
        (n < 0) or \
        (not isinstance(hash_zero, str)) or \
            (not isinstance(proof_digest_n, str)):
        return False

    # is it a start proof
    if n == 0 and proof_digest_n == hash_zero:
        return True
    else:
        # can hash zero be reproduced for a given range
        # were last value should be equal hash_zero
        proof_chain_digest = get_hash_chain(n, proof_digest_n)[-1]
        return (proof_chain_digest == hash_zero)

# %%


# Creates Class for the hashchains and the seeds dictionaries
class HashChains:
    def __init__(self, int_value=None):
        self.seeds = []
        self.hash_chains = {}
        self.mdp = []
        self.commitments = []

        # set values when it's possible
        if int_value:
            self.create_hash_chains(int_value)
            self.create_mdp_list(int_value)
            self.create_commitments()

    def set_hash_chains(self, seeds=None, hash_chains=None):
        if (seeds and hash_chains) and \
                (len(seeds) == len(hash_chains)):
            self.seeds = seeds
            self.hash_chains = hash_chains

    def create_hash_chains(self, int_value):
        h, s = get_hash_multichain(int_value)
        self.set_hash_chains(s, h)

    def create_mdp_list(self, int_value):
        self.mdp = mdp(int_value)

    def create_commitments(self):
        self.commitments = get_commitment_hash_wire(self.mdp, self.hash_chains)

# %%
