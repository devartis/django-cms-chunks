#! coding: utf-8
from django import template
from cms_chunks.models import Chunk
from cms.templatetags.placeholder_tags import RenderPlaceholder

register = template.Library()


class ChunksNode(template.Node):
    def __init__(self, key, parser, tokens, random=False):
        self.key = key
        self.random = random
        self.parser = parser
        self.tokens = tokens

    def render(self, context):
        chunks = Chunk.objects.with_tag(self.key)
        if chunks:
            output = "\n".join(
                (RenderPlaceholder(self.parser, self.tokens).render_tag(context, chunk.code, None) for chunk in
                 chunks))
            return output
        else:
            return ''


def parse_boolean(tokens):
    boolean_string = tokens[2]
    true_list = ["True", "true"]
    false_list = ["False", "false"]
    boolean_list = true_list + false_list
    is_boolean_string = boolean_string in boolean_list
    if is_boolean_string:
        return boolean_string in true_list
    else:
        template.TemplateSyntaxError("The second argument of %r tag must be a '%s'" % (tokens[0], boolean_list))


@register.tag(name='chunks')
def do_chunk_node(parser, token):
    tokens = token.split_contents()
    token_len = len(tokens)
    if token_len == 2:
        random = False
    elif token_len == 3:
        random = parse_boolean(tokens)
    else:
        raise template.TemplateSyntaxError("%r tag requires a 1 or 2 argument" % token.contents.split()[0])
    key = tokens[1]

    return ChunksNode(key, parser, tokens[1:2], random)


__author__ = 'lgomez'
