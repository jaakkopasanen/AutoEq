# Sony MDR-AS40EX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 -2.1; 22 -2.5; 23 -2.6; 25 -2.9; 26 -3.1; 28 -3.3; 30 -3.5; 32 -3.6; 35 -3.9; 37 -4.0; 40 -4.2; 42 -4.3; 45 -4.5; 49 -4.7; 52 -4.9; 56 -5.0; 59 -5.2; 64 -5.4; 68 -5.6; 73 -5.9; 78 -6.1; 83 -6.3; 89 -6.5; 95 -6.5; 102 -6.7; 109 -6.8; 117 -6.8; 125 -6.9; 134 -7.0; 143 -7.0; 153 -7.0; 164 -6.9; 175 -6.9; 188 -6.7; 201 -6.6; 215 -6.4; 230 -6.1; 246 -5.8; 263 -5.5; 282 -5.1; 301 -4.7; 323 -4.2; 345 -4.1; 369 -3.8; 395 -3.5; 423 -3.1; 452 -2.7; 484 -2.4; 518 -2.0; 554 -1.6; 593 -1.1; 635 -0.8; 679 -0.4; 726 0.1; 777 0.2; 832 0.3; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -0.9; 1429 -1.3; 1529 -1.7; 1636 -2.2; 1751 -2.5; 1873 -2.1; 2004 -1.3; 2145 -0.5; 2295 0.3; 2455 1.1; 2627 1.9; 2811 2.5; 3008 3.2; 3219 3.5; 3444 3.5; 3685 2.4; 3943 0.2; 4219 -2.4; 4514 -4.4; 4830 -4.9; 5168 -3.7; 5530 -1.7; 5917 -0.2; 6331 0.4; 6775 0.1; 7249 -1.3; 7756 -3.7; 8299 -5.9; 8880 -5.8; 9502 -2.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -1.8; 16326 -6.0; 17469 -6.0; 18692 -2.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6888459689549826dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-AS40EX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 76 Hz    | 0.36 | -5.0 dB |
| Peaking | 204 Hz   | 0.71 | -3.7 dB |
| Peaking | 8472 Hz  | 4.97 | -6.7 dB |
| Peaking | 17121 Hz | 3.05 | -7.3 dB |
| Peaking | 24000 Hz | 1.97 | -3.7 dB |
| Peaking | 818 Hz   | 2.72 | 1.3 dB  |
| Peaking | 1767 Hz  | 2.53 | -2.9 dB |
| Peaking | 3297 Hz  | 1.95 | 4.5 dB  |
| Peaking | 4652 Hz  | 3.15 | -7.8 dB |
| Peaking | 5444 Hz  | 0.95 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-AS40EX/Sony%20MDR-AS40EX.png)