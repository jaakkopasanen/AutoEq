# Audio Technica ATH-CKM500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.7dB
GraphicEQ: 10 -84; 20 -2.3; 22 -2.9; 23 -3.2; 25 -3.7; 26 -3.9; 28 -4.2; 30 -4.5; 32 -4.8; 35 -5.3; 37 -5.5; 40 -5.8; 42 -6.0; 45 -6.3; 49 -6.6; 52 -6.7; 56 -7.0; 59 -7.1; 64 -7.3; 68 -7.5; 73 -7.8; 78 -8.1; 83 -8.4; 89 -8.8; 95 -9.3; 102 -9.9; 109 -10.3; 117 -10.9; 125 -11.5; 134 -11.8; 143 -12.1; 153 -12.2; 164 -12.3; 175 -12.2; 188 -12.1; 201 -11.9; 215 -11.6; 230 -11.3; 246 -11.0; 263 -10.7; 282 -10.2; 301 -9.8; 323 -9.3; 345 -8.8; 369 -8.2; 395 -7.7; 423 -6.9; 452 -6.3; 484 -5.7; 518 -5.0; 554 -4.2; 593 -3.2; 635 -2.5; 679 -1.9; 726 -1.3; 777 -0.6; 832 -0.2; 890 0.0; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.5; 1248 -1.1; 1336 -1.8; 1429 -2.5; 1529 -3.1; 1636 -3.6; 1751 -4.0; 1873 -4.3; 2004 -4.6; 2145 -5.0; 2295 -5.4; 2455 -5.4; 2627 -5.7; 2811 -6.0; 3008 -6.0; 3219 -5.6; 3444 -4.8; 3685 -4.7; 3943 -4.6; 4219 -5.9; 4514 -7.1; 4830 -7.7; 5168 -7.9; 5530 -9.2; 5917 -9.2; 6331 -7.9; 6775 -6.7; 7249 -5.3; 7756 -4.2; 8299 -3.9; 8880 -4.6; 9502 -6.4; 10167 -7.5; 10879 -5.3; 11640 -0.9; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.7dB` and instead set Global volume in the UI for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-CKM500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 84 Hz    | 0.32 | -6.3 dB |
| Peaking | 213 Hz   | 0.69 | -8.0 dB |
| Peaking | 2510 Hz  | 1.5  | -5.0 dB |
| Peaking | 5641 Hz  | 1.63 | -8.6 dB |
| Peaking | 10056 Hz | 4.76 | -6.5 dB |
| Peaking | 234 Hz   | 2.02 | 1.7 dB  |
| Peaking | 478 Hz   | 0.57 | -2.3 dB |
| Peaking | 856 Hz   | 1.03 | 3.7 dB  |
| Peaking | 1599 Hz  | 2.76 | -1.8 dB |
| Peaking | 12418 Hz | 5.15 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-CKM500/Audio%20Technica%20ATH-CKM500.png)