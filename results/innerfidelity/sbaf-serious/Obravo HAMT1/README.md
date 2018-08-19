# Obravo HAMT1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.5; 26 5.3; 28 4.7; 30 4.0; 32 3.4; 35 2.7; 37 2.4; 40 2.2; 42 2.1; 45 1.7; 49 0.9; 52 -0.2; 56 -2.4; 59 -4.0; 64 -5.7; 68 -6.8; 73 -7.9; 78 -9.0; 83 -9.9; 89 -10.7; 95 -11.3; 102 -11.6; 109 -11.5; 117 -11.0; 125 -10.4; 134 -9.5; 143 -8.7; 153 -7.7; 164 -6.3; 175 -5.4; 188 -4.3; 201 -2.9; 215 -1.4; 230 0.3; 246 2.2; 263 4.4; 282 6.0; 301 6.0; 323 6.0; 345 6.0; 369 5.0; 395 1.5; 423 -1.8; 452 -4.2; 484 -7.4; 518 -9.9; 554 -10.1; 593 -8.9; 635 -7.4; 679 -6.1; 726 -4.8; 777 -3.6; 832 -2.5; 890 -1.7; 952 -0.7; 1019 0.3; 1090 1.4; 1167 2.6; 1248 3.7; 1336 4.7; 1429 5.7; 1529 6.0; 1636 6.0; 1751 5.9; 1873 3.0; 2004 -1.9; 2145 -4.3; 2295 -3.0; 2455 -1.7; 2627 -1.2; 2811 -1.6; 3008 -2.3; 3219 -3.0; 3444 -3.3; 3685 -3.3; 3943 -2.9; 4219 -2.2; 4514 -0.3; 4830 1.9; 5168 3.3; 5530 3.6; 5917 4.5; 6331 4.4; 6775 3.9; 7249 1.3; 7756 -0.0; 8299 -4.1; 8880 -7.4; 9502 -8.1; 10167 -6.7; 10879 -3.7; 11640 -0.5; 12455 0.0; 13327 -0.2; 14260 -1.9; 15258 -3.2; 16326 -3.6; 17469 -4.0; 18692 -4.8; 20000 -5.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Obravo HAMT1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 111 Hz   | 1.17 | -12.8 dB |
| Peaking | 325 Hz   | 1.78 | 11.6 dB  |
| Peaking | 541 Hz   | 1.91 | -12.8 dB |
| Peaking | 1461 Hz  | 3.17 | 7.6 dB   |
| Peaking | 22016 Hz | 0.12 | -4.6 dB  |
| Peaking | 24 Hz    | 1.28 | 6.7 dB   |
| Peaking | 2166 Hz  | 7.24 | -6.0 dB  |
| Peaking | 3780 Hz  | 1.29 | -11.6 dB |
| Peaking | 5696 Hz  | 0.57 | 11.6 dB  |
| Peaking | 9203 Hz  | 2.53 | -13.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Obravo%20HAMT1/Obravo%20HAMT1.png)