# Audio Technica ATH-A700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.2; 54 4.2; 60 3.6; 66 4.4; 72 3.5; 79 1.9; 87 1.5; 96 1.6; 106 1.4; 116 1.2; 128 1.2; 141 1.3; 155 1.5; 170 2.0; 187 2.2; 206 2.7; 227 3.4; 249 3.2; 274 4.0; 302 4.8; 332 4.9; 365 2.8; 402 0.5; 442 -0.6; 486 -0.9; 535 -0.6; 588 0.0; 647 0.3; 712 -0.4; 783 1.3; 861 0.4; 947 0.1; 1042 0.1; 1146 0.5; 1261 0.6; 1387 -0.1; 1526 -0.0; 1678 1.0; 1846 -0.2; 2031 -0.5; 2234 1.9; 2457 4.3; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.8; 4353 0.7; 4788 3.2; 5267 6.0; 5793 5.6; 6373 4.1; 7010 2.5; 7711 -2.8; 8482 -6.0; 9330 -4.7; 10263 -0.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.57 | 6.4 dB  |
| Peaking | 288 Hz  | 2.31 | 4.7 dB  |
| Peaking | 3098 Hz | 2.28 | 6.5 dB  |
| Peaking | 5962 Hz | 2.13 | 5.9 dB  |
| Peaking | 8523 Hz | 3.75 | -8.3 dB |
| Peaking | 201 Hz  | 4.48 | 1.1 dB  |
| Peaking | 342 Hz  | 7.98 | 2.1 dB  |
| Peaking | 452 Hz  | 2.85 | -2.0 dB |
| Peaking | 1982 Hz | 6.91 | -2.3 dB |
| Peaking | 2544 Hz | 8.27 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A700/Audio%20Technica%20ATH-A700.png)