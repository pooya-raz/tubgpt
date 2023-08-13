import openai
from Config import Config

openai.api_key = Config.openapi_key

context = """1. al-Dharīʿa ilā uṣūl al-sharīʿa  
   الذريعة إلى أصول الشريعة  
   ʿAlī b. al-Ḥusayn al-Sharīf al-Murtaḍā  
   (d. 436/1044)

   **Principle Manuscripts**
    * University of California, Los Angeles (#MS164), dated 5th-9th centuries/11th-15th centuries
    * Majlis, Tehran (#3185), dated 969/1561
    * Majlis, Tehran (#3794), dated 1025/1616
    * Marʿashī, Qum (#6519), dated 1027/1618
    * Maktabat Amīr al-Muʾminīn, Najaf (#140), dated 1042/1632-33

   **Editions**
    * *al-Dharīʿa ilā uṣūl al-sharīʿa*, ed. Abū l-Qāsim al-Gurjī (Tehran: Intishārāt-i Dānishgāh-i Tehrān, 1346Sh/1967)
    * *al-Dharīʿa ilā uṣūl al-sharīʿa*, ed. Abū l-Qāsim al-Gurjī (Tehran: Intishārāt-i Dānishgāh-i Tehrān, 1363Sh/1985)
    * *al-Dharīʿa ilā uṣūl al-sharīʿa*, ed. Abū l-Qāsim al-Gurjī (Tehran: Intishārāt-i Dānishgāh-i Tehrān, 1376Sh/1998)
    * *al-Dharīʿa ilā uṣūl al-sharīʿa*, ed. al-Lajna al-ʿIlmiyya fī Muʾassasat al-Imām al-Ṣādiq (Qum: Muʾassasat al-Imām al-Ṣādiq, 1387Sh/2008)
    * *al-Dharīʿa ilā uṣūl al-sharīʿa*, ed. al-Sayyid ʿAlī Riḍā al-Madadī (Mashhad: Bunyād-i Pazhūhishhā-yi Islāmī – Āstān-i Quds-i Raḍawī, 1399Sh/2020)

   **Commentaries**
    * *Sharḥ al-Dharīʿa*, Kamāl al-Dīn al-Murtaḍā b. al-Muntahā b. al-Ḥusayn b. ʿAlī al-Ḥusaynī al-Marʿashī (d. after 525/1130)
    * *Sharḥ masāʾil al-Dharīʿa*, Muḥammad b. ʿAlī al-Ṭabarī (fl. 553/1158)
    * *al-Mustaqṣā fī sharḥ al-Dharīʿa*, Hibatallāh 'Quṭb al-Dīn al-Rāwandī (d. 573/1177)
    * *al-Iʿtibār ʿalā kitāb al-Dharīʿa ilā uṣūl al-sharīʿa*, ʿIzz al-Dīn Abū Ḥāmid ʿAbd al-Ḥamīd b. Hibatallāh b. Muḥammad (b. Muḥammad) b. al-Ḥusayn b. Abī l-Ḥadīd al-Madāʾinī al-Baghdādī (d. 655 or 656/1257 or 1258)

"""
tripleQuote = '"""'
query = tripleQuote+ context + tripleQuote + "\n\n" + "Who wrote al-Dharia?"
response = openai.ChatCompletion.create(
   model = "gpt-3.5-turbo",
   messages = [
         {"role": "system", "content": "Answer questions with the data given in triple quotes"},
       {"role": "user", "content": query}
   ] 
)
print(response["choices"][0]["message"]["content"])