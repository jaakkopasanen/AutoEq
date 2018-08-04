# Stax SR009 SN SZ9 2251 KGSS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 5.8; 73 5.3; 78 5.1; 83 5.2; 89 5.1; 95 5.0; 102 4.6; 109 4.5; 117 4.2; 125 3.8; 134 3.5; 143 3.2; 153 3.1; 164 2.9; 175 2.9; 188 2.8; 201 2.8; 215 2.8; 230 2.8; 246 2.8; 263 2.7; 282 2.8; 301 2.7; 323 2.7; 345 2.6; 369 2.5; 395 2.4; 423 2.5; 452 2.4; 484 2.0; 518 1.9; 554 1.8; 593 1.8; 635 1.6; 679 1.2; 726 1.0; 777 1.0; 832 1.0; 890 0.7; 952 0.3; 1019 -0.0; 1090 -0.0; 1167 -0.5; 1248 -0.5; 1336 -0.6; 1429 -0.5; 1529 -0.6; 1636 -1.1; 1751 -0.2; 1873 1.7; 2004 3.0; 2145 3.3; 2295 4.4; 2455 4.8; 2627 3.8; 2811 2.8; 3008 3.2; 3219 3.1; 3444 3.7; 3685 3.7; 3943 2.6; 4219 1.2; 4514 0.4; 4830 -0.6; 5168 -0.0; 5530 3.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR009 SN SZ9 2251 KGSS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 123 Hz  | 0.09 | 8.1 dB  |
| Peaking | 603 Hz  | 0.12 | -5.3 dB |
| Peaking | 3537 Hz | 3.26 | 5.0 dB  |
| Peaking | 2381 Hz | 2.43 | 6.7 dB  |
| Peaking | 6137 Hz | 4    | 7.8 dB  |
| Peaking | 166 Hz  | 2.22 | -0.8 dB |
| Peaking | 1613 Hz | 7.13 | -1.2 dB |
| Peaking | 1444 Hz | 0.03 | 0.2 dB  |
| Peaking | 4965 Hz | 9.69 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR009%20SN%20SZ9%202251%20KGSS/Stax%20SR009%20SN%20SZ9%202251%20KGSS.png)