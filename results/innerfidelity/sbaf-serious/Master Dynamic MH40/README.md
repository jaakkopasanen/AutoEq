# Master Dynamic MH40

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.6; 22 1.4; 23 1.3; 25 1.2; 26 1.1; 28 1.0; 30 0.9; 32 0.8; 35 0.7; 37 0.6; 40 0.6; 42 0.6; 45 0.6; 49 0.5; 52 0.6; 56 0.7; 59 0.7; 64 0.8; 68 0.9; 73 1.0; 78 0.7; 83 0.3; 89 -0.4; 95 -0.8; 102 -0.8; 109 -0.8; 117 -1.1; 125 -1.7; 134 -2.4; 143 -3.0; 153 -2.7; 164 -1.6; 175 -1.8; 188 -2.3; 201 -1.9; 215 -1.4; 230 -0.7; 246 -0.1; 263 0.8; 282 1.3; 301 1.9; 323 2.5; 345 3.1; 369 3.6; 395 3.9; 423 4.2; 452 4.2; 484 3.9; 518 3.5; 554 3.3; 593 2.7; 635 2.0; 679 1.3; 726 0.9; 777 0.7; 832 0.4; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.0; 1167 -0.1; 1248 -0.1; 1336 -0.3; 1429 -0.6; 1529 -0.7; 1636 -0.6; 1751 -0.6; 1873 -0.2; 2004 0.2; 2145 1.8; 2295 2.7; 2455 2.2; 2627 0.4; 2811 -0.3; 3008 2.0; 3219 3.7; 3444 4.0; 3685 4.8; 3943 5.6; 4219 5.3; 4514 5.9; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic MH40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.14 | 1.1 dB  |
| Peaking | 157 Hz  | 1.17 | -3.5 dB |
| Peaking | 421 Hz  | 1.53 | 4.7 dB  |
| Peaking | 4149 Hz | 2.07 | 5.4 dB  |
| Peaking | 5852 Hz | 3.49 | 5.0 dB  |
| Peaking | 1502 Hz | 1.43 | -1.1 dB |
| Peaking | 1944 Hz | 2.76 | -2.3 dB |
| Peaking | 2314 Hz | 1.98 | 4.0 dB  |
| Peaking | 2743 Hz | 6.96 | -4.1 dB |
| Peaking | 9001 Hz | 3.97 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20MH40/Master%20Dynamic%20MH40.png)