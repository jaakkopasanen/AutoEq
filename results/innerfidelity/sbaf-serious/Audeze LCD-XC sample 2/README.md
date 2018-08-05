# Audeze LCD-XC sample 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.6; 59 4.8; 64 3.6; 68 3.2; 73 3.2; 78 3.2; 83 3.0; 89 2.8; 95 2.6; 102 2.5; 109 2.4; 117 1.9; 125 1.6; 134 1.5; 143 1.4; 153 1.5; 164 1.6; 175 1.1; 188 1.2; 201 1.4; 215 1.5; 230 1.8; 246 2.0; 263 2.1; 282 2.3; 301 2.4; 323 2.4; 345 2.5; 369 2.4; 395 2.3; 423 2.4; 452 2.2; 484 1.8; 518 1.7; 554 2.0; 593 2.1; 635 2.1; 679 1.8; 726 1.4; 777 1.1; 832 0.7; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.7; 1167 -1.2; 1248 -1.7; 1336 -2.3; 1429 -3.0; 1529 -3.7; 1636 -4.2; 1751 -4.3; 1873 -4.0; 2004 -3.2; 2145 -2.1; 2295 -1.0; 2455 0.6; 2627 1.7; 2811 2.1; 3008 3.1; 3219 3.7; 3444 4.4; 3685 4.4; 3943 2.8; 4219 -0.0; 4514 -2.8; 4830 -3.3; 5168 1.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -0.4; 16326 -0.6; 17469 -1.4; 18692 -2.8; 20000 -4.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.52 | 6.5 dB  |
| Peaking | 436 Hz   | 0.7  | 2.4 dB  |
| Peaking | 1680 Hz  | 1.83 | -5.0 dB |
| Peaking | 3255 Hz  | 3.34 | 5.0 dB  |
| Peaking | 6066 Hz  | 5.33 | 6.8 dB  |
| Peaking | 3818 Hz  | 7.72 | 3.0 dB  |
| Peaking | 2567 Hz  | 8.96 | 1.5 dB  |
| Peaking | 4778 Hz  | 4.33 | -6.0 dB |
| Peaking | 5408 Hz  | 8.52 | 5.4 dB  |
| Peaking | 19703 Hz | 1.6  | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-XC%20sample%202/Audeze%20LCD-XC%20sample%202.png)