# Audio Technica ATH-M50x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.7; 22 -1.2; 23 -1.4; 25 -1.8; 26 -1.9; 28 -2.2; 30 -2.5; 32 -2.7; 35 -2.9; 37 -3.0; 40 -3.1; 42 -3.1; 45 -3.2; 49 -3.2; 52 -3.1; 56 -3.0; 59 -2.9; 64 -2.8; 68 -2.4; 73 -1.6; 78 -0.6; 83 -0.0; 89 0.4; 95 0.2; 102 -0.9; 109 -1.8; 117 -2.2; 125 -2.9; 134 -3.7; 143 -4.0; 153 -3.7; 164 -2.0; 175 -2.4; 188 -2.9; 201 -2.1; 215 -1.4; 230 -0.5; 246 0.4; 263 1.2; 282 1.9; 301 2.4; 323 2.4; 345 2.2; 369 1.9; 395 1.6; 423 1.4; 452 1.1; 484 0.6; 518 0.2; 554 0.1; 593 0.2; 635 -0.1; 679 -0.3; 726 -0.4; 777 -0.3; 832 -0.4; 890 -0.3; 952 -0.0; 1019 0.0; 1090 0.2; 1167 0.5; 1248 0.1; 1336 -0.7; 1429 -1.3; 1529 -2.0; 1636 -2.6; 1751 -3.1; 1873 -3.1; 2004 -2.8; 2145 -2.4; 2295 -1.8; 2455 -0.6; 2627 0.3; 2811 1.3; 3008 2.6; 3219 3.3; 3444 4.0; 3685 3.8; 3943 2.3; 4219 0.1; 4514 0.4; 4830 3.1; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.096989832632929dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 1.24 | -3.6 dB |
| Peaking | 145 Hz   | 3.15 | -4.0 dB |
| Peaking | 1884 Hz  | 2.57 | -3.7 dB |
| Peaking | 3350 Hz  | 3.95 | 4.1 dB  |
| Peaking | 5777 Hz  | 3.34 | 6.8 dB  |
| Peaking | 89 Hz    | 7.2  | 1.6 dB  |
| Peaking | 197 Hz   | 4.68 | -2.2 dB |
| Peaking | 321 Hz   | 2.11 | 2.8 dB  |
| Peaking | 1170 Hz  | 7.92 | 0.9 dB  |
| Peaking | 24000 Hz | 1.79 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M50x/Audio%20Technica%20ATH-M50x.png)