from setuptools import setup, find_packages

setup(
    name="FakeApp",
    version="1.0",
    packages=find_packages(),
    entry_points={
      'paste.app_factory': """
      basic_app=fakeapp.apps:make_basic_app
      other=fakeapp.apps:make_basic_app2
      """,
      'paste.filter_factory': """
      caps=fakeapp.apps:make_cap_filter
      """,
      },
    )
