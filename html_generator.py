# coding:           utf-8
# Created on :      03/02/2015
# Last modified:    03/04/2015
# Author:           Shanfan Huang
# Description:      Course project for Intro to Programming - WIP 

# This program is supposed to work like posting to a blog.
# The user would fill in the title and content for a new article,
# select a section (category) this article blongs to,
# then the program will output the article to the html file.

# As of 03/04/2015, this program is not concerned about user input,
# only focuses on the output.

# Part 1: Create a data structure that reflects my HTML file
#         Fill in some testing data

sections = ["Getting started",
			"Stage 1: Make your web page",
			"Stage 2: Tell the Computer what to do",
			"Stage 3: Automate Your Page",
			"Stage 4: Let anyone modify your page",
			"Stage 5: Choose your next steps"]

all_articles = [[sections[0], "Preparation", '''
				<p class="title">Setting intentions</p>
				<p>I'm a user experience designer by profession, but I always considered myself as a maker. I don't just want to come up with a draft plan. I want to see things working as I intend them to. I have many ideas doodled down in my sketchbook. My greatest aspiration on this journey is to bring all my ideas to life one day.</p>
				<p>I have engough knowledge in HTML/CSS/jQuery to build small UI demos. But this body of knowledge is very fragmented. I want to consolidate that. Also I kept finding myself constrained by my lack of server-side knowledge. So I decided to take this nano degree to comb through what I knew and to fill in all the gaps. I'd like to finish this degree as soon as possible, then continue to the Front End Development Nano Degree. I'm also very interested in data analysis and visualization. That could be the 3<sup>rd</sup> one.</p>
			
				<p class="title">Think like a programmer</p>
				<p>Thinking like a programmer means we use:</p>
				<ul>
					<li><b>Procedural Thinking:</b> Breaking large goals into smaller steps that eventually get to the goal</li>
					<li><b>Abstract Thinking:</b> Think of a universal solution that could be applied to various similar situations, not just one specific situation.</li>
					<li><b>Systems Thinking:</b>
						<ul>
							<li>Systematic Debugging</li>
							<li>Big Picture Thinking</li>
							<li>Decision Making</li>
						</ul>
					</li>
					<li><b>Technological Empathy</b> - I find this one most enchanting:
						<p>Computers are "stupid". We need to help the computer to understand what the problem is - speaking the language a computer would understand - so that the computer can do what we want it to do.</p>
						<p>Computer empathy is the ability to understand what a computer is, how it works, and what it's good and bad at doing.</p>
					</li>
					<li><b>Debugging:</b>
						<p>Debugging is a systematic process of relentlessly identifying the cause of a computer program that doesn't work.When a program doesn't work, it's because there is a mistake (also known as a "bug") somewhere in the computer code. Since these mistakes are an unavoidable part of programming, every good programmer has a system for fixing them and that system usually looks something like this:</p>
						<ol>
							<li>Collect evidence (what makes this program fail?)</li>
							<li>Generate theories (what may have caused this problem?)</li>
							<li>Test those theories (if my theory is correct, how could I find out?)</li>
							<li>Fix the problem</li>
						</ol>
					</li>
				</ul>
			'''],
			    [sections[1], "HTML Basics", '''
			    <p class="title">How the "Web" is structured?</p>
				<p><em>HTML</em> is the basic document format that contains all the contents the author wants to share with the rest of the web.</p>
				<p>Many HTML files are hyperlinked through <em>URLs</em>. By hyperlinking the URLs, we'll be able to navigate from one file to another, hence the "web".</p>
				<p><em>HTTP</em> is the internet protocol that allows my browser to access the files stored on the server.</p>
			
				<p class="title">HTML Basics</p>
				<p>HTML files are written with tags and attributes.</p>
				<p>The open tag and its close tag together with their enclosed content are called <b>Element</b>. Note that some tags are <b>void tag</b> which by itself is an element. Such as <code>&#60;br></code> or <code>&#60;img></code>. Some tages are <b>inline tag</b>, which stays in the line of the text. Some others are <b>block tag</b>, which create a rectangle box surrounding the text or image and block the content off the flowing line of the previous text. There's also another type of tag called <b>Container Tags</b>. Unlike 'paragraph element' or 'header 1 element' which specifies the importance or purpose of the text, the <em>container tag</em> is invisible, and doesn't serve any specific content but to just <em>contain</em> the elements.</p>
			'''],
				[sections[1], "structured document", '''
				<p class="title">HTML, CSS and Javascript</p>
				<p><b>HTML</b> is like the structure of the house. <br>
				<b>CSS</b> is like the interior design of the house - what color is the wall, what patter is the rug...<br>
				<b>Javascript</b> is the tools to help you get around the house and to perform certain tasks. Things like the stove for cooking a meal, a screw driver to hang up a shelf… are a good analogy of what Javascript does to a webpage.
				</p>
				<p class="title">Tree-like Structure &amp; Boxify</p>
				<blockquote>DOM, Document Object Model, "defines the logical structure of documents and the way a document is accessed and manipulated." <br><a href="www.w3.org" target="_blank">W3 School</a>.</blockquote>
				<p>HTML tags or elements are written in a nested structure, like a tree. We should carefully nesting the block elements inside the container elements, and inline elements inside the block elements. Also we need to pay attention to the semantic use of the the tags. For example, a title should go into tags like <code>&#60;h1></code> or <code>&#60;h2></code>. The main text content is often wrapped in <code>&#60;p></code>. HTML file should be well structured, readable, and ready for the browser to interprete.</p>
				<p>Since all the HTML elements are essentially a rectangular box, when a front end developer receives a design mockup from the graphic designer, the first thing she does is to 'boxify' the mockup, which will serve as the basis of the HTML structure she would write later.</p>
			'''],
            [sections[2], "placeholder titile", "<p>lorem ipsum...</p>"],
            [sections[3], "placeholder titile", "<p>lorem ipsum...</p>"],
            [sections[3], "placeholder titile", "<p>lorem ipsum...</p>"],
            [sections[3], "placeholder titile", "<p>lorem ipsum...</p>"],
            [sections[4], "placeholder titile", "<p>lorem ipsum...</p>"],
            [sections[4], "placeholder titile", "<p>lorem ipsum...</p>"],
            [sections[5], "placeholder titile", "<p>lorem ipsum...</p>"],
            [sections[5], "placeholder titile", "<p>lorem ipsum...</p>"]
            ]

#Part 2: Write the function that generates the HTML content

def gen_article_html(title, content):
	# Generate each article that has a title and a body of content
	article_title = '<h3>' + title + '</h3>'
	article_content = '''
		<div class="content">
			''' + content + '''
		</div>'''
	article_html = '''
	<article>
		''' + article_title + article_content + '''
	</article>'''
	return article_html

 
def gen_section_html(section, articles):
 	# Put all the articles that belong to the same section together.
  	section_title = '<h2>' + section + '</h2>'
  	section_content = ''
  	
  	for article in articles:
  		if article[0] == section:
  			section_content += gen_article_html(article[1], article[2])
  	
  	section_html = '''<section>
  	''' + section_title + section_content + '''
	</section>
	'''
  	return section_html

def generate_html(sections, articles):
	# Output the entire html with all the sections
	html = ''
	for section in sections:
		html += gen_section_html(section, articles)
	return html

print generate_html(sections, all_articles)