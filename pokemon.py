# Israel Méndez Crespo
# Scripting Languages
# COP 2830C Section 31462
# Projects 1.2 and 1.3

import winsound
import time
import sys
import random


# Winsound works in Windows, but for Mac and Linux you can uncomment
# the import os line and replace the winsound play functions with
# the ones below. These will only play the sound and do not seem to
# to offer pause functionality but it can be added with the pysound library

# import os
# os.system("aplay battle.wav&") #Linux
# os.system("afplay battle.wav&") #Mac

# slow_prompt and slow_draw are similar functions made to imitate the
# pacing of 16-bit generation prompts. I would have used just one but
# the time function is throws a data type error when passing ints and floats

def slow_prompt(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.025)


def slow_draw(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.000001)


def print_bulbasaur():
    slow_draw("""\n
        MMMMMMMMMNNMMMdyMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMN++yd//omMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMhhhy+/++///oydmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMmooho///+++//////:::::///////++symMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMyosy////::::::////++///////////:::ohNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMhooh//////:::::::::://+++/////////:::sNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMNoooh////////::::::::::::/o//////////::/mMMMMMMMMMMMMMMNmmMMMMMMMMMM
        MMMMMMMsooys///////////////:::o++++++++////++++oddhhhhddmNho/:::-oNMMMMMMMM
        MMMMMNsoooy+/////////////////o+::::::::/+++/::::::::------:///:::-/NMMMMMMM
        MMMMNsoooyo+/////////////////s::::::::::::::::+ssoo+/:::::::::::::-oMMMMMMM
        MMMNsoooyso/////////////////o/::::::::::::::::/syyyyyhyso+/:::::::/:mMMMMMM
        MMNoooosso+//////////////+ooy:::::::::::::::::::/oyyyyyyyyho::::::::sMMMMMM
        MNsooooyoo+////////////+ooooo::::::::::::::::::::::+syyyys+::::::::::/mMMMM
        Myoooosoooo//////////+oooosy/::::::::::/::::::::::::::/+/::::hy/:::////dMMM
        Nooooosoooo+////////ooooso:o::::::::+shds-/:::/+:::::::::::::sy/:+:s+`:/dMM
        dooooooooooo+/////+oooso:::o:::::::oysoyh+ :/::/+::::+hyo::::::::+:sss :/NM
        hoooooooooooooo+ooosyho+::/+::::::+ys- +sy` ./::/::::+hyyy/:::::::::+s- +oM
        hoooooooossooooooyhhyyyh/:+:::::::sss` /sy.  ./:::::::hyyo:::::::::-:s/ -/N
        moooooooooosssyhhyyyyyh+::/:::::::yss:`osy.   +::::::://:::::::::::/+s- ./y
        Myooooooooosohyyyyyyyh+:::::::::::yssssssy    /::::::::::::::::::::ysy.:/:s
        MMhooooooso//hyyyyyyy+:::::::::::::/+oooso----/:::::::::::::::::::::+/::::s
        MMMNhssss/:::oooooo+/::::::::::::://::::::::::::::::::::::/:::::/:::::///oN
        MMMMMNds:::::::::::::::::::::::::::::/+::++//::::::::::::::::::/++o+//:smMM
        MMMMMMs::::::::::::::::::::::://:::::::/+ssssyssssooooooosssssyyhs/:+hNMMMM
        MMMMMy::::::/:::++/+/:::::::::::///:::::::/oo++////////////++++//ohNMMMMMMM
        MMMMN::::::yyys+:+ss/:::::::::::::/so++/::::::/+++++++++++++++++:sMMMMMMMMM
        MMMMy::::::hyyyyyo:h/:::::::+ys+:::/yooosoooo+++++++oooooo+/:::--hMMMMMMMMM
        MMMMs:::::+hyyyyyy:+o:::::::oyyo/+::/sooooooooooooooooooo/shys/--NMMMMMMMMM
        MMMMs:::::+hyyyyo:/oy/:::::::/::oyhs+osoooooooooosssooooo/hyyysosMMMMMMMMMM
        MMMMd/:::::+sso/:/oood/:::::::::/hyyyshooossyhdNyooooooo+/hyysosMMMMMMMMMMM
        MMMMNo+/::::::::/ooooyy+:::::::::syyyosyssohMMMMNsoooooo+:/syoomMMMMMMMMMMM
        MMMMMdoo+///://+oooohMMMs:::::::::yhyyshsomMMMMMMMyoooooo/::::dMMMMMMMMMMMM
        MMMMMMmooooooooooosdMMMMMm+::::::::/++:hMNMMMMMMMMMmsoooo//://dMMMMMMMMMMMM
        MMMMMMMMds-oys.ydosMMMMMMMMdo:://:/:/://NMMMMMMMMMMMMNd//hds+dNMMMMMMMMMMMM
        MMMMMMMMMMNMMMMMMMMMMMMMMMMMMMms/dy::mmdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        \n\n""")


def print_charmander():
    slow_draw("""\n
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMMMMMMMMMdyso+++osydNMMMMMMMMMMMMMMMM
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMMMMMMds:------------/smMMMMMMMMMMMMM
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMMMMNo+:------------...-/hMMMMMMMMMMM
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMMMd++/--------------....-/mMMMMMMMMM
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMMm+++/:-::-------------.--:dMMMMMMMM
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMN++sd+o/-+--------------/--/MMMMMMMM
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMMMs+yNo .y/:--------------/-+hMMMMMMMM
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMMm+ommo /h/:---------------/./NMMMMMMM
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMMs+yhmmymh-----------------+`ydMMMMMMM
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMN++hhddhhs-----------------ymdhMMMMMMM
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMd++osyssh/-----------------yhyhMMMMMMM
        ssssssssssssssssssssmMMMMMMMMMMMMMMMMy++++////------------------++/:mMMMMMM
        sssssssossssssssssssmMMMMMMMMMMMMMMMMh++++++/:---------------------:oMMMMMM
        ssssso+ossssssssssssmMMMMMMMMMMMMMMMMN++++h/:o+/::---/-----::---:+/+oMMMMMM
        hhhho+++ssssssssssssmMMMMMMMMMMMMMMMMMm++++soooooooo+++//::/++s++++sNMMMMMM
        hhhho+++s+/sssssssssmMMMMMMMMMMMMMMMMMMm++++so+::////+ooooooss+++ymMMMMMMMM
        hhhh++++o-.+osssssssmMMMMMMMMMMMMMMMMMMMy+++++o/:::::::/osoo+oymMMMMMMMMMMM
        hyys/:+++:--osssssshMMMMMMMMMMMMMMMMMMMNh++++++++++++++ooyhmMMMMMMMMMMMMMMM
        yo++-:++++++sssssshMMMMMMMMMMMMMMMmhs+::/+++++++++oo+++++oymMMMMMMMMMMMMMMM
        d/:..:++++++osssshMMMMNMMMMMMmhs+:-------://++++/:::/++/::--:+ydNMMMMMMMMMM
        yy:..:/++//+-+sssmMMMMd/+ss/:---------------:+:.......:/-/-------/oydmNMMMM
        o/+:..-++-.--./ssdMMdo+++/:----------------::``````````.//------------::ydN
        h://:..-//....-sssNMMh+++++::-------------/-`````````````+/------------:odM
        my+++-...-..-+sssyMMMMMNdhso+//:::::///:-/.``````````````.s//:::::::--:NMMM
        mdo++:.....-sssssyMMMMMMMMMMMNmmmmy++/:-/.````````````````+NmmmmmmmmmhsNMMM
        ddso+/-:-:/ossssssmMMMMMMMMMMMMMMs:::--/.`````````````````.MMMMMMMMMMMMMMMM
        mmdddNhohmdhhhhhhNMMMMMMMMMMMMMm/-----/-```````````````````NMMMMMMMMMMMMMMM
        NNNMMMh.-NMMMMMMMMMMMMMMMMMMMMh:------/````````````````````mMMMMMMMMMMMMMMM
        MMMMMMN--/NMMMMMMMMMMMMMMMMMMs-------/.````````````````````NMMMMMMMMMMMMMMM
        MMMMMMMy--:hMMMMMMMMMMMMMMMN+-------:+````````````````````-sdMMMMMMMMMMMMMM
        MMMMMMMNo:-:+hNMMMMMMMMMMMm:---------::-...```````````````/--/hMMMMMMMMMMMM
        MMMMMMMMd//://+oydmNMMMMMN:--------..-::-----............/:----+mMMMMMMMMMM
        MMMMMMMMMm:+++++++++++oooo/--------....+----------------//---...-dMMMMMMMMM
        MMMMMMMMMMNo/+++++++++++o++:-----------+--------------:++/::--...-mMMMMMMMM
        MMMMMMMMMMMMmo:/++++++++o+++/:--------:+-----------:/++++++//:----oMMMMMMMM
        MMMMMMMMMMMMMMNy+://+++s++++++////////o--------:/+++++++++++++////yMMMMMMMM
        MMMMMMMMMMMMMMMMMMmyo+/+++++++++++++ohsssyhdmNNddhys+++++++++++++oNMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMN+++++++++++hMMMMMMMMMMMMMMMMMs+++++++++++odMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMNs+++++++++oNMMMMMMMMMMMMMMMMMMhso+++++++o+//+sNMMMMM
        MMMMMMMMMMMMMMMMMMMMd/:o/o+++++++NMMMMMMMMMMMMMMMMMMMMMMMNmdhy/-/+::ssmMMMM
        MMMMMMMMMMMMMMMMMMMNhy/-:+s/-ooymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNddMmhMMMMMM
        MMMMMMMMMMMMMMMMMMMMMmdmMmoymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        \n\n""")


def print_squirtle():
    slow_draw("""\n
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdyso+++oooshdNMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy+:::::::::::----/sdMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmo:::::::/::::::::-----/yNMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs::::::////+:::::::::::::++mMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMN+:/::::ss  :h:::::::::::::/+oMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMo+++/::/hd++hNh:::::::::::::/omMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMh++++++//oydMMMmo:::::::::::::dhNMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMo++++++++/oodNNdy:::::::::::::osmMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMM+++++++++/:++oooo::::::::::::::++hMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMo+++++++++://::::::::::::::/:::://NMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMd+++++++oo++++++++++ooooooo++//+osMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMy+++++++++ooooooooo+++++++oooooyNMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMso+++++++++++++++++++++++++++smMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMNh+-+o+++++++++++++++++++//:/odNMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMdo+s.:/ssoo++++++++++++++//+ohdmNMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMNy++os+o+o+++oo+ooooooo+oo++///+//++shmNMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMNoossyo+++/::::/+////////:::::-.-//:::::/ohmMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMssooso+++/::::--:+/::::::::--....-+/:::::--:+ymMMMMM
        MMMMMMMMMMMMMMMMMMMMMMdo++oy++++::::::-::+/::::--.----::-.//:::::::::/oo+yM
        MMMMMMMMMMMMMMMMMMMMMN+/++o+++++/:::::::::+/::::+:----.....//::::::::+o+sNM
        MMMMMMMMMMMMMMMMMMMMMy//+++-o++++/::::///::/..../-..........+:::////+oo+odM
        MMMMMMMMMMMMMMMMMMMMM+//++o`/oo++++/::o+//:+....-/.........-osoooooooosss+m
        MMMMMMMMMMMMMMMMMMMMN///++s.-:+o+o+++/++++//:-...+........./-mNNNNNNNNMMMMM
        MMMMMMMMMMMMMMMMMMMMN+//++o/.::o+oo+++++++++/:...+........::.dMMMMMMMMMMMMM
        MMMMMMNNNNNNNMMMMMMMMs++++oo`::o://+++o+/:-......+.-----::+..mMMMMMMMMMMMMM
        MMMNho//::::/oymMMMMMysooooo.::o:::::::+:::::::::o::-----./:/MMMMMMMMMMMMMM
        MNy/::----------+dMMMmossoo/-:/+//::://-........./-........+sNMMMMMMMMMMMMM
        Mo::::::----------sNMMyosss-//+////++/::-......../-......../-/dMMMMMMMMMMMM
        h::::::::/:::::::::/dMNsos++/:::::::/+/::::--....+-......-/:---yMMMMMMMMMMM
        s:::::////////:::::::sNmsy+:::::::::::++:::::::::+----:::+:-----dMMMMMMMMMM
        h::::::::::::+::::::::/sds/::::::::::::/+:::://++++++//++:::----:MMMMMMMMMM
        N/:::::::::::+/:::::::::+o/:::::::::::::o//++//:::://ooo+/:::::--mMMMMMMMMM
        Mm+::::::::::o::::::::::o++:::::::--:::/o//:::///+sso++++++///::/dMMMMMMMMM
        MMNy/:::::/++:::::::::::o++/::::::-:::/yyyhhhddmNMMMy++++++++++++mMMMMMMMMM
        MMMMMmyo++/:::::::://+oyh++++/:::::::/dMMMMMMMMMMMMMMs++++++++++//sNMMMMMMM
        MMMMMMMMNmddhhhddmmNMMMMm++++++++++++hMMMMMMMMMMMMMMMNmhyso+++os++mNMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMd+++++++++++oMMMMMMMMMMMMMMMMMMMMMNmdysMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMM+/++++/++o+/oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMmNMMdooymMMmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    \n\n""")


# The following functions will slow draw the Pokémon
# to be battled in the training and boss functions

def print_pikachu():
    slow_draw("""\n
           oMMMMMMMMMMMMMmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMMmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMNMNhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMNdo--NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh+dMMo   
           oMMMMMMMMMm+----MMMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMNNmMMMMMMMMMNs-``-NMo   
           oMMMMMMMMM:..--/MMMMMMMMMMMMMMMMMMMNdhs+:-hMMMNNmmNMMMMMMMmo-`````sMo   
           oMMMMMMMMN.....sMMMMMMMMMMMMMMMNds/:-----+NMNNNNNMMMMMMMd+-.......:Mo   
           oMMMMMMMMm...-:hdhhhhddmNMMMmy+:--------+NMMNMMMMMMMMMd+--.......--do   
           oMMMMMMMMN-..-.-....----::+o:----------oNMMMMMMMMMMMd+-----.--....-oo   
           oMMMMMMMNh-......../-+y:------::::+oyhmMMMMMMMMMMMd+----------------o   
           oMMMMMMd+-........-dhdm+------:+mNNMMMMMMMMMMMMMmo:----------------:+   
           oMMMMMhdyo..-....--:oo/-::/:---:sMMMMMMMMMMMMMNs:---------------:+hmo   
           oMMMMm:ys:-:/:::/+....-+//+o/::-:yMMMMMMMMMMMh/--------------/ohNMMMo   
           oMMMMd+----:ssssss.---++++oo/:::::dMMMMMMMMMM+:::::------:/odNMMMMMMo   
           oMMMMm+o-...:ssysy----:ooooo:::::::mMMMMMMMMMN+::::::::/ohNMMMMMMMMMo   
           oMMMMMds+----:so+o--:::://::-::::::+NMMMMMMMMMN+::::/odNMMMMMMMMMMMMo   
           oMMMMMMNy/::::://:---::-----://:::--+NMMMMMMMMMNo//oNMMMMMMMMMMMMMMMo   
           oMMMMMMNmho/-::::-::::-----////:/----oNMMMMMMMMNy//+dMMMMMMMMMMMMMMMo   
           oMmmhs+::-------:---:::::-:+::/:/:-..-odMMMMMmyo++++yMMMMMMMMMMMMMMMo   
           os//---....-...------------/--/:::--...-sNMms++++ohmMMMMMMMMMMMMMMMMo   
           o+//-----....-.....---------:-----:--....+mMms++yNMMMMMMMMMMMMMMMMMMo   
           omdhysso+//::+-......-.......----------...+mMMdsohNMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMMN/....-..........-------------/hNmhssymMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMMMd.....---...---..-------------/ysyhmNMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMMMM:.....-----------.----------://ydNMMMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMMMM+.......-----------......---///hdmMMMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMMMMy..--.....----------------:////mMMMMMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMMMMN:---------:::::::::::::://////MMMMMMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMMMMMmo:::::////+osyso+///////////hMMMMMMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMMMMMMMmhso++oymMMMMMMMNdhysss+++oMMMMMMMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMMMMMMMMMMMs+omMMMMMMMMMMMMMMMho+omMMMMMMMMMMMMMMMMMMMMMMo   
           oMMMMMMMMMMMMMMMMMMMMMNyoNMMMMMMMMMMMMMMMMho+mMMMMMMMMMMMMMMMMMMMMMMo
        \n\n""")


def print_eevee():
    slow_draw("""\n
        MMMMMMMMhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMs+sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMmyNyoNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMhdddyodMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMyddhdh+hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMhhhdhhh+hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMmyhhhhhh+mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMsdhhhhhyoMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMhymdhhdmohMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmddhyyNMMMMMMMMMMMM
        MMMMMMMMMyhNmdmMhoMMmMm+dNMh/mMMMMMMMMMMMMMMMNmdhyyyysyhhdhohNMMMMMMMMMMMMM
        MMMMMMMMMMyyNNNMN+Nmo+s//++o:/hdyMNMMMMMMNdysyhhhhhhdddddyymMMMMMMMMMMMMMMM
        MMMMMMMMMMMdsmMMN+yo/////////////ooNMMMmyshmNNmdhhhhhhhyydMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMNyhho++//////////////+++dmyymNMMNmdhhhhhhssdNMMMMMMMmydMMMMMMMM
        MMMMMMMMMMMMMMmy++++///////////+++++oshNMMMMNNNmmdhsydNMMMMMMMNy:-:MMMMMMMM
        MMMMMMMMMMMMMMN++++o++++++++++++++++++yNNNmmmdhyyyhNMMMMMMMNds:----hMMMMMMM
        MMMMMMMMMMMMMMh++y/dso++++++++++++++++oyhhhhhdmmNMMMNNmdyo/:-------sMMMMMMM
        MMMMMMMMMMMMMMs+yMhMy++++++++++ooys+++omMMMMMMMNmhysso+///:::/:----oMMMMMMM
        MMMMMMMMMMMMMMo+dNMNs+++++++++sN+hm+++sMMMMMNdysoooooooooooooo/----yMMMMMMM
        MMMMMMMMMMMMMN++shdh++++++++++NMMNN++omMMMMmyooooooooooooooooo/----hMMMMMMM
        MMMMMMMMMMNh+y+++oo++++++++++ommNdh+oyMMMMNsoooooooooooooooooo:-:-:NMMMMMMM
        MMMMMMMMNs-../oo+++++++oo+++++syhyooosshNMhsoooooooooooooooooo/oo/sMMMMMMMM
        MMMMMMMMy.``..-/oo++++++o+oo++++++ooo:--/hyysooooooooooooooooossssNMMMMMMMM
        MMMMMMMN.``.....:/++oo++++++++ooooo+::::-:oyyssssoooooooooossssyydMMMMMMMMM
        MMMMMMMy-```........:/++oooooo++o/::::::::oyyyyyysssssssssssyyyydMMMMMMMMMM
        MMMMMMMdo-...-.``.-....--::::::::/::::::::+osyyyyyyyyssyyyyyyyydMMMMMMMMMMM
        MMMMMMMMms-..:```...........-:/:::/::::::sssooyyyyyyyyyyyyyyydNMMMMMMMMMMMM
        MMMMMMMMMMd+::`.-.````````...::+::o:::::ooooooohyyyyyyyyyyhdNMMMMMMMMMMMMMM
        MMMMMMMMMMMMmy--::.....`````.::+:/+:::/oooooooohmdddddmmNNMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMh/-+---..-....-:+//o/++ooooooooooyMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMNs/+:::::---::/++sssoooooooooooohMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMmoss+:--::/ooooooyoosymo++++ooodMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMyoooo++yooosoooohyhydMm+++++++mMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMNoooossso+oooooyhyyymMMy++++++MMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMy+++++s++++++ohyyhmMMMo+++++dMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMd+++++s++++++syyhNMMNs+++++hMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMNo////o+//+++smdmMMMMoo++++yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMNhoo/+o/////oNMMMMMMMNmhdhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMNMNhsssymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        \n\n""")


def print_dragonite():
    slow_draw("""\n      
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMoMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdomMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMyyMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNysyyyhyyyyyyyhNMMNy/sMMMMMMMMMMMMMMMMMysMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNMMMMMMd+o+////ohNMMMMMMMMMMMMMMM/MMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms++++:::::::sNhyyyyyhdmNMmsyMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy+////:::::::::/mMMMMMMNdhhdNMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh////+:::::::::::dMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMNho//NMMMMMMMMMMMMMMM+///oN--::::::::/hMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMdo+//+:yMMMMMMMMMMMMMMd////hmy-::::::::mNMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMh+/+///so/NMMMMMMMMMMMMMo/////+/:::::::::hMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMmo+/////ooo+oMMMMMMMMMMMMm///+++/:::::::::::mMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMy/+//////o+oo+sMMMMMMMMMMMo///+oo//::::::::::dMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMs+o//////++/+oo+oNMMMMMMMMy/////ooo+/::::::::+odMMMMMMMMMMMMMMM
        MMMMMMMMMMMo+oo//////+////ooo+hNMMMMMd::://++//+++//+/+++oo+hMMMMMmMmdodMMM
        MMMMMMMMMMy+ooo//////o/////+oooohNMMm/:::::/+:://///o//+//+o+mMMMd:o//:ohhN
        MMMMMMMMMm/sooo+/////o///////+oooosh/:::::::/.------:+/o////ssmy+:::::::/hM
        MMMMMMMMMsooosys+////+////////+oooo:::::::::+--......////////:::::::::::+MM
        MMMMMMMMM+sydNMMNmho//+//+syyyhys+::::::::::+.........-/:::::::::::::::+mMM
        MMMMMMMMM+dMMMMMMMMMmyyymNMMMMMNo:::::::::::/:..-------:/::::::::::::/sNMMM
        MMMMMMMMMsmMMMMMMMMMMMMMMMMMMMd/::::::::/::::/.........../+//::://+ohNMMMMM
        MMMMMMMMMNdMMMMMMMMMMMMMMMMMNy/::::::::/o::::/...........-ommmmmmNNMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMmo:::::::::/o:::::+--...........+NMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMh+:::::::::++/:::::/............../NMMMMMMMMMMMMM
        ydMMMMMMMMMMMMMMMMMMMMMMMs/:::::::::++/::::::/.-------.....--/NMMMMMMMMMMMM
        o:sNMMMMMMMMMMMMMMMMMMMMm//::::::::++/:::::::/................+MMMMMMMMMMMM
        h::+hNMMMMMMMMMMMMMMMMMMN+/:::::::o///::::::/-.................hMMMMMMMMMMM
        N/:::+hNMMMMMMMMMMMMMMMMdss/::::/+////::::::+.-----------------+hNMMMMMMMMM
        Md:::::/ymMMMMMMMMMMMMMMMMN-/++:+::::/::::::/..................-/+mMMMMMMMM
        MMy:::::::+ymNMMMMMMMMMMMMMmo///:::::::::::/...................-/:/mMMMMMMM
        MMMy:::::::::/oyhmNNNNNNNNmo///:::::::::///:---...........-----/:::+MMMMMMM
        MMMMd+::::::::::::://++++o+///:::::::::::+-..................../::::dMMMMMM
        MMMMMNs+::::::::::::::::/+////::::::::::::/..................-/:::::yMMMMMM
        MMMMMMNdo+/::::::::::::/o/////::::::::::::+-.--------------..-/:::::yMMMMMM
        MMMMMMMMNyo++//::::::::+o/////::::::::::::/................-//:::::/NMMMMMM
        MMMMMMMMMMNyo+o+++/////+o/////:::::::::::::-----......----:/::::::/mMMMMMMM
        MMMMMMMMMMMMMdy/o/o++++/o/////::::::::::/+---...--------:++/////+yNMMMMMMMM
        MMMMMMMMMMMMMMMNmss//o/+oo/////:::::::///////:::::://+o++///++ohNMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMmhso//oo////::::://///::://///+oo++/////+ymMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMNdhd+///:::+//+////++oyhdmNMmo+///////+ooshdNMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMN+//::::ymmmmNNNMMMMMMMMMMMho+//::::::::::oymMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMNo//:::::+MMMMMMMMMMMMMMMMMMMMho+/::::::/:---:yMMM
        MMMMMMMMMMMMMMMMMMMMMMMMm+/::::::::hMMMMMMMMMMMMMMMMMMMMMmhyo+++/--:oosmMMM
        MMMMMMMMMMMMMMMMMMMMMMMm+/:::::::::/MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMM+/:::/::://::NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMM-.//-.-//`.+dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMM.-y+``-y:-sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMdMMd/hMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        \n\n""")


# This section will output an intro .wav file
# display an introduction message and ASCII art

winsound.PlaySound("intro", winsound.SND_FILENAME | winsound.SND_ASYNC)

intro = """\n\t\tHello, welcome to the world of Pokémon! ...err, I mean Python. In this
        world, Pokémon are made of ASCII art. That's right, they look even uglier than
        the originals, but they can still be fun. Choose one and see! \n\n"""

slow_prompt(intro)

slow_prompt("BULBASAUR")
print_bulbasaur()

slow_prompt("CHARMANDER")
print_charmander()

slow_prompt("SQUIRTLE")
print_squirtle()

# The selection interface will prompt the user to
# make a valid choice and will continue looping
# until the a valid selection is made

slow_prompt("1- Bulbasaur, 2- Charmander, 3- Squirtle\n")
pokemon_choice = input("Choose a starter Pokémon :")

valid_pokemon_choice = False
while not valid_pokemon_choice:

    if pokemon_choice == "1":
        slow_prompt("\nYou have selected Bulbasaur")
        valid_pokemon_choice = True
    elif pokemon_choice == "2":
        slow_prompt("\nYou have selected Charmander")
        valid_pokemon_choice = True
    elif pokemon_choice == "3":
        slow_prompt("\nYou have selected Squirtle")
        valid_pokemon_choice = True
    else:
        pokemon_choice = input("Please select a Pokémon using keys 1, 2, or 3: ")

# This section will assess if the Pokémon is ready to
# face a boss or if the Pokémon needs to train more

# The following list will pertain to the skill level
# values established by the scenario constraints

# None value was added in order to link stats to direct
# damage and ease the reading of Pokémon stats.

skill_level = ["None", "Beginner", "Apprentice", "Associate", "Skilled", "Professional",
               "Artisan", "Master", "God"]


# The Pokémon class will hold common attributes shared
# by all Pokémon. These attribute are established by the
# scenario specifications. Also it will be able to print out
# it stats relevant to the scenario specifications.

class Pokemon:
    def __init__(self, arg_name, arg_type, arg_hp, arg_melee, arg_ranged, arg_block,
                 arg_agility, arg_healing, arg_movelist):
        self.name = arg_name
        self.type = arg_type
        self.hp = arg_hp
        self.melee = arg_melee
        self.ranged = arg_ranged
        self.block = arg_block
        self.agility = arg_agility
        self.healing = arg_healing
        self.move_list = arg_movelist

    def view_stats(self):
        slow_prompt("\nName:    " + self.name)
        slow_prompt("\nType:    " + self.type)
        slow_prompt("\nHP       " + str(self.hp))
        slow_prompt("\nMelee:   " + skill_level[self.melee])
        slow_prompt("\nRanged:  " + skill_level[self.ranged])
        slow_prompt("\nBlock:   " + skill_level[self.block])
        slow_prompt("\nAgility: " + skill_level[self.agility])
        slow_prompt("\nHealing: " + skill_level[self.healing])
        print("\n")


if pokemon_choice == "1":
    my_pokemon = Pokemon("Bulbasaur", "Grass", 18, 7, 3, 3, 3, 3, ["Tackle", "Vine Whip", "Leech Seed"])
elif pokemon_choice == "2":
    my_pokemon = Pokemon("Charmander", "Fire", 16, 3, 7, 3, 3, 3, ["Scratch", "Ember", "Smokescreen"])
elif pokemon_choice == "3":
    my_pokemon = Pokemon("Squirtle", "Water", 20, 3, 3, 7, 3, 3, ["Bite", "Water Gun", "Withdraw"])

my_pokemon.view_stats()


# The following code will determine is the Pokémon is fit
# to battle a boss or if it needs more training.

# Fun fact:
# This is supposed to be the main part of the code. XD

# This function is written in the order of constraints
# established by the scenario. It is interpreted in the
# form of a Pokémon needing an agility of 4(Skilled) and
# either a ranged attack of 3(Associate) or melee attack
# of 4(Skilled). If these statistics do not return True
# then it will require the Pokemon to have an agility of
# 4(Skilled) and either block or healing with a rating of
# 3(Associate)

def assess_pokemon():
    if (my_pokemon.agility >= 4) and ((my_pokemon.ranged >= 3) or (my_pokemon.ranged >= 4)):
        slow_prompt("Pokemon is ready to battle boss.")
        return True
    elif (my_pokemon.agility >= 4) and ((my_pokemon.block >= 3) or (my_pokemon.healing >= 3)):
        slow_prompt("Pokemon is ready to battle boss.")
        return True
    else:
        slow_prompt("Pokemon is not ready to battle boss.\n")
        return False


battle_ready = assess_pokemon()


# In this section, code will be defined for each
# Pokémon's unique moves.

def tackle(opponent):
    slow_prompt(my_pokemon.name + " does a hefty tackle!\n")
    opponent.hp -= (my_pokemon.melee - opponent.block)
    return opponent


def scratch(opponent):
    slow_prompt(my_pokemon.name + " scratches the opponent!\n")
    opponent.hp -= (my_pokemon.melee - opponent.block)
    return opponent


def bite(opponent):
    slow_prompt(my_pokemon.name + " bites into the other Pokémon!\n")
    opponent.hp -= (my_pokemon.melee - opponent.block)
    return opponent


def vinewhip(opponent):
    slow_prompt(my_pokemon.name + " vine WHIPS the opposition!\n")
    if opponent.type == "Rock":
        opponent.hp -= 8
    else:
        opponent.hp -= (my_pokemon.ranged - opponent.block)
    return opponent


def ember(opponent):
    slow_prompt(my_pokemon.name + " sets " + opponent.name + " on FIRE!\n")
    if opponent.type == "Grass":
        opponent.hp -= 8
    else:
        opponent.hp -= (my_pokemon.ranged - opponent.block)
    return opponent


def watergun(opponent):
    slow_prompt(my_pokemon.name + " BLASTS " + opponent.name  + "!\n")
    if opponent.type == "Fire":
        opponent.hp -= 8
    else:
        opponent.hp -= (my_pokemon.ranged - opponent.block)
    return opponent


def leech(opponent):
    slow_prompt(my_pokemon.name + " leeches life from " + opponent.name + "!\n")
    my_pokemon.hp += my_pokemon.healing
    opponent.hp -= 2
    return opponent


def smokescreen(opponent):
    slow_prompt(my_pokemon.name + " hides in a cloud of smokescreen!\n")
    opponent.agility -= my_pokemon.ranged
    opponent.hp -= 0
    return opponent


def withdraw(opponent):
    slow_prompt(my_pokemon.name + " withdraws into its shell!\n")
    my_pokemon.block += 4
    opponent.hp -= 0
    return opponent

# my_move function can be call to utilize one
# of the many moves performed by the starting
# Pokemon. They in turn call functions that
# determine the effects of the moves


def my_move(opponent):
    slow_prompt("Choose your move: \n")
    n = 1
    for i in my_pokemon.move_list:
        slow_prompt(str(n) + "- ")
        slow_prompt(i)
        slow_prompt("\n")
        n += 1

    valid_move_choice = False
    move_choice = input()

    while not valid_move_choice:
        if move_choice == "1":
            if my_pokemon.move_list[0] == "Tackle":
                opponent = tackle(opponent)
                valid_move_choice = True
            elif my_pokemon.move_list[0] == "Scratch":
                opponent= scratch(opponent)
                valid_move_choice = True
            elif my_pokemon.move_list[0] == "Bite":
                opponent = bite(opponent)
                valid_move_choice = True
        elif move_choice == "2":
            if my_pokemon.move_list[1] == "Vine Whip":
                opponent = vinewhip(opponent)
                valid_move_choice = True
            elif my_pokemon.move_list[1] == "Ember":
                opponent = ember(opponent)
                valid_move_choice = True
            elif my_pokemon.move_list[1] == "Water Gun":
                opponent = watergun(opponent)
                valid_move_choice = True
        elif move_choice == "3":
            if my_pokemon.move_list[2] == "Leech Seed":
                opponent = leech(opponent)
                valid_move_choice = True
            elif my_pokemon.move_list[2] == "Smokescreen":
                opponent = smokescreen(opponent)
                valid_move_choice = True
            elif my_pokemon.move_list[2] == "Withdraw":
                opponent = withdraw(opponent)
                valid_move_choice = True
        else:
            move_choice = input("Please select a choice using keys 1, 2, or 3: ")
    return opponent


# The battle function will call a battle against
# a specific enemy. It could be improved by passing
# the draw function through a class property but
# as I understand this will require me to use static
# classes so I will avoid them for the sake of simplicity
# This means that a battle function can be receive
# objects of Pokémon type to reduce code redundancy

def battle_pikachu():
    winsound.PlaySound("battle", winsound.SND_FILENAME | winsound.SND_ASYNC)
    print_pikachu()
    pikachu = Pokemon("Pikachu", "Electric", 12, 3, 6, 2, 6, 1, ["Tackle", "Thunder", "Iron Tail"])

    while pikachu.hp > 0 and my_pokemon.hp > 0:
        if pikachu.agility > my_pokemon.agility:
            attack = random.choice(pikachu.move_list)
            if attack == "Tackle":
                slow_prompt("Pikachu does Tackle!\n")
                my_pokemon.hp -= my_pokemon.block - 2
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                pikachu.hp = my_move(pikachu).hp
                slow_prompt("Pikachu's HP falls to " + str(pikachu.hp) + "\n")
                if pikachu.hp <= 0:
                    break
            elif attack == "Thunder":
                slow_prompt("Pikachu uses Thunder!\n")
                my_pokemon.hp -= my_pokemon.block - 7
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                pikachu.hp = my_move(pikachu).hp
                slow_prompt("Pikachu's HP falls to " + str(pikachu.hp) + "\n")
                if pikachu.hp <= 0:
                    break
            else:
                slow_prompt("Pikachu uses Iron Tail!\n")
                my_pokemon.hp -= my_pokemon.block + pikachu.ranged
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                pikachu.hp = my_move(pikachu).hp
                slow_prompt("Pikachu's HP falls to " + str(pikachu.hp) + "\n")
                if pikachu.hp <= 0:
                    break
        else:
            pikachu.hp = my_move(pikachu).hp
            slow_prompt("Pikachu's HP falls to " + str(pikachu.hp) + "\n")
            attack = random.choice(pikachu.move_list)
            if attack == "Tackle":
                slow_prompt("Pikachu does Tackle!\n")
                my_pokemon.hp -= my_pokemon.block - 23

                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                pikachu.hp = my_move(pikachu).hp
                slow_prompt("Pikachu's HP falls to " + str(pikachu.hp) + "\n")
                if pikachu.hp <= 0:
                    break
            elif attack == "Thunder":
                slow_prompt("Pikachu uses Thunder!\n")
                my_pokemon.hp -= my_pokemon.block - 7
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                pikachu.hp = my_move(pikachu).hp
                slow_prompt("Pikachu's HP falls to " + str(pikachu.hp) + "\n")
                if pikachu.hp <= 0:
                    break
            else:
                slow_prompt("Pikachu uses Iron Tail!\n")
                my_pokemon.hp -= 2
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                pikachu.hp = my_move(pikachu).hp
                slow_prompt("Pikachu's HP falls to " + str(pikachu.hp) + "\n")
                if pikachu.hp <= 0:
                    break

    if (my_pokemon.hp <= 0):
        winsound.PlaySound("flute", winsound.SND_FILENAME | winsound.SND_ASYNC)
        slow_prompt("Game Over \n")
    elif (pikachu.hp <= 0):
        winsound.PlaySound("victory", winsound.SND_FILENAME | winsound.SND_ASYNC)
        slow_prompt(my_pokemon.name + " levels up!\n\n")

    proceed = input("Press any key to continue")

def battle_eevee():
    winsound.PlaySound("battle", winsound.SND_FILENAME | winsound.SND_ASYNC)
    print_eevee()
    eevee = Pokemon("Eevee", "Normal", 15, 3, 2, 3, 7, 1, ["Tackle", "Quick Attack", "Swift"])

    while eevee.hp > 0 and my_pokemon.hp > 0:
        if eevee.agility > my_pokemon.agility:
            attack = random.choice(eevee.move_list)
            if attack == "Tackle":
                slow_prompt("Eevee does Tackle!\n")
                my_pokemon.hp -= 3
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                eevee.hp = my_move(eevee).hp
                slow_prompt("Eevee's HP falls to " + str(eevee.hp) + "\n")
                if eevee.hp <= 0:
                    break
            elif attack == "Quick Attack":
                slow_prompt("Eevee quickly attacks!\n")
                my_pokemon.hp -= 1
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
            else:
                slow_prompt("Eevee uses Swift!\n")
                my_pokemon.hp -= 5
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                eevee.hp = my_move(eevee).hp
                slow_prompt("Eevee's HP falls to " + str(eevee.hp) + "\n")
                if eevee.hp <= 0:
                    break
        else:
            eevee.hp = my_move(eevee).hp
            slow_prompt("Eevee's HP falls to " + str(eevee.hp) + "\n")
            attack = random.choice(eevee.move_list)
            if attack == "Tackle":
                slow_prompt("Eevee does Tackle!\n")
                my_pokemon.hp -= 3
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                eevee.hp = my_move(eevee).hp
                slow_prompt("Eevee's HP falls to " + str(eevee.hp) + "\n")
                if eevee.hp <= 0:
                    break
            elif attack == "Quick Attack":
                slow_prompt("Eevee quickly attacks!\n")
                my_pokemon.hp -= 1
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
            else:
                slow_prompt("Eevee uses Swift!\n")
                my_pokemon.hp -= 5
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                eevee.hp = my_move(eevee).hp
                slow_prompt("Eevee's HP falls to " + str(eevee.hp) + "\n")
                if eevee.hp <= 0:
                    break

    if (my_pokemon.hp <= 0):
        winsound.PlaySound("flute", winsound.SND_FILENAME | winsound.SND_ASYNC)
        slow_prompt("Game Over \n")
    elif (eevee.hp <= 0):
        winsound.PlaySound("victory", winsound.SND_FILENAME | winsound.SND_ASYNC)
        slow_prompt(my_pokemon.name + " levels up!\n\n")

    proceed = input("Press any key to continue")


def battle_dragonite():
    winsound.PlaySound("battle", winsound.SND_FILENAME | winsound.SND_ASYNC)
    print_dragonite()
    dragonite = Pokemon("Dragonite", "Dragon", 30, 7, 7, 7, 7, 7, ["Wing Attack", "Slam", "Hyper Beam"])

    while dragonite.hp > 0 and my_pokemon.hp > 0:
        if dragonite.agility > my_pokemon.agility:
            attack = random.choice(dragonite.move_list)
            if attack == "Wing Attack":
                slow_prompt("Dragonite uses Wing Attack!\n")
                my_pokemon.hp -= my_pokemon.block - dragonite.ranged
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                dragonite.hp = my_move(dragonite).hp
                slow_prompt("Dragonite's HP falls to " + str(dragonite.hp) + "\n")
                if dragonite.hp <= 0:
                    break
            elif attack == "Slam":
                slow_prompt("Dragonite slams " + my_pokemon.name + "!\n")
                my_pokemon.hp -= my_pokemon.block - dragonite.melee
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                dragonite.hp = my_move(dragonite).hp
                slow_prompt("Dragonite's HP falls to " + str(dragonite.hp) + "\n")
                if dragonite.hp <= 0:
                    break
            else:
                slow_prompt("Dragonite uses HYPER BEAM!\n")
                my_pokemon.hp -= my_pokemon.block + dragonite.ranged
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                dragonite.hp = my_move(dragonite).hp
                slow_prompt("Dragonite's HP falls to " + str(dragonite.hp) + "\n")
                if dragonite.hp <= 0:
                    break
        else:
            dragonite.hp = my_move(dragonite).hp
            slow_prompt("Dragonite's HP falls to " + str(dragonite.hp) + "\n")
            attack = random.choice(dragonite.move_list)
            if attack == "Wing Attack":
                slow_prompt("Dragonite uses Wing Attack!\n")
                my_pokemon.hp -= my_pokemon.block - dragonite.ranged
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                dragonite.hp = my_move(dragonite).hp
                slow_prompt("Dragonite's HP falls to " + str(dragonite.hp) + "\n")
                if dragonite.hp <= 0:
                    break
            elif attack == "Slam":
                slow_prompt("Dragonite slams " + my_pokemon.name + "!\n")
                my_pokemon.hp -= my_pokemon.block - dragonite.melee
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                dragonite.hp = my_move(dragonite).hp
                slow_prompt("Dragonite's HP falls to " + str(dragonite.hp) + "\n")
                if dragonite.hp <= 0:
                    break
            else:
                slow_prompt("Dragonite uses HYPER BEAM!\n")
                my_pokemon.hp -= my_pokemon.block + dragonite.ranged
                slow_prompt(my_pokemon.name + "'s HP falls to " + str(my_pokemon.hp) + "\n")
                if my_pokemon.hp <= 0:
                    break
                dragonite.hp = my_move(dragonite).hp
                slow_prompt("Dragonite's HP falls to " + str(dragonite.hp) + "\n")
                if dragonite.hp <= 0:
                    break

    if (my_pokemon.hp <= 0):
        winsound.PlaySound("flute", winsound.SND_FILENAME | winsound.SND_ASYNC)
        slow_prompt("Game Over \n")
    elif (dragonite.hp <= 0):
        winsound.PlaySound("victory", winsound.SND_FILENAME | winsound.SND_ASYNC)
        slow_prompt(my_pokemon.name + " levels up!\n\n")

    my_pokemon.view_stats()
    proceed = input("Press any key to continue")

# This section will prompt the user to choose between
# training or battling the boss should it meet the
# requirements to do so

def choose_battle(battle_ready):
    slow_prompt("\nWhat would you like to do? \n")
    battle_choice = input("1- Boss 2- Train : ")

    valid_battle_choice = False
    while not valid_battle_choice:

        if battle_choice == "1":
            if battle_ready:
                print("Let's take down this boss!")
                battle_dragonite()
                valid_battle_choice = True
            else:
                print("Pokémon is not ready to battle, but can train!")
                battle_choice = input("1- Boss 2- Train : ")
        elif battle_choice == "2":
            print("Let's train!")
            slow_prompt("\nWhich pokémon would you like to battle:")

            opponent_choice = input("\n1- Pikachu 2- Eevee: ")
            valid_opponent_choice = False

            while not valid_opponent_choice:
                if opponent_choice == "1":
                    battle_pikachu()
                    valid_opponent_choice = True
                elif opponent_choice == "2":
                    battle_eevee()
                    valid_opponent_choice = True
                else:
                    opponent_choice = input("Please select a choice using keys 1 or 2: ")

            valid_battle_choice = True
        else:
            battle_choice = input("Please select a choice using keys 1 or 2: ")

    my_pokemon.hp += 10
    my_pokemon.melee += 1
    my_pokemon.ranged += 1
    my_pokemon.block += 1
    my_pokemon.agility += 1
    my_pokemon.healing += 1

    winsound.PlaySound("route24", winsound.SND_FILENAME | winsound.SND_ASYNC)

    my_pokemon.view_stats()
    battle_ready = assess_pokemon()
    choose_battle(battle_ready)

choose_battle(battle_ready)
input("Press any key to EXIT")
