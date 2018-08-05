# Beyerdynamic DT 880 32 ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.7; 30 5.5; 32 5.1; 35 4.7; 37 4.4; 40 4.0; 42 3.8; 45 3.6; 49 3.3; 52 3.1; 56 2.8; 59 2.6; 64 2.4; 68 2.4; 73 2.7; 78 2.6; 83 1.8; 89 1.0; 95 0.5; 102 -0.1; 109 -0.5; 117 -1.0; 125 -1.5; 134 -2.0; 143 -2.2; 153 -2.4; 164 -2.5; 175 -2.6; 188 -2.7; 201 -2.7; 215 -2.7; 230 -2.6; 246 -2.5; 263 -2.5; 282 -2.4; 301 -2.3; 323 -2.3; 345 -2.1; 369 -2.1; 395 -1.9; 423 -1.6; 452 -1.1; 484 -1.1; 518 -1.2; 554 -1.0; 593 -0.8; 635 -0.7; 679 -0.6; 726 -0.5; 777 -0.1; 832 -0.2; 890 -0.3; 952 -0.1; 1019 0.0; 1090 0.3; 1167 0.5; 1248 0.6; 1336 0.6; 1429 0.2; 1529 -0.2; 1636 -0.6; 1751 -1.1; 1873 -1.3; 2004 -1.1; 2145 -1.1; 2295 -0.9; 2455 -0.3; 2627 -0.8; 2811 -1.0; 3008 -1.0; 3219 -1.0; 3444 -0.6; 3685 -0.5; 3943 -0.7; 4219 -0.7; 4514 0.3; 4830 2.5; 5168 5.7; 5530 6.0; 5917 5.5; 6331 0.2; 6775 -1.5; 7249 -1.9; 7756 -2.6; 8299 -4.0; 8880 -5.0; 9502 -3.7; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -3.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 22 Hz    |  0.48 | 6.2 dB  |
| Peaking | 77 Hz    |  2.5  | 2.0 dB  |
| Peaking | 191 Hz   |  0.58 | -3.2 dB |
| Peaking | 5507 Hz  |  5.5  | 7.6 dB  |
| Peaking | 8536 Hz  |  2.96 | -5.0 dB |
| Peaking | 1346 Hz  |  1.85 | 1.4 dB  |
| Peaking | 1787 Hz  |  2.07 | -1.6 dB |
| Peaking | 5069 Hz  | 10.01 | 2.3 dB  |
| Peaking | 3937 Hz  |  1.22 | -1.1 dB |
| Peaking | 10718 Hz |  5.68 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%2032%20ohm/Beyerdynamic%20DT%20880%2032%20ohm.png)