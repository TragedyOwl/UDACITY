import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

engagement_fn = './data/daily-engagement.csv'
submissions_fn = './data/project-submissions.csv'

engagement = read_csv(engagement_fn)
submissions = read_csv(submissions_fn)

print(engagement[0])
print(submissions[0])