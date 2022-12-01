import pytest
from incolumepy.utils.changelog import (
    changelog_write, changelog_messages, update_changelog, msg_classify
)

__author__ = '@britodfbr'  # pragma: no cover


def test_msg_classify(return_git_tag):
    assert msg_classify(return_git_tag) == ''
