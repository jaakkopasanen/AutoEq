# Audio Technica ATH-CKM500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.2dB
GraphicEQ: 10 -84; 20 -2.4; 22 -3.0; 23 -3.3; 25 -3.8; 26 -4.0; 28 -4.4; 30 -4.7; 32 -5.1; 35 -5.5; 37 -5.8; 40 -6.2; 42 -6.5; 45 -6.8; 49 -7.3; 52 -7.6; 56 -7.9; 59 -8.2; 64 -8.6; 68 -8.9; 73 -9.3; 78 -9.7; 83 -10.0; 89 -10.4; 95 -10.7; 102 -10.9; 109 -11.1; 117 -11.3; 125 -11.5; 134 -11.6; 143 -11.7; 153 -11.7; 164 -11.7; 175 -11.7; 188 -11.6; 201 -11.5; 215 -11.2; 230 -10.9; 246 -10.7; 263 -10.5; 282 -10.0; 301 -9.6; 323 -9.2; 345 -8.7; 369 -8.1; 395 -7.6; 423 -6.9; 452 -6.2; 484 -5.6; 518 -5.0; 554 -4.1; 593 -3.2; 635 -2.5; 679 -1.9; 726 -1.2; 777 -0.5; 832 -0.2; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.2; 1167 -0.5; 1248 -1.1; 1336 -1.8; 1429 -2.5; 1529 -3.1; 1636 -3.6; 1751 -4.0; 1873 -4.3; 2004 -4.6; 2145 -5.0; 2295 -5.4; 2455 -5.4; 2627 -5.7; 2811 -6.0; 3008 -6.0; 3219 -5.6; 3444 -4.8; 3685 -4.7; 3943 -4.6; 4219 -5.9; 4514 -7.1; 4830 -7.7; 5168 -7.9; 5530 -9.2; 5917 -9.2; 6331 -7.9; 6775 -6.7; 7249 -5.3; 7756 -4.2; 8299 -3.9; 8880 -4.6; 9502 -6.4; 10167 -7.5; 10879 -5.3; 11640 -0.9; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.22720988564614833dB` and instead set Global volume in the UI for both channels to **-2**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-CKM500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 98 Hz    | 0.41 | -9.7 dB |
| Peaking | 261 Hz   | 0.88 | -5.8 dB |
| Peaking | 2504 Hz  | 1.48 | -5.0 dB |
| Peaking | 5643 Hz  | 1.63 | -8.6 dB |
| Peaking | 10057 Hz | 4.78 | -6.6 dB |
| Peaking | 30 Hz    | 2.13 | -0.5 dB |
| Peaking | 474 Hz   | 2.18 | -1.5 dB |
| Peaking | 916 Hz   | 1.25 | 2.3 dB  |
| Peaking | 1596 Hz  | 2.76 | -1.8 dB |
| Peaking | 12440 Hz | 5.15 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-CKM500/Audio%20Technica%20ATH-CKM500.png)