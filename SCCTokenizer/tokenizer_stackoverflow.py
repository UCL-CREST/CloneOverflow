import json
import logging
import re
import os, platform
import collections
import sys
import hashlib
import datetime as dt


separators = [';', '.', '[', ']', '(', ')', '~', '!', '-', '+', 
	'&', '*', '/', '%', '<', '>', '^', '|', '?', '{', 
	'}', '=', '#', ',','"', '\\', ':', '$', "'", '`', '@']
comment_inline = "//"
comment_inline_pattern = comment_inline + '.*?$'
comment_open_tag = "/\\*"
comment_close_tag = "\\*/"
comment_open_close_pattern = comment_open_tag + '.*?' + comment_close_tag
# proj_id_flag = "2"

FILE_blocks_stats_file = 'so-stats.stats'
FILE_blocks_tokens_file = 'so-tokens.tokens'

block_count = 0


def tokenize_python_blocks(block_string):
    # This function will return ((blocks_tokens,blocks_stats), block_parsing_times)

    (start_line, end_line) = ('NULL', 'NULL')
	
    block_stats = 'ERROR'
    block_tokens = 'ERROR'

    block_hash = 'ERROR'
    block_lines = 'ERROR'
    block_LOC = 'ERROR'
    block_SLOC = 'ERROR'

    h_time = dt.datetime.now()
    m = hashlib.md5()
    # m.update(block_string.encode("utf-8"))
    block_hash = m.hexdigest()
    hash_time = (dt.datetime.now() - h_time).microseconds
    
    block_lines = block_string.count('\n')
    if not block_string.endswith('\n'):
      block_lines += 1
    block_string = "".join([s for s in block_string.splitlines(True) if s.strip()])
   
    block_LOC = block_string.count('\n')
    if not block_string.endswith('\n'):
      block_LOC += 1

    r_time = dt.datetime.now()
    # Remove tagged comments
    block_string = re.sub(comment_open_close_pattern, '', block_string, flags=re.DOTALL)
    # Remove end of line comments
    block_string = re.sub(comment_inline_pattern, '', block_string, flags=re.MULTILINE)
    re_time = (dt.datetime.now() - r_time).microseconds

    block_string = "".join([s for s in block_string.splitlines(True) if s.strip()]).strip()

    block_SLOC = block_string.count('\n')
    if block_string != '' and not block_string.endswith('\n'):
      block_SLOC += 1

    block_stats = (block_hash, block_LOC)

    # Rather a copy of the file string here for tokenization
    block_string_for_tokenization = block_string

    #Transform separators into spaces (remove them)
    s_time = dt.datetime.now()
    for x in separators:
      block_string_for_tokenization = block_string_for_tokenization.replace(x,' ')
    se_time = (dt.datetime.now() - s_time).microseconds

    ##Create a list of tokens
    block_string_for_tokenization = block_string_for_tokenization.split()
    ## Total number of tokens
    tokens_count_total = len(block_string_for_tokenization)
    ##Count occurrences
    block_string_for_tokenization = collections.Counter(block_string_for_tokenization)
    ##Converting Counter to dict because according to StackOverflow is better
    block_string_for_tokenization=dict(block_string_for_tokenization)
    ## Unique number of tokens
    tokens_count_unique = len(block_string_for_tokenization)

    t_time = dt.datetime.now()
    #SourcererCC formatting
    tokens = ','.join(['{}@@::@@{}'.format(k.encode("ascii", "ignore"), v) for k,v in block_string_for_tokenization.iteritems()])
    token_time = (dt.datetime.now() - t_time).microseconds

    # MD5
    h_time = dt.datetime.now()
    m = hashlib.md5()
    m.update(tokens)
    hash_time += (dt.datetime.now() - h_time).microseconds

    block_tokens = (tokens_count_total,tokens_count_unique,m.hexdigest(),'@#@'+tokens)

    return ((block_tokens, block_stats), [se_time, token_time, hash_time, re_time])


def process_contents(post_id, method_id, block_string, FILE_tokens_file, FILE_stats_file, logging):
	
    (block_data, block_parsing_times) = tokenize_python_blocks(block_string)
    ww_time = dt.datetime.now()
   
    (blocks_tokens, blocks_stats) = block_data
    global block_count
    block_id = str(block_count)

    (block_hash, block_LOC) = blocks_stats
    (tokens_count_total,tokens_count_unique,token_hash,tokens) = blocks_tokens

    # Adjust the blocks stats written to the files, file stats start with a letter 'b'
    # FILE_stats_file.write(','.join([post_id, block_id, '\"' + block_hash + '\"', method_id, str(block_LOC)]) + '\n')
    # FILE_tokens_file.write(','.join([post_id, block_id, str(tokens_count_total), str(tokens_count_unique), method_id, token_hash + tokens]) + '\n')
    FILE_tokens_file.write(','.join(
        [post_id, method_id + tokens]) + '\n')
    w_time = (dt.datetime.now() - ww_time).microseconds

    logging.info('Successfully ran process_contents ' + post_id)

    return block_parsing_times + [w_time] # [s_time, t_time, w_time, hash_time, re_time]


def process_so_file(FILE_tokens_file, FILE_stats_file):

    with open("so.txt", "r") as f:
        all_snippets = f.read()
        blocks = all_snippets.split("===@@@UCI===")
        for item in blocks:
            item = item.strip()
            if len(item)==0:
                continue
            else:
                try:
                    global block_count
                    lines = item.split("\n")
                    post_id = lines[0]
                    method_id = lines[1]
                    snippet = "\n".join(lines[2:])
                    process_contents(post_id, method_id, snippet.decode('UTF-8'), FILE_tokens_file, FILE_stats_file, logging)
                    block_count += 1
                    
                except Exception as e:
                    logging.warning("%s cannot be pasred by so text parser" % item)
                    logging.warning(e)


def main():

    # logging setting    
    FORMAT = '[%(levelname)s] %(message)s'
    logging.basicConfig(level=logging.DEBUG,format=FORMAT)
    file_handler = logging.FileHandler('so-more-than-10-log.log')
    file_handler.setFormatter(logging.Formatter(FORMAT))
    logging.getLogger().addHandler(file_handler)

    p_start = dt.datetime.now()

    with open(FILE_blocks_tokens_file, 'w') as FILE_tokens_file, \
         open(FILE_blocks_stats_file, 'w') as FILE_stats_file:
        
        print "starting"
        process_so_file(FILE_tokens_file, FILE_stats_file)

    p_elapsed = dt.datetime.now() - p_start
    logging.info('All done in %s' % p_elapsed)
    print 'All %s blocks done in %s' % (block_count, p_elapsed)


main()


	






