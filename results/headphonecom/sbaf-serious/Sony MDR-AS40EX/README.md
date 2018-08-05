# Sony MDR-AS40EX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 10 -84; 20 -2.1; 22 -2.4; 23 -2.6; 25 -2.8; 26 -3.0; 28 -3.1; 30 -3.3; 32 -3.4; 35 -3.6; 37 -3.6; 40 -3.7; 42 -3.8; 45 -4.0; 49 -4.0; 52 -4.1; 56 -4.1; 59 -4.1; 64 -4.2; 68 -4.2; 73 -4.3; 78 -4.5; 83 -4.7; 89 -4.9; 95 -5.2; 102 -5.6; 109 -6.1; 117 -6.4; 125 -7.0; 134 -7.2; 143 -7.4; 153 -7.5; 164 -7.4; 175 -7.4; 188 -7.2; 201 -7.0; 215 -6.7; 230 -6.4; 246 -6.1; 263 -5.7; 282 -5.3; 301 -4.8; 323 -4.4; 345 -4.2; 369 -3.9; 395 -3.6; 423 -3.1; 452 -2.7; 484 -2.5; 518 -2.1; 554 -1.6; 593 -1.0; 635 -0.7; 679 -0.5; 726 -0.0; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -0.9; 1429 -1.3; 1529 -1.6; 1636 -2.2; 1751 -2.5; 1873 -2.0; 2004 -1.3; 2145 -0.5; 2295 0.2; 2455 1.2; 2627 1.8; 2811 2.5; 3008 3.3; 3219 3.5; 3444 3.4; 3685 2.3; 3943 0.5; 4219 -2.4; 4514 -4.6; 4830 -5.0; 5168 -3.6; 5530 -1.7; 5917 -0.3; 6331 0.4; 6775 0.2; 7249 -1.2; 7756 -3.7; 8299 -6.1; 8880 -5.9; 9502 -2.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -2.0; 16326 -6.1; 17469 -5.9; 18692 -2.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.1dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-AS40EX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.6  | -2.9 dB |
| Peaking | 173 Hz   | 0.65 | -7.3 dB |
| Peaking | 8511 Hz  | 5.15 | -6.9 dB |
| Peaking | 24000 Hz | 1.97 | -3.8 dB |
| Peaking | 31097 Hz | 3.04 | -7.3 dB |
| Peaking | 817 Hz   | 2.73 | 1.3 dB  |
| Peaking | 1775 Hz  | 2.37 | -3.1 dB |
| Peaking | 3342 Hz  | 1.77 | 4.6 dB  |
| Peaking | 4650 Hz  | 3.45 | -7.5 dB |
| Peaking | 6809 Hz  | 0.36 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-AS40EX/Sony%20MDR-AS40EX.png)