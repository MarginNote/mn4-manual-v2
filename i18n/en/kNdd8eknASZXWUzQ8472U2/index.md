# Custom Card Fonts

> 💡MarginNote lets you customize the fonts of cards and text boxes, breaking past the limits of your device's default fonts to personalize how your text looks. Switch font styles freely to match your own taste, so the text in your notes, documents, and more reflects your personal aesthetic and gives you a visual experience all your own.

## 1 Using and Switching Fonts

### 1.1 Switching Fonts in MN

- Select the text, then pick the font you want from the keyboard accessory bar to switch.

![Switching fonts in MN Switching fonts in MN ](image/2d465873b2749e3a.webp)

> 💡**Can't find the "keyboard accessory bar"? How do I open it?**
>
> Open MN Settings → Keyboard → turn off "Hide Keyboard Accessory Bar"
>
> ![Enabling the keyboard accessory bar Enabling the keyboard accessory bar ](image/f4d1b203fdebf2b4.webp)

### 1.2 Preview

- A comparison of a note before and after switching fonts

![Preview of custom fonts in use Preview of custom fonts in use ](image/9c88e20f044e6301.webp)

## 2 Installing Custom Fonts on Mac

### **Download the Font File**

- Open your browser and enter a font download URL (using [http://aafont.com.cn](http://aafont.com.cn "http://aafont.com.cn") as an example), pick a font you like, and click Download

![Mac: downloading the font file Mac: downloading the font file ](image/18788abeb260d46d.webp)

### 2.2 Install the Font File

- Open the downloaded font file (.ttf/.otf) and choose "Install"; the font is then installed automatically

![Mac: the font file installs automatically Mac: the font file installs automatically ](image/8ef7bdeb6dbc1ac8.webp)

## 3 Installing Custom Fonts on iPhone / iPad

### **Download the Font File**

- Open your browser and enter a font download URL (using [http://aafont.com.cn](http://aafont.com.cn "http://aafont.com.cn") as an example), pick a font you like, and click Download

![iOS: downloading the font file iOS: downloading the font file ](image/57dbde2218b19b61.webp)

- The downloaded font file (.ttf/.otf) is saved in the "Files app"; remember where it is stored

![Where the font file is stored Where the font file is stored ](image/8adf3d648e16b05a.webp)

> ⚠️If the downloaded font comes as a compressed (.zip) archive, unzip it first!

### 3.2 Install the Fontcase app from the App Store **, then import the font file you saved earlier**

- Import → select the saved font file → Open → Install → Download Fonts → allow the configuration profile to download → a popup confirms the download succeeded

![Animated demo: downloading the configuration profile Animated demo: downloading the configuration profile ](image/b96538921c5c3f9b.webp)

### **Install the Configuration Profile**

- Download the configuration profile in Fontcase
- System Settings → Install Profile → Install → enter your password → Install → Install Profile → Done

![Animated demo: installing the configuration profile Animated demo: installing the configuration profile ](image/0b28d5ec9b08a422.webp)

### 3.4 Use the Custom Font

Launch MarginNote and you can use the newly installed font; for the steps, see Using and Switching Fonts.

> 💡If the font list doesn't update, restart the app or your device.
>
> Third-party fonts often include only a Regular weight, so bold, italic, and underline may not be available.

## 4 Beautify Your Handwriting: **Turn on "Scribble" to Instantly Polish Your Writing**

System Settings → Apple Pencil → Scribble, which automatically converts your handwriting into printed text

![Enabling the Apple Pencil Scribble feature Enabling the Apple Pencil Scribble feature ](image/88ea2ffa274fae0e.webp)

## 5 Recommended Font Download Sites

- $Aa Font Library$
  > A complete collection of Chinese handwriting fonts
  > [Aa Font Library – Worry-free fonts for businesses. Founded in 2015, Aa Font Library is dedicated to creating commercial fonts with distinctive, original designs. It currently offers over 3,000 copyrighted font sets, spanning professional, creative, calligraphy, handwriting, and decorative styles. https://www.aafont.com.cn](https://www.aafont.com.cn "Aa字库-让企业用字无忧 Aa字库成立于2015年，致力于创造原创设计风格独树一帜的商用字体。目前版权字体超3000套，包括专业字体、创意字体、书法字体、手写字体、装饰字体等。 https://www.aafont.com.cn")
- $DaFont$
  > Stylish English fonts
  > [DaFont - Download fonts Archive of freely downloadable fonts. Browse by alphabetical listing, by style, by author or by popularity. https://www.dafont.com](https://www.dafont.com "DaFont - Download fonts Archive of freely downloadable fonts. Browse by alphabetical listing, by style, by author or by popularity. https://www.dafont.com")
- $100Font$
  > A huge library of free fonts
  > [  https://www.100font.com](https://www.100font.com "  https://www.100font.com")
- $Font World $
  > The pinnacle of design fonts
  > [Font World – Free downloads and online previews for all kinds of fonts. Font World offers high-speed, free downloads and online previews of Chinese fonts, handwriting fonts, English fonts, graphic fonts, and more. https://www.fonts.net.cn](https://www.fonts.net.cn "字体天下-提供各类字体的免费下载和在线预览服务 字体天下提供中文字体、手写字体、英文字体、图形字体等各种字体的高速免费下载和在线预览服务. https://www.fonts.net.cn")

## 6 FAQ

### 6.1 Q1: What should I do if font installation fails?

If font installation fails, troubleshoot in the following order:

1. Update your system to iOS 13+ and free up storage space (leave at least a few dozen MB available);
2. Confirm the font file is in .ttf / .otf format and is complete and undamaged;
3. Use a reputable font app (such as Fontcase / iFont) to import it, and install the profile when prompted;
4. Go to Settings → General → VPN & Device Management and trust the profile;
5. Restart your phone, then check whether the installation succeeded under Settings → General → Fonts;
6. Still failing: try a different font file, switch to a different font-installer app, or update iOS.

### 6.2 Q2: What should I do if fonts don't display?

Cause: This is a bug in OS 26 — the "Cambria Math" font was not bundled in the build, yet this font is essential for rendering PDF math formulas. After upgrading, this missing font causes formulas that previously displayed correctly to fail to show.

![PDF math formulas that previously rendered correctly now show as "dots" — " ••• •• " PDF math formulas that previously rendered correctly now show as "dots" — " ••• •• " ](image/621c9f61875ce6a1.webp)

There are 2 solutions:

1. Flatten the PDF: Export the PDF as a print version. Flattening the PDF resolves most PDF compatibility issues.

![Print → PDF → Save as PDF Print → PDF → Save as PDF ](image/6e7d17811bdeae4b.webp)

1. Manually install the "Cambria Math" font; once installed, formulas display correctly again.

   [cambria math.ttf](file/86b2771fbe9e9d55.ttf)

![After installing the "Cambria Math" font, formulas render correctly After installing the "Cambria Math" font, formulas render correctly ](image/9387ad09b83bb424.webp)

### 6.3 Q3: How do I remove an installed custom font?

- Method 1: Delete the profile
  1. Open System Settings → General → VPN & Device Management;
  2. Find the profile that corresponds to the font (such as iFont or Fontcase);
  3. Tap Remove Profile → confirm with your password;
  4. Go back to System Settings → General → Fonts, and the font will be gone.
- Method 3: Uninstall the font app directly
  1. Simply uninstall the font app (iFont, Fontcase, etc.);
  2. The system automatically removes all fonts installed by that app.
