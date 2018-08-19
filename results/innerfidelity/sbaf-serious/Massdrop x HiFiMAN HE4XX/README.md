# Massdrop x HiFiMAN HE4XX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 10 -84; 20 4.0; 22 3.5; 23 3.2; 25 2.8; 26 2.7; 28 2.4; 30 2.2; 32 2.0; 35 1.8; 37 1.8; 40 1.7; 42 1.6; 45 1.6; 49 1.5; 52 1.4; 56 1.1; 59 0.8; 64 0.4; 68 0.3; 73 0.1; 78 -0.0; 83 -0.2; 89 -0.4; 95 -0.6; 102 -0.8; 109 -0.8; 117 -0.9; 125 -1.2; 134 -1.3; 143 -1.3; 153 -1.5; 164 -1.6; 175 -1.7; 188 -1.8; 201 -1.9; 215 -1.8; 230 -1.6; 246 -1.5; 263 -1.4; 282 -1.4; 301 -1.6; 323 -1.8; 345 -2.0; 369 -2.2; 395 -2.0; 423 -1.6; 452 -1.0; 484 -0.6; 518 -1.1; 554 -1.3; 593 -1.1; 635 -1.1; 679 -1.3; 726 -1.2; 777 -0.3; 832 -0.3; 890 -0.3; 952 -0.3; 1019 0.1; 1090 0.4; 1167 0.6; 1248 1.0; 1336 0.9; 1429 1.0; 1529 1.1; 1636 1.4; 1751 1.8; 1873 1.9; 2004 1.7; 2145 1.2; 2295 0.9; 2455 -0.1; 2627 -0.7; 2811 -1.0; 3008 -1.3; 3219 -1.0; 3444 0.0; 3685 -0.2; 3943 -0.1; 4219 -2.3; 4514 -3.3; 4830 -2.0; 5168 0.5; 5530 1.3; 5917 0.3; 6331 -2.8; 6775 -5.5; 7249 -6.0; 7756 -5.4; 8299 -5.8; 8880 -6.8; 9502 -5.2; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.0; 20000 -1.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.094867438619666dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x HiFiMAN HE4XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.25 | 3.7 dB  |
| Peaking | 241 Hz   | 0.34 | -1.9 dB |
| Peaking | 1985 Hz  | 1.1  | 3.0 dB  |
| Peaking | 2764 Hz  | 1.63 | -2.5 dB |
| Peaking | 8094 Hz  | 2.42 | -6.9 dB |
| Peaking | 3900 Hz  | 4.59 | 2.0 dB  |
| Peaking | 4482 Hz  | 4.09 | -4.3 dB |
| Peaking | 5525 Hz  | 3.98 | 3.9 dB  |
| Peaking | 6733 Hz  | 7.38 | -3.1 dB |
| Peaking | 10911 Hz | 5.98 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20HiFiMAN%20HE4XX/Massdrop%20x%20HiFiMAN%20HE4XX.png)