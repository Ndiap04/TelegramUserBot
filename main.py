from pyrogram import Client 

Client = Client(
    'nomesessione', #nome sessione
    session_string = '1BVtsOHsBu8GBoqO6vuvDv-CgXRxqMXmup0WaO_xuKEVnTRyuUmzDBtAgwctIkE1JxldXFFQkD82GfFz2mmcPUFlZQmy6iX2ZWMnTdJ-D34_7_P2YrwGqU22zLUuXKdCBijhK4I_u-nBurqQl7p7fAB2Iw8RW_OaBG18sbnUNkvkqMml1WcXKRBeHqN_dFr5StWssELeZKcClkZWDKJuqHR9oybfcg3zlwmsueizaXZ0k9zsQYpi56ZZP6SpItBfdlUlVISnKqjNAYotPjqCmqdI0V39j14juwYykIC76I4UEvZvA8NTqRwhd1tv9848aPODgQnI2KpMk424q_yhF_cg2iKAzz1s=', #string session che ricavi da generatorestring.py avviandolo
    api_id = "5341004", #api id che prendi da my.telegram.org
    api_hash = "49660f97ddc3eae70ef5b64595af60a5", #api hash che prendi da my.telegram.org
    plugins = dict(root="plugins") #cartella dei plugins
)

if __name__ == "__main__":
    Client.run()
