import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import csv

# Fetch the service account key JSON file contents
cred = credentials.Certificate('cloverflow-firebase-adminsdk.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cloverflow-4dd16.firebaseio.com/'
})

# Get a database reference to our blog.
ref = db.reference('clones/')
# print(ref.get())

pairs_ref = ref.child('pairs')

filename = '/Users/Chaiyong/IdeasProjects/StackoverflowChecker/indv_simian_df_130901_pt1+2+3+4_firebase.csv'
bigdict = {}
count = 0
rowcount = 0

with open(filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # count how many record we have
    for row in readCSV:
        rowcount += 1

with open(filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        if count > 199:
            break
        # print(row)
        codefile1 = open('/Users/Chaiyong/Downloads/stackoverflow/stackoverflow_formatted/' + row[0],'r')
        code1 = codefile1.read()

        codefile2 = open('/Users/Chaiyong/Downloads/stackoverflow/QualitasCorpus-20130901r/projects_130901r_pt1+2+3/' + row[3], 'r')
        code2 = codefile2.read()

        codefile2orig = open(
            '/Users/Chaiyong/Downloads/stackoverflow/QualitasCorpus-20130901r/projects_130901r_pt1+2+3/' + row[3],
            'r')
        code2orig = codefile2orig.read()
        code2orig = ""

        bigdict.update({
                count: {
                    'file1': row[0],
                    'start1': int(row[1]),
                    'end1': int(row[2]),
                    'code1': code1,
                    'code1orig': code1,
                    'file2': row[3],
                    'start2': int(row[4]),
                    'end2': int(row[5]),
                    'code2': code2,
                    'code2orig': code2,
                    'classification': code2orig,
                    'notes': '',
                    'total': 200
                    # 'total': rowcount

                }
            })
        count += 1

    print "Size: ", len(bigdict)
    pairs_ref.set(bigdict)

    print "done:", count