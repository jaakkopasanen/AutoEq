# Sony MDR-1000X Wireless NC Off

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 10 -84; 20 -4.0; 22 -4.2; 23 -4.3; 25 -4.5; 26 -4.6; 28 -4.7; 30 -4.9; 32 -4.9; 35 -5.1; 37 -5.1; 40 -5.3; 42 -5.4; 45 -5.5; 49 -5.6; 52 -5.7; 56 -5.7; 59 -5.6; 64 -5.4; 68 -5.2; 73 -4.9; 78 -4.8; 83 -4.6; 89 -4.6; 95 -5.3; 102 -6.5; 109 -6.9; 117 -7.4; 125 -7.7; 134 -6.9; 143 -6.0; 153 -5.6; 164 -3.8; 175 -4.0; 188 -4.4; 201 -3.6; 215 -2.8; 230 -2.1; 246 -1.9; 263 -2.3; 282 -2.4; 301 -2.4; 323 -2.0; 345 -1.4; 369 -0.7; 395 -0.4; 423 -0.8; 452 -1.3; 484 -1.5; 518 -1.8; 554 -1.0; 593 0.4; 635 -0.0; 679 -1.7; 726 -2.0; 777 0.1; 832 0.2; 890 -0.5; 952 -0.3; 1019 -0.0; 1090 0.7; 1167 2.5; 1248 2.0; 1336 3.0; 1429 1.8; 1529 1.0; 1636 0.3; 1751 -2.1; 1873 -3.0; 2004 -3.3; 2145 -4.0; 2295 -2.4; 2455 -1.3; 2627 0.2; 2811 -0.2; 3008 -1.3; 3219 -1.5; 3444 -1.5; 3685 -1.6; 3943 -4.4; 4219 -6.0; 4514 -5.4; 4830 -3.0; 5168 -3.1; 5530 -5.5; 5917 -5.4; 6331 -4.2; 6775 -0.9; 7249 -0.5; 7756 -2.0; 8299 -4.1; 8880 -5.1; 9502 -4.3; 10167 -2.3; 10879 -0.4; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.151295247253532dB` and instead set Global volume in the UI for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wireless NC Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.58 | -5.0 dB |
| Peaking | 128 Hz   | 1.04 | -5.7 dB |
| Peaking | 4794 Hz  | 1.43 | -4.8 dB |
| Peaking | 9028 Hz  | 4.92 | -4.6 dB |
| Peaking | 24000 Hz | 2.15 | -2.8 dB |
| Peaking | 955 Hz   | 0.58 | -0.9 dB |
| Peaking | 1332 Hz  | 2.31 | 4.5 dB  |
| Peaking | 2079 Hz  | 2.42 | -4.6 dB |
| Peaking | 2642 Hz  | 2.98 | 2.9 dB  |
| Peaking | 11855 Hz | 3.94 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wireless%20NC%20Off/Sony%20MDR-1000X%20Wireless%20NC%20Off.png)