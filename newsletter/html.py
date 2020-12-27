# coding: utf-8

import bs4
import newsletter_parser.JournalNewsPrep as journalNews

myJournalNews=journalNews.JournalNews(
    date='September 11, 2020',

    title='A new publication alert from <i>Antibody Therapeutics</i>',

    editor_notes='We are pleased to introduce a recent published review article in Antibody Therapeutics, an official journal of Chinese Antibody Society, entitled “Preclinical and clinical development of therapeutic antibodies targeting functions of CD47 in the tumor microenvironment”. The corresponding authors are David D. Roberts from National Cancer Institute, National Institutes of Health. The following is the abstract of this review article.',

    article_img_url='https://res.cloudinary.com/dmqakeiv6/image/upload/v1599875049/newsletters/Screen_Shot_2020-09-11_at_8.36.31_PM_majklk.png',

    figure_caption='Figure 1. CD47 functions in the tumor microenvironment.',

    url='https://academic.oup.com/abt/article/3/3/179/5889920',

    # notice that main_text is in compressed html format
    main_text='<p>CD47 is a ubiquitously expressed cell surface glycoprotein that functions as a signaling receptor for thrombospondin-1 and as the counter-receptor for signal regulatory protein-α (SIRPα). Engaging SIRPα on macrophages inhibits phagocytosis, and CD47 thereby serves as a physiological marker of self. However, elevated CD47 expression on some cancer cells also protects tumors from innate immune surveillance and limits adaptive antitumor immunity via inhibitory SIRPα signaling in antigen-presenting cells. CD47 also mediates inhibitory thrombospondin-1 signaling in vascular cells, T cells, and NK cells, and blocking inhibitory CD47 signaling on cytotoxic T cells directly increases tumor cell killing. Therefore, CD47 functions as an innate and adaptive immune checkpoint. These findings have led to the development of antibodies and other therapeutic approaches to block CD47 functions in the tumor microenvironment (see Figure 1 above). Preclinical studies in mice demonstrated that blocking CD47 can limit the growth of hematologic malignancies and solid tumors and enhance the efficacy of conventional chemotherapy, radiation therapy, and some targeted cancer therapies. Humanized CD47 antibodies are showing promise in early clinical trials, but side effects related to enhanced phagocytic clearance of circulating blood cells remain a concern. Approaches to circumvent these include antibody preloading strategies and development of antibodies that recognize tumor-specific epitopes of CD47, SIRPα antibodies, and bivalent antibodies that restrict CD47 blockade to specific tumor cells. Preclinical and clinical development of antibodies and related biologics that inhibit CD47/SIRPα signaling are reviewed, including strategies to combine these agents with various conventional and targeted therapeutics to improve patient outcome for various cancers.</p> <p>You are welcome to read the full length of this article by clicking on link above. You are also welcome to cite this article in your own manuscripts in the future.</p>',

    add_notes_title='Call for Paper',

    add_notes_text=' <p><i>Antibody Therapeutics</i> is an official journal of the Chinese Antibody Society and published by the Oxford University Press. As a peer-reviewed and <b>open access</b> journal, <i>Antibody Therapeutics</i> provides a forum for the publication of the latest advances and challenges in the discovery, research, development and methodology of therapeutic antibodies for global scientific community.</p> <p>The current COVID-19 pandemic is an unprecedented global public health challenge. <i>Antibody Therapeutics</i> invites papers that contribute knowledge to develop therapeutics and diagnostics strategies for our battle against COVID-19. We are particularly interested in research, method or review articles regarding discovery and engineering of COVID-19 diagnostic and therapeutic antibodies for clinical applications. Given the urgency of the current global pandemic, we will provide a fast-track option for all COVID-19 manuscripts. It will take 2 weeks or less from submission to acceptance. Manuscripts should be submitted via <i>Antibody Therapeutics</i> online <a href="https://mc.manuscriptcentral.com/abt">submission site</a>. Authors can publish in the journal with no charge (see the <a href="https://academic.oup.com/abt/pages/General_Instructions">authors’ instructions</a>).</p> <p>Correspondence or questions: <a href="mailto:abt@oup.com">contact editorial office</a></p> <p><b>Editorial operation team</b></p> <p><b><i>Antibody Therapeutics</i>, an official journal of Chinese Antibody Society</b></p>'

)

soup=myJournalNews.getJournalNews()
myJournalNews.writeJournalNews('1')


