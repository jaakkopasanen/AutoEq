# Bluedio R2-WH

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.2; 22 0.4; 23 -0.0; 25 -0.8; 26 -1.1; 28 -1.7; 30 -2.3; 32 -2.7; 35 -3.2; 37 -3.5; 40 -3.8; 42 -4.0; 45 -4.2; 49 -4.3; 52 -4.3; 56 -4.4; 59 -4.4; 64 -4.4; 68 -4.4; 73 -4.3; 78 -4.2; 83 -4.1; 89 -4.0; 95 -4.2; 102 -4.8; 109 -5.2; 117 -5.5; 125 -5.6; 134 -6.1; 143 -6.4; 153 -6.6; 164 -6.3; 175 -6.3; 188 -6.3; 201 -6.1; 215 -5.8; 230 -5.7; 246 -5.1; 263 -5.6; 282 -5.5; 301 -5.1; 323 -4.5; 345 -4.5; 369 -4.4; 395 -3.7; 423 -2.9; 452 -2.6; 484 -2.4; 518 -1.8; 554 -0.7; 593 0.6; 635 1.3; 679 2.1; 726 2.7; 777 3.1; 832 2.6; 890 1.4; 952 0.5; 1019 -0.1; 1090 -0.3; 1167 -0.2; 1248 0.0; 1336 0.0; 1429 0.1; 1529 0.1; 1636 -0.2; 1751 -0.6; 1873 -1.0; 2004 -1.4; 2145 -0.3; 2295 -0.2; 2455 -0.1; 2627 0.0; 2811 0.5; 3008 1.6; 3219 3.0; 3444 3.9; 3685 4.3; 3943 5.8; 4219 6.0; 4514 5.7; 4830 5.3; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio R2-WH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 1.4  | 2.9 dB  |
| Peaking | 42 Hz   | 1.16 | -2.9 dB |
| Peaking | 192 Hz  | 0.4  | -6.1 dB |
| Peaking | 722 Hz  | 2.31 | 5.1 dB  |
| Peaking | 4873 Hz | 1.59 | 6.8 dB  |
| Peaking | 11 Hz   | 1.13 | 1.6 dB  |
| Peaking | 2036 Hz | 3.3  | -1.3 dB |
| Peaking | 3812 Hz | 2.9  | 3.0 dB  |
| Peaking | 6210 Hz | 3.27 | 5.6 dB  |
| Peaking | 5810 Hz | 1.03 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bluedio%20R2-WH/Bluedio%20R2-WH.png)