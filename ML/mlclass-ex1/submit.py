#  I got this script from someone in the fall '11 ML class and I am embarressed to say I don't remember their name
# and since the class has gone off line I can't review the forums to work out who it was ...
# as a result I can't give credit where credit is due, except to say it is to an otherwise anonymous coder ...

# note the upload URLs are from the Fall '11 class, so these will have to be updated ot work with any new ML class

from getpass import getpass
import sha
import random
from urllib import urlopen, urlencode
from random import sample
import os.path
from numpy import *

__all__ = ['submit']

# ================== CONFIGURABLES FOR EACH HOMEWORK ==================

challenge_url = 'http://www.ml-class.org/course/homework/challenge'
submit_url = 'http://www.ml-class.org/course/homework/submit'
homework_id = '1'

part_names = [
    'Warm up exercise',
    'Computing Cost (for one variable)',
    'Gradient Descent (for one variable)',
    'Feature Normalization',
    'Computing Cost (for multiple variables)',
    'Gradient Descent (for multiple variables)',
    'Normal Equations',
    ]

srcs = [
    'warmup_exercise.py',
    'compute_cost.py',
    'gradient_descent.py',
    'feature_normalize.py',
    'compute_cost_multi.py',
    'gradient_descent_multi.py',
    'normal_eqn.py',
    ]

def output(part_id):
    X1 = matrix([ones(20), exp(1) + exp(2) * arange(0.1, 2.1, 0.1)]).T
    Y1 = X1[:,1] + sin(X1[:,0]) + cos(X1[:,1])
    X2 = hstack((X1, power(X1[:,1], 0.5), power(X1[:,1], 0.25)))
    Y2 = power(Y1, 0.5) + Y1

    fname = srcs[part_id-1].rsplit('.',1)[0]
    mod = __import__(fname, fromlist=[fname], level=1)
    func = getattr(mod, fname)

    if part_id == 1:
        return sprintf('%0.5f ', func())
    elif part_id == 2:
        return sprintf('%0.5f ', func(X1, Y1, matrix([0.5, -0.5]).T))
    elif part_id == 3:
        return sprintf('%0.5f ', func(X1, Y1, matrix([0.5, -0.5]).T, 0.01, 10))
    elif part_id == 4:
        return sprintf('%0.5f ', func(X2[:,1:4]))
    elif part_id == 5:
        return sprintf('%0.5f ', func(X2, Y2, matrix([0.1, 0.2, 0.3, 0.4]).T))
    elif part_id == 6:
        return sprintf('%0.5f ', func(X2, Y2, matrix([-0.1, -0.2, -0.3, -0.4]).T, 0.01, 10))
    elif part_id == 7:
        return sprintf('%0.5f ', func(X2, Y2))

# ============================== SUBMIT ===============================

def submit(part_id=None):
    print '==\n== [ml-class] Submitting Solutions | Programming Exercise %s\n==', \
          homework_id

    if part_id is None:
        part_id = prompt_part()

    if not is_valid_part(part_id):
        print '!! Invalid homework part selected.'
        print '!! Expected an integer from 1 to %d.' % (len(part_names)+1)
        print '!! Submission Cancelled'
        return

    login, password = login_prompt()
    if not login:
        print '!! Submission Cancelled'
        return

    submit_parts = [part_id] if part_id <= len(part_names) else range(1,len(part_names)+1)

    print '\n== Connecting to ml-class ... '

    for part_id in submit_parts:
        # Submit this part
        # Get Challenge
        login, ch, signature = get_challenge(login)
        if not login or not ch or not signature:
            # Some error occured, error string in first return element.
            print '\n!! Error: %s\n' % login
            return

        ch_resp = challenge_response(login, password, ch)
        result, s = submit_solution(login, ch_resp, part_id, output(part_id), source(part_id), signature)
        print '\n== [ml-class] Submitted Homework %s - Part %d - %s' % (
                homework_id, part_id, part_names[part_id-1])
        print '== %s' % s.strip()

# ============================== HELPERS ==============================

def sprintf(fmt, arg):
    "emulates (part of) Octave sprintf function"
    if isinstance(arg, tuple):
        # for multiple return values, only use the first one
        arg = arg[0]

    if isinstance(arg, matrix):
        # convert to array for easier serialization
        arg = array(arg)

    if isinstance(arg, ndarray):
        # concatenates all elements, column by column
        return ''.join(fmt % e for e in arg.T.reshape(arg.size))
    else:
        return fmt % arg

def prompt_part():
    print '== Select which part(s) to submit:'
    for i, name in enumerate(part_names):
        print '==   %d) %s [%s]' % (i+1, name, srcs[i])
    print '==   %d) All of the above\n==' % (len(part_names)+1)
    selpart = raw_input('Enter your choice [1-%d]:' % (len(part_names)+1))
    try:
        return int(selpart)
    except ValueError:
        return -1

def is_valid_part(part_id):
    return part_id and 1 <= part_id <= len(part_names)+1

def login_prompt():
    login = raw_input('login (Email address): ')
    password = getpass('Password: ')
    return login, password

def challenge_response(email, passwd, challenge):
    salt = ')~/|]QMB3[!W`?OVt7qC"@+}'
    s = sha.new(salt + email + passwd).hexdigest()
    s = sha.new(challenge + s).hexdigest()
    sel = sample(xrange(len(s)), 16)
    return ''.join(s[i] for i in sorted(sel))

def source(part_id):
    fname = srcs[part_id-1]
    try:
        # try relative path
        f = open(fname)
    except IOError:
        # else try the directory of this script
        fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
        f = open(fpath)
    try:
        src = f.read() + '||||||||'
    finally:
        f.close()
    return src

def get_challenge(email):
    f = urlopen(challenge_url, urlencode({'email_address': email}))
    try:
        return f.read().strip().split('|')
    finally:
        f.close()

def submit_solution(email, ch_resp, part, output, source, signature):
    params = {
    'homework': homework_id,
    'part': str(part),
    'email': email,
    'output': output,
    'source': source,
    'challenge_response': ch_resp,
    'signature': signature }

    f = urlopen(submit_url, urlencode(params))
    try:
        return 0, f.read()
    finally:
        f.close()
