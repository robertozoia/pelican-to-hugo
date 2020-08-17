import unittest

import pelican_to_hugo

class TestPelicanToHugoFrontMatter(unittest.TestCase):
    """
    Tests pelican to Hugo TOML Front Matter
    """

    def test_title(self):
        cases = [
            ('Title: Java Programming 101', 'title = "Java Programming 101"'),
            ('Title: Java Programming: 101', 'title = "Java Programming: 101"'),
        ]
        for t_pelican, t_hugo in cases:
            self.assertEqual(
                pelican_to_hugo.to_hugo_frontmatter(t_pelican),
                t_hugo
            )

    def test_date(self):
        cases = [ # Deliberately truncate time
            ('Date: 2011-04-15 19:24:58', 'date = "2011-04-15"' ),
            ('Date: 2011-04-15', 'date = "2011-04-15"'),
        ]
        for t_pelican, t_hugo in cases:
            self.assertEqual(
                pelican_to_hugo.to_hugo_frontmatter(t_pelican),
                t_hugo
            )

    def test_slug(self):
        cases = [
            ('Slug: java-programming-101', 'slug = "java-programming-101"'),
        ]
        for t_pelican, t_hugo in cases:
            self.assertEqual(
                pelican_to_hugo.to_hugo_frontmatter(t_pelican),
                t_hugo
            )

    def test_tags(self):
        cases = [
            ('Tags: exceptions, inheritance, Java programming, polymorphism',
            'tags = ["exceptions", "inheritance", "Java programming", "polymorphism"]'),
        ]
        for t_pelican, t_hugo in cases:
            self.assertEqual(
                pelican_to_hugo.to_hugo_frontmatter(t_pelican),
                t_hugo
            )

    def test_title_link(self):
        cases = [
            ('title_link: http://shawnblanc.net/2008/02/interview-john-gruber/',
             'linkTitle = "http://shawnblanc.net/2008/02/interview-john-gruber/"'),
        ]
        for t_pelican, t_hugo in cases:
            self.assertEqual(
                pelican_to_hugo.to_hugo_frontmatter(t_pelican),
                t_hugo
            )

    def test_categories(self):
        cases = [
            ('category:  coding', 'categories = ["coding", ]'),
        ]
        for t_pelican, t_hugo in cases:
            self.assertEqual(
                pelican_to_hugo.to_hugo_frontmatter(t_pelican),
                t_hugo
            )



if __name__=='__main__':
    unittest.main()
