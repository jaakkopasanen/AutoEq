# Stax SR-009 SZ9-1278 after burnin

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.9; 59 5.4; 64 5.0; 68 5.1; 73 5.3; 78 5.3; 83 5.3; 89 5.1; 95 4.9; 102 4.6; 109 4.4; 117 4.1; 125 3.7; 134 3.4; 143 3.2; 153 3.0; 164 2.8; 175 2.8; 188 2.8; 201 2.7; 215 2.7; 230 2.8; 246 2.7; 263 2.6; 282 2.6; 301 2.6; 323 2.5; 345 2.5; 369 2.4; 395 2.3; 423 2.3; 452 2.2; 484 1.8; 518 1.7; 554 1.8; 593 1.8; 635 1.5; 679 1.3; 726 1.2; 777 1.3; 832 1.4; 890 1.1; 952 0.5; 1019 -0.1; 1090 -0.1; 1167 -0.6; 1248 -0.4; 1336 -0.5; 1429 -0.7; 1529 -1.0; 1636 -1.4; 1751 -0.7; 1873 0.4; 2004 1.5; 2145 2.0; 2295 2.8; 2455 3.9; 2627 4.1; 2811 3.1; 3008 2.7; 3219 2.4; 3444 3.5; 3685 3.5; 3943 2.1; 4219 1.3; 4514 0.2; 4830 -0.5; 5168 0.9; 5530 5.2; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 SZ9-1278 after burnin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.3  | 4.8 dB  |
| Peaking | 121 Hz   | 0.23 | 2.5 dB  |
| Peaking | 2552 Hz  | 4.53 | 4.0 dB  |
| Peaking | 3531 Hz  | 5.05 | 3.1 dB  |
| Peaking | 6074 Hz  | 4.88 | 6.6 dB  |
| Peaking | 165 Hz   | 2.96 | -0.6 dB |
| Peaking | 1412 Hz  | 1.34 | -3.0 dB |
| Peaking | 4816 Hz  | 8.71 | -2.3 dB |
| Peaking | 1364 Hz  | 0.49 | 1.5 dB  |
| Peaking | 23999 Hz | 1.82 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009%20SZ9-1278%20after%20burnin/Stax%20SR-009%20SZ9-1278%20after%20burnin.png)