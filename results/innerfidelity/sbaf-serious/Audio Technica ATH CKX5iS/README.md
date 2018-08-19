# Audio Technica ATH CKX5iS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 10 -84; 20 -6.8; 22 -6.8; 23 -6.8; 25 -6.8; 26 -6.8; 28 -6.8; 30 -6.8; 32 -6.8; 35 -6.8; 37 -6.8; 40 -6.8; 42 -6.8; 45 -6.8; 49 -6.7; 52 -6.7; 56 -6.7; 59 -6.7; 64 -6.6; 68 -6.7; 73 -6.7; 78 -6.7; 83 -6.7; 89 -6.7; 95 -6.7; 102 -6.6; 109 -6.4; 117 -6.3; 125 -6.2; 134 -6.0; 143 -5.9; 153 -5.7; 164 -5.5; 175 -5.1; 188 -4.9; 201 -4.6; 215 -4.2; 230 -3.9; 246 -3.6; 263 -3.3; 282 -2.9; 301 -2.6; 323 -2.2; 345 -1.8; 369 -1.5; 395 -1.1; 423 -0.7; 452 -0.4; 484 -0.2; 518 0.0; 554 0.4; 593 0.8; 635 1.0; 679 1.0; 726 1.1; 777 1.2; 832 1.0; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.4; 1336 -1.9; 1429 -2.6; 1529 -3.5; 1636 -4.0; 1751 -4.3; 1873 -4.0; 2004 -3.5; 2145 -3.8; 2295 -4.3; 2455 -4.5; 2627 -5.2; 2811 -5.8; 3008 -5.4; 3219 -4.4; 3444 -2.9; 3685 -2.2; 3943 -2.6; 4219 -4.3; 4514 -6.1; 4830 -7.4; 5168 -8.3; 5530 -8.3; 5917 -6.0; 6331 -3.6; 6775 -1.4; 7249 -0.2; 7756 0.2; 8299 0.0; 8880 -1.0; 9502 -3.2; 10167 -5.5; 10879 -5.7; 11640 -3.9; 12455 -2.9; 13327 -4.1; 14260 -5.1; 15258 -2.6; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.3254239745287397dB` and instead set Global volume in the UI for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH CKX5iS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.25 | -7.3 dB |
| Peaking | 1714 Hz  | 3.24 | -3.6 dB |
| Peaking | 2750 Hz  | 2.6  | -5.1 dB |
| Peaking | 5190 Hz  | 3.5  | -8.5 dB |
| Peaking | 12249 Hz | 1.45 | -4.7 dB |
| Peaking | 18 Hz    | 2.47 | -0.9 dB |
| Peaking | 679 Hz   | 1.91 | 2.1 dB  |
| Peaking | 7954 Hz  | 4.07 | 2.6 dB  |
| Peaking | 10284 Hz | 6.91 | -3.1 dB |
| Peaking | 16753 Hz | 5.52 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH%20CKX5iS/Audio%20Technica%20ATH%20CKX5iS.png)