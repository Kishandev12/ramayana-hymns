#!/usr/bin/env python3
"""
Add 10+ Sample Hymns from Different Kandas
This script automatically adds beautiful sample hymns to your website
"""

import re

SAMPLE_HYMNS = [
    {
        'kanda': 'bala',
        'title': 'Invocation to Saraswati',
        'subtitle': 'Sarga 1',
        'preview': 'Valmiki invokes Goddess Saraswati, the deity of knowledge and arts, seeking her blessings to compose the great epic.',
        'sanskrit': 'वाग्देवी प्रसीद मह्यं कविता कर्तुं शक्तिं देहि।\nत्वदनुग्रहेण वाल्मीकिः रामायणं रचयिष्यति॥',
        'transliteration': 'Vāgdevī prasīda mahyaṃ kavitā kartuṃ śaktiṃ dehi,\nTvadanugraheṇa Vālmīkiḥ Rāmāyaṇaṃ racayiṣyati',
        'translation': 'O Goddess of Speech, be pleased with me and grant me the power to compose poetry. By your grace, Valmiki shall compose the Ramayana.',
        'context': 'Before beginning the epic, Valmiki seeks divine inspiration from Saraswati, establishing the sacred nature of the composition.',
        'fullContent': '''
            <h2 class="section-title">The Divine Beginning</h2>
            <p>This invocation marks the auspicious beginning of the world's first epic poem. Valmiki acknowledges that great works of literature are born from divine grace, not mere human effort.</p>
            
            <h2 class="section-title">Significance</h2>
            <ul style="padding-left: 2rem; line-height: 2;">
                <li>Establishes the sacred tradition of invoking deities before artistic creation</li>
                <li>Shows humility of even the great sage Valmiki</li>
                <li>Connects poetry with divine inspiration</li>
            </ul>
        '''
    },
    {
        'kanda': 'ayodhya',
        'title': 'Dasharatha\'s Lament',
        'subtitle': 'Sarga 64',
        'preview': 'King Dasharatha\'s heart-wrenching words as he recalls Rama before his death, expressing the unbearable pain of separation.',
        'sanskrit': 'राम रामेति रामेति हा राम इति वदन्।\nदशरथो नृपो दुःखाद्देहं त्यक्त्वा दिवं गतः॥',
        'transliteration': 'Rāma Rāmeti Rāmeti Hā Rāma iti vadan,\nDaśaratho nṛpo duḥkhād dehaṃ tyaktvā divaṃ gataḥ',
        'translation': 'Crying "Rama, Rama, Rama, O Rama!", King Dasharatha, overcome with grief, left his body and ascended to heaven.',
        'context': 'Unable to bear separation from his beloved son Rama, Dasharatha passes away calling out his name repeatedly.',
        'fullContent': '''
            <h2 class="section-title">The Power of a Father's Love</h2>
            <p>This poignant moment captures the depth of parental love. Dasharatha, a mighty emperor who ruled the prosperous kingdom of Ayodhya, finds that worldly power means nothing without his son.</p>
            
            <div class="translation" style="margin: 2rem 0;">
                "What use is this kingdom without Rama? What use is life itself? A father's heart cannot survive when separated from his beloved child."
            </div>
            
            <h2 class="section-title">Spiritual Teaching</h2>
            <p>The constant repetition of "Rama" at the moment of death is significant in Hindu tradition. The name of God on one's lips at death is considered the highest blessing, ensuring liberation.</p>
        '''
    },
    {
        'kanda': 'aranya',
        'title': 'Sita\'s Devotion',
        'subtitle': 'Sarga 10',
        'preview': 'Sita\'s beautiful words expressing her unwavering devotion to Rama, declaring she would rather be with him in the forest than in heaven.',
        'sanskrit': 'छायेव रामस्य निवसामि वने।\nस्वर्गोऽपि न मे रोचते रामं विना॥',
        'transliteration': 'Chāyeva Rāmasya nivasāmi vane,\nSwargo\'pi na me rocate Rāmaṃ vinā',
        'translation': 'I dwell in the forest like the shadow of Rama. Even heaven does not appeal to me without Rama.',
        'context': 'When asked to return to Ayodhya, Sita firmly declares her intention to stay with Rama in exile.',
        'fullContent': '''
            <h2 class="section-title">Ideal of Devotion</h2>
            <p>Sita's words represent the highest ideal of devotion in Hindu philosophy - where the devotee finds the presence of the divine more valuable than any worldly or heavenly pleasure.</p>
            
            <div class="sanskrit-text" style="margin: 2rem 0;">
                न मे रोचते स्वर्गो ना च राज्यं न च सुखम्।<br>
                यत्र रामो न तिष्ठेत तत्र मे नास्ति वासनम्॥
            </div>
            
            <div class="translation">
                Heaven appeals not to me, nor kingdom, nor pleasure. Where Rama is not, there I have no desire to dwell.
            </div>
        '''
    },
    {
        'kanda': 'kishkinda',
        'title': 'Hanuman\'s First Meeting with Rama',
        'subtitle': 'Sarga 3',
        'preview': 'The momentous first meeting between Hanuman and Lord Rama, marking the beginning of eternal devotion.',
        'sanskrit': 'नमामि चरणौ रामस्य करुणासागरस्य च।\nभक्तानां अभयप्रदं सदा रक्षकं जगत्॥',
        'transliteration': 'Namāmi caraṇau Rāmasya karuṇāsāgarasya ca,\nBhaktānāṃ abhayapradaṃ sadā rakṣakaṃ jagat',
        'translation': 'I bow to the feet of Rama, who is an ocean of compassion, the giver of fearlessness to devotees, and the eternal protector of the universe.',
        'context': 'Upon meeting Rama, Hanuman immediately recognizes His divine nature and surrenders completely.',
        'fullContent': '''
            <h2 class="section-title">The Meeting of Devotee and Divine</h2>
            <p>This meeting between Hanuman and Rama is one of the most significant moments in the Ramayana. It establishes the ideal relationship between devotee and deity.</p>
            
            <h2 class="section-title">Hanuman's Recognition</h2>
            <p>Disguised in human form, Rama's divinity was not apparent to all. But Hanuman, with his pure heart and spiritual insight, immediately recognized the Supreme Lord.</p>
            
            <div class="translation" style="margin: 2rem 0;">
                "At first sight itself, my heart recognized You as the Supreme Being. Your form radiates divine grace, and Your eyes overflow with compassion. I am eternally blessed to serve You."
            </div>
        '''
    },
    {
        'kanda': 'sundara',
        'title': 'Hanuman\'s Leap',
        'subtitle': 'Sarga 1',
        'preview': 'Hanuman prepares to leap across the ocean to Lanka, invoking divine blessings and demonstrating supreme devotion.',
        'sanskrit': 'यत्र यत्र रघुनाथकीर्तनं तत्र तत्र कृतमस्तकाञ्जलिम्।\nभाष्पवारिपरिपूर्णलोचनं मारुतिं नमत राक्षसान्तकम्॥',
        'transliteration': 'Yatra yatra raghunāthakīrtanaṃ tatra tatra kṛtamastakāñjalim,\nBhāṣpavāriparipūrṇalocanaṃ mārutiṃ namata rākṣasāntakam',
        'translation': 'Wherever the glories of Rama are sung, there Hanuman appears with folded hands and eyes filled with tears of devotion. Bow to that Maruti, the destroyer of demons.',
        'context': 'Before his impossible leap across the ocean, Hanuman meditates on Rama, drawing divine strength from devotion.',
        'fullContent': '''
            <h2 class="section-title">The Impossible Made Possible</h2>
            <p>Hanuman faced an impossible task - leap 100 yojanas (about 800 miles) across the ocean. Mountains of obstacles lay ahead: the vast ocean, demon guardians, and his own self-doubt.</p>
            
            <h2 class="section-title">The Source of Strength</h2>
            <p>What enabled Hanuman to accomplish the impossible? Not physical strength alone, but complete surrender to Rama. He declares:</p>
            
            <div class="sanskrit-text" style="margin: 2rem 0;">
                राम काज कीन्हे बिनु मोहि कहाँ बिश्राम।<br>
                सत्य प्रतिज्ञा राघव की करिहउँ कपि काम॥
            </div>
            
            <div class="translation">
                "Without accomplishing Rama's mission, I shall find no rest. True to Rama's promise, I shall fulfill this monkey's task."
            </div>
            
            <h2 class="section-title">Universal Message</h2>
            <p>Hanuman's leap teaches us that when we align ourselves with a higher purpose and seek divine grace with complete faith, no obstacle is insurmountable.</p>
        '''
    },
    {
        'kanda': 'sundara',
        'title': 'Sita in Ashoka Vatika',
        'subtitle': 'Sarga 15',
        'preview': 'Hanuman finds Sita in the Ashoka grove, where despite suffering, she remains devoted to Rama.',
        'sanskrit': 'राममेव सदा ध्यायन्ती रुदन्ती च मुहुर्मुहुः।\nपतिव्रता सीता दुःखं सहते रावणालये॥',
        'transliteration': 'Rāmameva sadā dhyāyantī rudantī ca muhurmuhuh,\nPativatā Sītā duḥkhaṃ sahate rāvaṇālaye',
        'translation': 'Always meditating on Rama and weeping repeatedly, the devoted wife Sita bears suffering in Ravana\'s abode.',
        'context': 'Despite captivity and constant threats, Sita\'s mind never wavers from Rama.',
        'fullContent': '''
            <h2 class="section-title">Unwavering Faith</h2>
            <p>Sita's situation represents the darkest trial - separated from her beloved, imprisoned by a demon king, threatened daily. Yet her faith remains unshaken.</p>
            
            <div class="translation" style="margin: 2rem 0;">
                "Though my body is imprisoned here, my mind dwells eternally with Rama. Ravana may have power over this physical form, but my soul belongs only to my Lord."
            </div>
            
            <h2 class="section-title">The Power of Chastity</h2>
            <p>Sita's purity creates an invisible shield around her. Despite Ravana's power, he cannot touch her. This demonstrates the spiritual truth that purity is the greatest protection.</p>
        '''
    },
    {
        'kanda': 'yuddha',
        'title': 'Rama\'s Prayer to Surya',
        'subtitle': 'Sarga 105',
        'preview': 'Before the final battle with Ravana, Sage Agastya teaches Rama the Aditya Hridayam, the hymn to the Sun God.',
        'sanskrit': 'आदित्यहृदयं पुण्यं सर्वशत्रुविनाशनम्।\nजयावहं जपेन्नित्यं अक्षयं परमं शिवम्॥',
        'transliteration': 'Ādityahṛdayaṃ puṇyaṃ sarvaśatruvināśanam,\nJayāvahaṃ japennityaṃ akṣayaṃ paramaṃ śivam',
        'translation': 'The Aditya Hridayam is sacred, destroyer of all enemies, bestower of victory. Chanting it daily brings imperishable supreme auspiciousness.',
        'context': 'The powerful Aditya Hridayam stotra, recited to give Rama strength before his final battle.',
        'fullContent': '''
            <h2 class="section-title">The Supreme Hymn</h2>
            <p>The Aditya Hridayam is considered one of the most powerful hymns in Hindu scriptures. It was taught to Rama by Sage Agastya at the critical moment before facing Ravana.</p>
            
            <h2 class="section-title">Why Sun God?</h2>
            <p>Surya, the Sun God, represents:</p>
            <ul style="padding-left: 2rem; line-height: 2;">
                <li>Eternal energy and vitality</li>
                <li>Dispeller of darkness (ignorance)</li>
                <li>Witness to all actions</li>
                <li>Source of all life</li>
            </ul>
            
            <div class="translation" style="margin: 2rem 0;">
                "O Rama, worship the Sun God with this hymn. He who gives light to all worlds, who destroys darkness, who witnesses all actions - His grace will ensure your victory."
            </div>
        '''
    },
    {
        'kanda': 'yuddha',
        'title': 'Victory Hymn',
        'subtitle': 'Sarga 109',
        'preview': 'After defeating Ravana, the gods sing praises to Rama, recognizing his divine nature and righteous victory.',
        'sanskrit': 'जयति तदङ्कुरो वंशः कोसलानां महात्मनाम्।\nयत्र जातो महाभागो रामो दाशरथिः प्रभुः॥',
        'transliteration': 'Jayati tadaṅkuro vaṃśaḥ kosalānāṃ mahātmanām,\nYatra jāto mahābhāgo rāmo dāśarathiḥ prabhuḥ',
        'translation': 'Victory to that noble lineage of the great souls of Kosala, in which was born the supremely fortunate Rama, son of Dasharatha, the Lord.',
        'context': 'The celestial beings celebrate Rama\'s victory over evil, praising his divine glory.',
        'fullContent': '''
            <h2 class="section-title">Victory of Dharma</h2>
            <p>Rama's victory over Ravana represents more than a military triumph. It symbolizes the eternal victory of dharma (righteousness) over adharma (unrighteousness).</p>
            
            <div class="sanskrit-text" style="margin: 2rem 0;">
                परित्राणाय साधूनां विनाशाय च दुष्कृताम्।<br>
                धर्मसंस्थापनार्थाय सम्भवामि युगे युगे॥
            </div>
            
            <div class="translation">
                "For the protection of the good, for the destruction of evildoers, and for the establishment of dharma, I manifest age after age."
            </div>
            
            <h2 class="section-title">Universal Celebration</h2>
            <p>Not just humans, but all celestial beings - gods, sages, ancestors - rejoiced at this victory. It was a cosmic event restoring balance to the universe.</p>
        '''
    },
    {
        'kanda': 'uttara',
        'title': 'Rama\'s Coronation Hymn',
        'subtitle': 'Sarga 4',
        'preview': 'The hymn sung during Rama\'s coronation as emperor of Ayodhya, celebrating the return of the righteous king.',
        'sanskrit': 'अयोध्यावासिभिः सर्वैः कृतं रामाभिषेचनम्।\nप्रहृष्टा मानवाः सर्वे रामो राजा भविष्यति॥',
        'transliteration': 'Ayodhyāvāsibhiḥ sarvaiḥ kṛtaṃ rāmābhiṣecanam,\nPrahṛṣṭā mānavāḥ sarve rāmo rājā bhaviṣyati',
        'translation': 'All residents of Ayodhya performed Rama\'s coronation. All people rejoiced that Rama would be their king.',
        'context': 'After 14 years of exile and victory over Ravana, Rama returns to rule Ayodhya.',
        'fullContent': '''
            <h2 class="section-title">The Return of the King</h2>
            <p>Rama's coronation marks the beginning of Ram Rajya - the golden age of righteous rule that has become synonymous with the perfect society.</p>
            
            <h2 class="section-title">Characteristics of Ram Rajya</h2>
            <ul style="padding-left: 2rem; line-height: 2;">
                <li>No poverty or suffering among citizens</li>
                <li>Justice equal for all</li>
                <li>Natural harmony and prosperity</li>
                <li>Dharma upheld in all aspects of life</li>
                <li>People lived long, healthy lives</li>
            </ul>
            
            <div class="translation" style="margin: 2rem 0;">
                "In Rama's kingdom, trees bore fruit in all seasons, cows gave abundant milk, clouds rained exactly when needed, and every citizen lived content and virtuous."
            </div>
        '''
    },
    {
        'kanda': 'uttara',
        'title': 'Final Prayers',
        'subtitle': 'Sarga 110',
        'preview': 'The concluding prayers of the Ramayana, blessing all who read and recite this sacred epic.',
        'sanskrit': 'रामायणं यः पठेद्विप्रो यश्चृणुयाद्विचक्षणः।\nसर्वपापविनिर्मुक्तो विष्णुलोकं स गच्छति॥',
        'transliteration': 'Rāmāyaṇaṃ yaḥ paṭhedvipro yaścṛṇuyādvicakṣaṇaḥ,\nSarvapāpavinirmukto viṣṇulokaṃ sa gacchati',
        'translation': 'The wise one who reads or listens to the Ramayana becomes freed from all sins and attains Vishnu\'s eternal abode.',
        'context': 'Valmiki concludes his epic with blessings for all readers and listeners.',
        'fullContent': '''
            <h2 class="section-title">The Power of Sacred Literature</h2>
            <p>The Ramayana is not merely a story but a spiritual text. Reading, hearing, or contemplating it is considered a spiritual practice that purifies the mind and elevates consciousness.</p>
            
            <h2 class="section-title">Blessings for Readers</h2>
            <div class="translation" style="margin: 2rem 0;">
                "One who reads even one verse of the Ramayana with devotion,<br>
                One who hears it with faith and attention,<br>
                One who contemplates its meaning with a pure heart —<br>
                All sins are washed away, and the supreme goal is attained."
            </div>
            
            <h2 class="section-title">Living the Ramayana</h2>
            <p>The true purpose of the Ramayana is not just to be read but to be lived. Each character teaches us how to navigate life's challenges with grace, devotion, and adherence to dharma.</p>
            
            <div class="sanskrit-text" style="margin: 2rem 0;">
                रामो विग्रहवान् धर्मः साधुः सत्यपराक्रमः।<br>
                राजा सर्वस्य लोकस्य देवानामपि रक्षकः॥
            </div>
            
            <div class="translation">
                "Rama is dharma incarnate, virtuous and truly valorous,<br>
                King of all worlds and protector even of the gods."
            </div>
        '''
    }
]

def add_hymns_to_index():
    """Add all sample hymns to index.html"""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find hymnsData array
        match = re.search(r'const hymnsData = \[(.*?)\];', content, re.DOTALL)
        if not match
