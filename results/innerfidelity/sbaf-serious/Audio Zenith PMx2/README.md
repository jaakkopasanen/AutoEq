# Audio Zenith PMx2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.8; 26 5.7; 28 5.4; 30 5.2; 32 5.0; 35 4.7; 37 4.6; 40 4.5; 42 4.5; 45 4.6; 49 4.5; 52 4.1; 56 3.5; 59 3.1; 64 2.7; 68 2.5; 73 2.2; 78 1.9; 83 1.6; 89 1.3; 95 0.9; 102 0.6; 109 0.5; 117 0.3; 125 -0.1; 134 -0.2; 143 -0.4; 153 -0.6; 164 -0.7; 175 -0.8; 188 -1.0; 201 -1.1; 215 -1.1; 230 -1.0; 246 -1.0; 263 -1.2; 282 -1.1; 301 -1.1; 323 -0.8; 345 0.0; 369 0.7; 395 0.9; 423 0.7; 452 0.4; 484 0.1; 518 -0.1; 554 -0.2; 593 -0.1; 635 -0.2; 679 -0.4; 726 -0.5; 777 -0.4; 832 -0.2; 890 0.0; 952 0.0; 1019 0.1; 1090 0.4; 1167 0.8; 1248 1.5; 1336 1.7; 1429 1.8; 1529 1.6; 1636 1.6; 1751 2.1; 1873 2.6; 2004 3.6; 2145 4.2; 2295 4.5; 2455 5.1; 2627 5.5; 2811 5.5; 3008 5.8; 3219 5.7; 3444 5.5; 3685 5.5; 3943 5.7; 4219 5.2; 4514 5.3; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.5; 9502 -0.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Zenith PMx2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.89 | 5.5 dB  |
| Peaking | 48 Hz   | 1.06 | 2.9 dB  |
| Peaking | 203 Hz  | 1.22 | -1.4 dB |
| Peaking | 2989 Hz | 1.11 | 5.7 dB  |
| Peaking | 5547 Hz | 2.65 | 4.9 dB  |
| Peaking | 397 Hz  | 5.96 | 1.3 dB  |
| Peaking | 752 Hz  | 2.62 | -0.7 dB |
| Peaking | 4428 Hz | 2.99 | 1.1 dB  |
| Peaking | 6512 Hz | 5.31 | 3.5 dB  |
| Peaking | 7083 Hz | 1.37 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Zenith%20PMx2/Audio%20Zenith%20PMx2.png)