FROM django
ADD . /NZGoalDtree
WORKDIR /NZGoalDtree
RUN pip install --proxy=127.0.0.1:3128 -r requirements.txt
