from setuptools import setup, find_packages

setup(
    name='twinsight_model',
    version='0.1.0',
    author='Lakshmi Anandan',
    author_email='lakshmi19anandan@gmail.com',
    description='A predictive modeling package for personalized health risk estimation leveraging All of Us data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Lakshmi2819/Regression-Model',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'numpy',
        'google-cloud-bigquery', # Required by dataloader.py
        'pyyaml',                # Required by dataloader.py
        'joblib',                # Explicitly list joblib for clarity, though often transitive
    ],
    entry_points={
        'console_scripts': [
            'twinsight-cli = cli:main'
        ]
    }, 
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
