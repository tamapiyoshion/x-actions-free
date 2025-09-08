import os, tweepy, sys

def get_api():
    auth = tweepy.OAuth1UserHandler(
        os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'],
        os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET']
    )
    return tweepy.API(auth)

def pop_first_line(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f.readlines()]
    return (lines[0].strip(), lines[1:]) if lines else (None, lines)

def write_lines(path, lines):
    with open(path, 'w', encoding='utf-8') as f:
        for l in lines: f.write(l + '\n')

def main():
    q = 'data/queue.txt'
    if not os.path.exists(q): print('queue.txt not found'); sys.exit(0)
    text, rest = pop_first_line(q)
    if not text: print('no text to post'); sys.exit(0)
    status = get_api().update_status(status=text)
    print('posted:', status.id)
    write_lines(q, rest)

if __name__ == '__main__': main()
