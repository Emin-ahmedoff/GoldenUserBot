# Faster & Secure & Special Container #
# Thanks to mkaraniya & zakaryan2004

FROM emin-ahmedoff/goldenuserbot:latest
RUN git clone https://github.com/Emin-ahmedoff/GoldenUserBot /root/GoldenUserBot
WORKDIR /root/GoldenUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
