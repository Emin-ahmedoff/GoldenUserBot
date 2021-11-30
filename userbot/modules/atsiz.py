# Copyright (C) 2020 Yusuf Usta.
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# Golden userbot


from random import choice
from userbot import CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ================= CONSTANT =================
ATSIZ = ['Dostluğu düşmənçiliyə çevirmək asan, düşmənçiliyi dostluğa çevirmək çətindir.', 'Düşmənə bəslədiyin kini körükləmə, yoxsa özün də yanarsan.', 'Bəzən insan; ”Mən yaxşıyam” deyəndə gözlərinin içine baxıb ”yaxşı deyilsən bilirəm” deyəcək birine çox ehtiyac duyar”.', 'Hansı içki sevdiyinin qoxusu qədər sərxoş edə bilər ki.', 'Gəncliyin və sağlamlığın dəyəri itiriləndən sonra bilinər. [ Həzrəti Əli əleyhissalam ]', 'Qəzəbə sevgi ilə, pisliyə yaxşılıqla, haqsızlıqlığa əfv etməklə, yalana doğru ilə cavab ver.', 'Gülmək hər vaxt xoşbəxt olmaq üçün deyil. Bəzən elə gülmələr vardır ki; ən böyük ağrıları gizləmək üçündür.', 'Yalnız uşaqkən gülər insan, digərləri gülmək deyil. Çünki insan böyüdükcə komik şeylərə deyil, ağrılara gülməni öyrənər.', 'İki şey insanı gözdən salar: 1-Demaqoqluq 2-Özünü öymək', '“Unutdum” Demək Belə Xatırlamaqdır, Əslində…', 'Bəzən Ona Nələrsə Yazarsan Silərsən…Yenə Yazarsan Silərsən.O Heç Birini Oxumaz Əlbəttə Ki… Amma Sən Sanki Hər Şeyi Demiş Olarsan…', 'İnsanlar Nə Qədər Ağıllı Olursa Olsun…Sevdiyi Adamın Bir Sözünə Aldanacaq Qədər Axmaqdır Əslində.', 'Dəyər verdiyin insan sənə dəyər vermirsə, burax öz dəyəriylə qalsın.', 'Başını Köksümə Qoyduğunda Tək Bir Düşmənim Var… O da Keçib Gedən Zaman…', 'Qadınlarda riyaziyyata qarşı sevgi var. Onlar yaşlarını ikiyə bölür,paltarlarının qiymətini ikiyə vurur,sevmədikləri rəfiqələrinin yaşını 5 yaş artırırlar.', 'Kim keçmiş səadəti haqqında düşünmürsə,o artıq qocadır.', 'Dünyada ən aşkar və aydın dəlil onların özlərinin varlığıdır.', 'Xoşbəxt var-dövləti olan deyil,dövlətə ehtiyacı olmayandır.', 'Həyat qəribə mən qəribə.Həyat bir dərs mən dərsdən qaçan tələbə…', 'Səsini belə xatırlamıram, amma söylədikləri hələ də ağılımda.', 'Kişi və qadın arasında heç bir zaman dostluq ola bilməz…Onların arasında yalnız sevgi,düşmənçilik,ehtiras və məftunluq ola bilər… Oskar Uayld', 'Güvən itdiyi yerdə, dostluq da itir…', 'Dostluq var – məqsədi xeyir üçün,dostluq var – məqsədi xoş vaxt keçirtmək üçün…', 'İnsanı Ən Çox Üzən Şey… Gözləmədiyi Kəslər Adam Olarkən… Adam Sandıqlarının İnsan Belə Olamamış Olmasıdır…', 'Sevəni Axtarırsansa Evinə Get… Qapını Anan Açacakdır…', 'Arxamdan Danışmağa Davam Et… “Çünki qarşıma çıxacaq qədər böyük deyilsən”…', 'Eşq üçün tökülən göz yaşı ilə savaşda axan qanı heç bir şey əvəz edə bilməz..', 'ALLAH qorxusu ilə ağlayan gözə Cəhənnəm atəşinin toxunması haramdır.ALLAH qorxusu ilə gözündən yaş axana Qiyamətdə əzab olmaz..(Həzrəti Muhəmməd s.a.v)', 'Sevgi gözlərini kor edibsə, çalışma bir də o gözləri açmağa.', '“Bəziləri arxanızdan danışırsa, onlardan öndəsiz deməkdir.”', 'O qədər də əhəmiyyətli deyil buraxıb getmələr, Arxalarında doldurulması Mümkün olmayan boşluqlar buraxılmasaydı əgər.', '“Qabına yeyə biləcəyin qədər yemək, həyatına sevə biləcəyin qədər insan al .. Israf lazım deyil.”', 'Ərzə hacət yox halım sənə əyandır.Dilə ehtiyac yoxdur səssizliyim sənə bəyandır.Sözə lüzum yoxdur susuşum sənə kəlamdır.[Mövlana]', 'Ölümlə əbədi mübarizədəyik. Qalibin O olacağını əvvəlcədən bilə-bilə.', '“Bəzən insanları ağrılarındakı bənzərlik qədər bir-birinə bağlayan heç bir şey yoxdur…”', '“Təcrübə insanın başına gələnlər deyil, başına gəldiyində nə etdiyidir…”', 'Ağlamaqdan qorxma!Zehnindəki iztirab verən düşüncələr göz yaşı ilə təmizlənər…!', 'Torpaq bir gün yağışın qiymətini anlayacaq.Fəqət həmin gün artıq yağış yağmayacaq”', '“Əvvəlcə onlar səni görmürlər, sonra sənə gülürlər, sonra səninlə mübarizə aparırlar və sonda sən qalib gəlirsən.”', '“İstəyimizi birdən-birə reallaşdıra bilməyəcəyimizi bilirik və bu vecimizə də deyil.”', '“Heç vaxt eşq əzabı çəkən birinə aşiq olmayın. O insan yaralıdır və yara sarğısı olaraq sizdən istifadə edəcək.”', '“Hər kəs öz keçmişini qəlbi ilə bildiyi bir kitabın səhifələri kimi bağlı saxlayar. Və dostları, sadəcə onun ön sözünü oxuya bilər”', '“Başqa planetlərdə də həyat varmı deyə maraq edirik, sanki bu planetdə yaşamağı bacarıq bilmişik kimi”', '“Qəribə deyilmi? Üzünə güləcək qədər dost sandığın kəslər, əslində arxandan danışacaq qədər üzsüzlər”', '“Problem sənin mənə yalan danışmağında deyil , problem sahib olduğun o ağlınla məni aldada biləcəyinə inanmağındır…']
ATSIZ_SIIR = [
    """
Dilek yolunda ölmek Türklere olmaz tasa,
Türk'e boyun eğdirir yalnız türeyle yasa;
Yedi ordu birleşip kaşımızda parlasa
Onu kanla söndürür parçalarız, yeneriz.

Biz Turfanı yarattık uyku uyurken Batı
Nuh doğmadan kişnedi ordularımızın atı.
Sorsan şöyle diyecek gök denilen şu çatı:
Türk gücü bir yıldırım, Türk bilgisi bir deniz.

Delinse yer, çökse gök,yansa, kül olsa dört yan,
Yüce dileğe doğru yine yürürüz yayan.
Yıldırımdan, tipiden, kasırgadan yılmayan,
Ölümlerle eğlenen tunç yürekli Türkleriz...
    """,
    """
Pınar başına geldi
Bir elinde güğümü;
Çattı yay kaşlarını
Görünce güldüğümü,
Bağlamıştı gönlümü
Saçlarını düğümü.
Bilmiyordum bu örgü
Acaba bir büğümü?

Sordum: nerdedir yerin?
Nedir senin değerin?
Yedi kral vurulmuş,
Ne bu ceylan gözlerin? Hangisine varırsın
Bu yedi ünlü erin?
Şöyle dedi bakarak
Göklere derin derin:

Kıralların taçları
Beni bağlar büğü mü?
Orduları açamaz
Gönlümdeki düğümü.
saraylarda süremem
Dağlarda sürdüğümü.
Bin cihana değişmem
Şu öksüz Türklüğümü...
""",
"""
Türk duygusu her Türkçüye en tatlı kımızdır;
Türk ülküsü candan da aziz bayrağımızdır.

Bayrak ki onun gölgesi Bozkurtları toplar;
Bayrak ki bütün kaybedilen yurtları toplar.

Nerden geliyor? Tanrıkut'un ordularından!
Lakin bize bir beyt okuyor kutlu yarından:

Darbeyle gönüllerde yatan ülkü silinmez!
Atsız yere düşmekle bu bayrak yere inmez!...
""",
"""
Ey vatan!
Güzel turan!
Sana feda biz varız.
Düşman oğlu meydana çık!
Kahramanlık kimde ise anlarız.
""",
"""
Ey sen ki kül ettin beni onmaz yakışınla, 
Ey sen ki gönüller tutuşur her bakışınla! 
Hançer gibi keskin ve çiçekler gibi ince 
Çehren bana uğrunda ölüm hazzı verince 
Gönlümdeki azgın devi rüzgarlara attım; 
Gözlerle günah işlemenin zevkini tattım. 
Gözler ki birer parçasıdır sende İlahın, 
Gözler ki senin en katı zulmün ve silahın, 
Vur şanlı silahınla gönül mülkü düzelsin; 
Sen öldürüyorken de vururken de güzelsin!""",
"""
Bu gün yollanıyorken bir gurbete yeniden 
Belki bir kişi bile gelmeyecektir bize. 
Bir kemiğin ardında saatlerce yol giden 
itler bile gülecek kimsesizliğimize 

Gidiyorum: gönlümde acısı yanıkların... 
Ordularla yenilmez bir gayız var kanımda. 
Dün benimle birlikte gülen tanıdıkların 
Yalnız bir hatırası kaldı artık yanımda.
""",
"""
Dilek yolunda ölmek Türklere olmaz tasa,
Türk’e boyun eğdirir yalnız türeyle yasa;
Yedi ordu birleşip karşımızda parlasa
Onu kanla söndürüp parçalarız, yeneriz .

Biz Tufanı yarattık uyku uyurken batı,
Nuh doğmadan kişnedi ordularımızın atı.
Sorsan şöyle diyecek gök denilen şu çatı:
Türk gücü bir yıldırım Türk bilgisi bir deniz.

Delinse yer, çökse gök yansa kül olsa dört yan,
Yüce dileğe doğru yine yürürüz yayan.
Yıldırımdan tipiden kasırgadan yılmayan,
Ölümlerle eğlenen tunç yürekli Türkleriz…
""",
"""
Atandan kalmış olan kılıcı iyi bile,
Onu bütün gücünle vuracaksın çağında.
Savaş….. Bunun tadını ey Türk sen bulamazsın,
Ne sevgili yanında, ne baba ocağında.

Savaşmaktan kaçınır, kim varsa alnı kara;
Kan dökmeyi bilenler hükmeder topraklara…
Kazanmanın sırrını bilmiyorsan git, ara,
“Çanakkale” ufkunda, “Sakarya” toprağında.

Siyasette muhabbet… Hepsi yalan palavra…
Doğru sözü “Kül Tegin” kitabesinde ara…
Lenin’den bahsederse karşında bir maskara,
Bir tebessüm belirsin sadece dudağında.

Yatağında ölmeyi hatırından sök, çıkar!
Döşeğin kara toprak, yorganındır belki kar…
Sen gurbette kalırsan, ben ölürsem ne çıkar?
Ruhlarımız buluşur elbet Tanrıdağı’nda…
""",
"""
Mukadderat isterse seni yoldan çevirsin,
Sen hele bu yollarda yıpranarak aşın da,
Varsın bütün ömrünce bir an nasip olmasın,
Yorgunluğunu gidermek serin bir su başında.

Bir gülüşten ne çıkar, ne çıkar ağlamaktan?
Kullar kancıklık eder, bela bulursun Hak’tan.
Gün olur ki bir yudum su ararsın bataktan,
Gün olur ki bir tutam tuz bulunmaz aşında.

Bir çığ gibi yürürsün bir lahza durmaksızın,
Bir ilahi kaynaktan geliyor çünkü hızın.
Duygular ölmüştür… Tapınılan bir kızın,
Bir füsun bulamazsın gözlerinde, kaşında.

Iztırabı kanına katta göz kırpmadan iç!
Varsın gülsün ardından, ne çıkar, bir iki piç…
Bu varlık dünyasında yalnız senin hiç mi hiç
Bir şeyin olmayacak… Hatta mezar taşın da…
""",
"""
Yer bulmasın gönlünde ne ihtiras, ne haset.
Sen bütün varlığına yurdumuzun malısın.
Sen bir insan değilsin; ne kemiksin, ne de et;
Tunçtan bir heykel gibi ebedi kalmalısın.

Iztırap çek, inleme… Ses çıkarmadan aşın.
Bir damlacık aksa da, bir acizdir göz yaşın;
Yarı yolda ölse de en yürekten yoldaşın
Tek başına dileğe doğru at salmalısın.

Ezilmekten çekinme… Gerilmekten sakın!
İradenle olmalı bütün uzaklar yakın,
Dolu dizgin yaparken ülküne doğru akın,
Ateşe atılmalı, denize dalmalısın.

Ölümlerden sakınma, meyus olmaktan utan!
Bir kere düşün nedir seni dünyada tutan?
Mefkuresinden başka her varlığı unutan
Kahramanlar gibi sen, ebedi kalmalısın…
"""
]

@register(outgoing=True, pattern="^.atsız$")
async def atsiz(e):
    """ Atsız sözlüğü """
    await e.edit(f"`{choice(ATSIZ)}`")

@register(outgoing=True, pattern="^.atsız şiir")
async def atsizs(e):
    """ Atsız şiir sözlüğü """
    await e.edit(f"`{choice(ATSIZ_SIIR)}`")


CmdHelp('atsız').add_command(
    'atsız', None, 'Bir Atsız sözü.'
).add_command(
    'atsız şiir', None, 'Bir Atsız şiiri.'
).add()
