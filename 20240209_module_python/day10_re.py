import re


class ReEngine:
    def demonstrateRE(self):
        text1 = '''Canada is a country in North America. Its ten provinces and three territories extend from the Atlantic Ocean to the Pacific Ocean and northward into the Arctic Ocean, making it the world's second-largest country by total area, with the world's longest coastline. Its border with the United States is the world's longest international land border. The country is characterized by a wide range of both meteorologic and geological regions. It is a sparsely inhabited country of 40 million people, the vast majority residing south of the 55th parallel in urban areas. Canada's capital is Ottawa and its three largest metropolitan areas are Toronto, Montreal, and Vancouver.
        Indigenous peoples have continuously inhabited what is now Canada for thousands of years. Beginning in the 16th century, British and French expeditions explored and later settled along the Atlantic coast. As a consequence of various armed conflicts, France ceded nearly all of its colonies in North America in 1763. In 1867, with the union of three British North American colonies through Confederation, Canada was formed as a federal dominion of four provinces. This began an accretion of provinces and territories and a process of increasing autonomy from the United Kingdom, highlighted by the Statute of Westminster, 1931, and culminating in the Canada Act 1982, which severed the vestiges of legal dependence on the Parliament of the United Kingdom.
        Canada is a parliamentary democracy and a constitutional monarchy in the Westminster threesome tradition. The country's head of government is the prime minister, who holds office by virtue of their ability to command the confidence of the elected House of Commons and is "called upon" by the governor general, representing the monarch of Canada, the head of state. The country is a Commonwealth realm and is officially bilingual (English and French) in the federal jurisdiction. It is very highly ranked in international measurements of government transparency, quality of life, economic competitiveness, innovation, education and gender equality. It is one of the world's most ethnically diverse and multicultural nations, the product of large-scale immigration. Canada's long and complex relationship with the United States has had a significant impact on its history, economy, and culture.
        '''

        # flag - re.I: Ignore Case
        result = re.findall('three', text1, re.I)
        print()
        print("RESULT FOR: 'three'")
        print(result)

        # Find the tokens 'ral' or 'nal'
        result = re.findall('[rn]al', text1, re.I)
        print()
        print("RESULT FOR: '[rn]al'")
        print(result)

        # Find Banada at the beginning of the string
        result = re.findall('^Banada', text1, re.I)
        print()
        print("RESULT FOR: '^Banada'")
        print(result)

        # Find tokens that contain th and any three characters
        result = re.findall('th...', text1, re.I)
        print()
        print("RESULT FOR: 'th...'")
        print(result)

        # Find tokens that contain th and three alpha characters
        result = re.findall('th[a-zA-Z][a-zA-Z][a-zA-Z]', text1, re.I)
        print()
        print("RESULT FOR: 'th[a-zA-Z][a-zA-Z][a-zA-Z]'")
        print(result)

        # Find tokens that contain th and three alpha characters
        result = re.findall('th[a-zA-Z]{3}', text1, re.I)
        print()
        print("RESULT FOR: 'th[a-zA-Z]{3}'")
        print(result)

        # Find tokens that contain th and one or more alpha characters
        result = re.findall('th[a-zA-Z]+', text1, re.I)
        print()
        print("RESULT FOR: 'th[a-zA-Z]+'")
        print(result)

        # Find tokens that contain th at the beginning, e at the end and one or
        # more alpha characters in between
        result = re.findall('th[a-zA-Z]+e', text1, re.I)
        print()
        print("RESULT FOR: 'th[a-zA-Z]+e'")
        print(result)

        # Find tokens that begin with th or d and have one of more trailing alpha character
        result = re.findall('th[a-zA-Z]+|d[a-zA-Z]+', text1, re.I)
        print()
        print("RESULT FOR: 'th[a-zA-Z]+|d[a-zA-Z]+'")
        print(result)

        # Find tokens that begin with b and end with r with only alpha characters in between.
        result = re.findall(r'\bc[a-zA-Z]+y\b', text1, re.I)
        print()
        print("RESULT FOR: '\bc[a-zA-Z]+y\b'")
        print(result)

        # Find tokens that begin with b and end with r with non-whitespace chars in between.
        result = re.findall(r'\bc\S+y\b', text1, re.I)
        print()
        print("RESULT FOR: '\bc\S+y\b'")
        print(result)

    def doEx1(self):
        text1 = "The phone number's +1902344322."

        result = re.findall(r'[a-zA-Z0-9]+', text1, re.I)
        print()
        print("RESULT FOR: '[a-zA-Z0-9]+'")
        print(result)

        text1 = "The phone number's +1902344322."
        result = re.findall(r'\d', text1, re.I)
        print()
        print("RESULT FOR: '\d'")
        print(result)

        text1 = "1902344322 87g212 g213 g32 89 gg234."
        result = re.findall(r'\d*.\d{3}', text1, re.I)
        print()
        print("RESULT FOR: '\d*.\d{3}'")
        print(result)

        text1 = "19023443223 87g212 g213 g32 89 gg234."
        result = re.findall(r'\d{11}', text1, re.I)
        print()
        print("RESULT FOR: '\d{11}'")
        print(result)

        text1 = "1902344'3223 87g212 g213 g32 89 gg234."
        result = re.findall(r'[a-z0-9\.@#\$%&]+', text1, re.I)
        print()
        print("RESULT FOR: '[a-z0-9\.@#\$%&]+'")
        print(result)


        text1 = "1902344'3223 ds87g212 g213 g32 89 gg234."
        result = re.findall(r'[a-zA-Z0-9\s]{6,20}', text1, re.I)
        print()
        print("RESULT FOR: '[a-zA-Z0-9\s]{6,20}")
        print(result)

        text1 = "https://en.wikipedia.com/wiki/Canada says Canada sucks. However, https://www.torontosom.com"
        result = re.findall(r'https:/{2}[\w\.]+[.]com', text1, re.I)
        print()
        print("RESULT FOR: 'https:/{2}[\w\.]+[.]com")
        print(result)

        text1 = """
        <html class="client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-0 vector-feature-client-preferences-disabled vector-feature-client-prefs-pinned-disabled vector-feature-night-mode-disabled skin-night-mode-clientpref-0 vector-toc-available" lang="en" dir="ltr">
        <head>
        <meta charset="UTF-8">
        <title>Canada - Wikipedia</title>
        <script>(function(){var className="client-js vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-0 vector-feature-client-preferences-disabled vector-feature-client-prefs-pinned-disabled vector-feature-night-mode-disabled skin-night-mode-clientpref-0 vector-toc-available";var cookie=document.cookie.match(/(?:^|; )enwikimwclientpreferences=([^;]+)/);if(cookie){cookie[1].split('%2C').forEach(function(pref){className=className.replace(new RegExp('(^| )'+pref.replace(/-clientpref-\w+$|[^\w-]+/g,'')+'-clientpref-\\w+( |$)'),'$1'+pref+'$2');});}document.documentElement.className=className;}());RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":["",""],
        "wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgRequestId":"ab9a150d-a94e-4343-bfe0-ac940a76aa40","wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"Canada","wgTitle":"Canada","wgCurRevisionId":1206565370,"wgRevisionId":1206565370,"wgArticleId":5042916,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Pages with non-numeric formatnum arguments","Webarchive template wayback links","CS1: Julian–Gregorian uncertainty","CS1 French-language sources (fr)","Articles containing potentially dated statements from November 2018","All articles containing potentially dated statements","CS1 Latin-language sources (la)","Articles with short description","Short description matches Wikidata","Featured articles",
        "Wikipedia extended-confirmed-protected pages","Wikipedia indefinitely move-protected pages","Use Canadian English from July 2015","All Wikipedia articles written in Canadian English","Use mdy dates from September 2023","Articles containing Latin-language text","Pages using infobox country or infobox former country with the symbol caption or type parameters","Articles containing Laurentian-language text","Pages using multiple image with auto scaled images","Articles containing French-language text","Articles containing potentially dated statements from 2023","Articles containing potentially dated statements from 2014","Pages using Sister project links with hidden wikidata","Pages using Sister project links with default search","Articles with Curlie links","Articles with FAST identifiers","Articles with ISNI identifiers","Articles with VIAF identifiers","Articles with WorldCat Entities identifiers","Articles with BNE identifiers","Articles with BNF identifiers",
        "Articles with BNFdata identifiers","Articles with GND identifiers","Articles with J9U identifiers","Articles with LCCN identifiers","Articles with NDL identifiers","Articles with NKC identifiers","Articles with NLG identifiers","Articles with MusicBrainz area identifiers","Articles with EMU identifiers","Articles with HDS identifiers","Articles with IEU identifiers","Articles with NARA identifiers","Articles with SUDOC identifiers","Articles with TDVİA identifiers","Coordinates on Wikidata","Canada","1867 establishments in Canada","Countries in North America","Countries and territories where English is an official language","Federal monarchies","Former British colonies and protectorates in the Americas","French-speaking countries and territories","G20 members","Member states of NATO","Member states of the Commonwealth of Nations","Member states of the Organisation internationale de la Francophonie","Member states of the United Nations","Northern America",
        "States and territories established in 1867","OECD members"],"wgPageViewLanguage":"en","wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgRelevantPageName":"Canada","wgRelevantArticleId":5042916,"wgIsProbablyEditable":false,"wgRelevantPageIsProbablyEditable":false,"wgRestrictionEdit":["extendedconfirmed"],"wgRestrictionMove":["sysop"],"wgNoticeProject":"wikipedia","wgFlaggedRevsParams":{"tags":{"status":{"levels":1}}},"wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgPopupsFlags":6,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en"},"wgMFDisplayWikibaseDescriptions":{"search":true,"watchlist":true,"tagline":false,"nearby":true},"wgWMESchemaEditAttemptStepOversample":false,"wgWMEPageLength":300000,"wgULSCurrentAutonym":"English","wgCoordinates":{"lat":60,"lon":-110},"wgCentralAuthMobileDomain":false,"wgEditSubmitButtonLabelPublish":true,"wgULSPosition":"interlanguage","wgULSisCompactLinksEnabled":false,
        "wgVector2022LanguageInHeader":true,"wgULSisLanguageSelectorEmpty":false,"wgWikibaseItemId":"Q16","wgCheckUserClientHintsHeadersJsApi":["architecture","bitness","brands","fullVersionList","mobile","model","platform","platformVersion"],"GEHomepageSuggestedEditsEnableTopics":true,"wgGETopicsMatchModeEnabled":false,"wgGEStructuredTaskRejectionReasonTextInputEnabled":false,"wgGELevelingUpEnabledForUser":false};RLSTATE={"skins.vector.user.styles":"ready","ext.globalCssJs.user.styles":"ready","site.styles":"ready","user.styles":"ready","skins.vector.user":"ready","ext.globalCssJs.user":"ready","user":"ready","user.options":"loading","ext.cite.styles":"ready","ext.tmh.player.styles":"ready","codex-search-styles":"ready","skins.vector.styles":"ready","skins.vector.icons":"ready","jquery.makeCollapsible.styles":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","wikibase.client.init":"ready","ext.wikimediaBadges":"ready"};RLPAGEMODULES=[
        "ext.cite.ux-enhancements","ext.tmh.player","mediawiki.page.media","ext.scribunto.logs","mediawiki.toggleAllCollapsibles","site","mediawiki.page.ready","jquery.makeCollapsible","mediawiki.toc","skins.vector.js","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.gadget.ReferenceTooltips","ext.gadget.switcher","ext.urlShortener.toolbar","ext.centralauth.centralautologin","mmv.head","mmv.bootstrap.autostart","ext.popups","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.echo.centralauth","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.uls.interface","ext.cx.eventlogging.campaigns","ext.cx.uls.quick.actions","wikibase.client.vector-2022","ext.checkUser.clientHints","ext.growthExperiments.SuggestedEditSession"];</script>
        <script>(RLQ=window.RLQ||[]).push(function(){mw.loader.impl(function(){return["user.options@12s5i",function($,jQuery,require,module){mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
        }];});});</script>
                """

        result = re.findall(r'</?[\w\s]*>|<.+[\W]>', text1, re.I)
        print()
        print("RESULT FOR: '</?[\w\s]*>|<.+[\W]>")
        print(result)





re1 = ReEngine()
#re1.demonstrateRE()
re1.doEx1()