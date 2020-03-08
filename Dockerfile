FROM zzzcat/dispshell:python3

WORKDIR /cloudinary-work

#
# cloudinary CLI
#
COPY cloudinary-requirements.txt .
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r cloudinary-requirements.txt && \
    echo "*** INSTALLED: cloudinary modules ***"

#
# cloudinary samples
#
COPY cloudinary.sh .
COPY example ./example
CMD ["bash", "cloudinary.sh"]