
import os
import datetime

def main(pelican_content_dir, output_dir):

    pelican_posts = get_pelican_post_files(pelican_content_dir)
    files_with_errors = []

    for p_file in pelican_posts:
        with open(p_file, "r") as f:
            content = f.readlines()

        parsing_front_matter = True
        hugo_content = []
        content = [x.strip() for x in content]

        # use TOML format
        hugo_content.append('+++')

        for line in content:
            line = line.strip()
            if line  == '\n' or len(line) == 0:
                if parsing_front_matter:
                    hugo_content.append('+++')
                    parsing_front_matter = False

                hugo_content.append('')
                continue

            if parsing_front_matter:
                h_line = to_hugo_frontmatter(line)
                if h_line:
                    hugo_content.append(h_line)
                else:
                    files_with_errors.append(f)
                    break
            else:
                hugo_content.append(to_hugo_content(line))

        h_fname = hugo_output_path(output_dir, p_file )
        with open(h_fname, "w") as hf:
            hf.write('\n'.join(hugo_content))


def hugo_output_path(fpath, fname):

    return os.path.join(fpath,os.path.basename(fname))


def to_hugo_content(line):
    return line


def to_hugo_frontmatter(line):
    r = None
    if line.upper().startswith('TITLE:'):
        r = 'title = "{}"'.format(_content(line))

    if line.upper().startswith('DATE:'):
        s = _content(line)
        d = None
        try:
            d = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S").date()

        except ValueError:
            try:
                d = datetime.datetime.strptime(s, "%Y-%m-%d").date()
            except ValueError:
                pass
        if d:
            r = 'date = "{}"'.format(d.strftime("%Y-%m-%d"))


    if line.upper().startswith('SLUG:'):
        r = 'slug = "{}"'.format(_content(line))

    if line.upper().startswith('TAGS:'):
        p_tags = _content(line).split(',')
        h_tags = ', '.join(['"{}"'.format(t.strip().lstrip()) for t in p_tags])
        r = 'tags = [{}]'.format(h_tags)

    if line.upper().startswith('LANG:'):
        r = 'lang = "{}"'.format(_content(line))

    if line.upper().startswith('CATEGORY:'):
        r = 'categories = ["{}", ]'.format(_content(line))

    if line.upper().startswith('TITLE_LINK:'):
        r = 'linkTitle = "{}"'.format(_content(line))

    return r


def _content(s, divider=':'):
    return s[s.find(divider)+1:].lstrip()


def get_pelican_post_files(pelican_content_dir, file_extension='md'):

    pelican_posts = []
    for root, dirs, files in os.walk(pelican_content_dir):
        for name in files:
            if os.path.splitext(name)[1][1:] == file_extension:
                pelican_posts.append(os.path.join(root, name))

    return pelican_posts


if __name__ == '__main__':
    pelican_content_dir =  "/Users/robertoz/Dropbox/blog/code.zoia.org/content/"
    output_dir = "content"

    try:
        os.mkdir(output_dir)
    except FileExistsError:
        pass

    main(pelican_content_dir, output_dir)
