# Stax SR-009 SN SZ9 2251 KGSS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.9; 59 5.6; 64 5.6; 68 5.3; 73 4.6; 78 4.4; 83 4.4; 89 4.4; 95 4.3; 102 4.1; 109 4.1; 117 4.0; 125 3.8; 134 3.6; 143 3.4; 153 3.3; 164 3.2; 175 3.1; 188 3.1; 201 3.0; 215 3.0; 230 3.0; 246 2.9; 263 2.8; 282 2.8; 301 2.8; 323 2.7; 345 2.6; 369 2.5; 395 2.4; 423 2.5; 452 2.4; 484 2.0; 518 1.9; 554 1.8; 593 1.8; 635 1.6; 679 1.2; 726 1.0; 777 1.0; 832 1.0; 890 0.7; 952 0.3; 1019 -0.0; 1090 -0.0; 1167 -0.5; 1248 -0.5; 1336 -0.6; 1429 -0.5; 1529 -0.6; 1636 -1.1; 1751 -0.2; 1873 1.7; 2004 3.0; 2145 3.3; 2295 4.4; 2455 4.8; 2627 3.8; 2811 2.8; 3008 3.2; 3219 3.1; 3444 3.7; 3685 3.7; 3943 2.6; 4219 1.2; 4514 0.4; 4830 -0.6; 5168 -0.0; 5530 3.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 SN SZ9 2251 KGSS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 106 Hz   |  0.09 | 8.0 dB  |
| Peaking | 551 Hz   |  0.1  | -5.0 dB |
| Peaking | 2371 Hz  |  2.42 | 6.7 dB  |
| Peaking | 3540 Hz  |  3.29 | 4.9 dB  |
| Peaking | 6161 Hz  |  4.03 | 7.7 dB  |
| Peaking | 55 Hz    |  3.59 | 0.4 dB  |
| Peaking | 1649 Hz  |  9.73 | -1.4 dB |
| Peaking | 4184 Hz  |  0.13 | 0.2 dB  |
| Peaking | 4984 Hz  | 11.29 | -1.9 dB |
| Peaking | 11254 Hz |  2.63 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009%20SN%20SZ9%202251%20KGSS/Stax%20SR-009%20SN%20SZ9%202251%20KGSS.png)