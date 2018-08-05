# Onkyo IE-HF300S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.5; 22 -0.8; 23 -0.9; 25 -1.2; 26 -1.3; 28 -1.6; 30 -1.8; 32 -1.9; 35 -2.1; 37 -2.2; 40 -2.4; 42 -2.4; 45 -2.6; 49 -2.7; 52 -2.7; 56 -2.8; 59 -2.9; 64 -2.9; 68 -3.0; 73 -3.1; 78 -3.3; 83 -3.5; 89 -3.9; 95 -4.3; 102 -4.8; 109 -5.2; 117 -5.7; 125 -6.2; 134 -6.6; 143 -6.8; 153 -6.9; 164 -6.9; 175 -6.8; 188 -6.6; 201 -6.5; 215 -6.2; 230 -5.9; 246 -5.7; 263 -5.4; 282 -5.0; 301 -4.7; 323 -4.4; 345 -3.9; 369 -3.6; 395 -3.3; 423 -2.8; 452 -2.4; 484 -2.1; 518 -1.7; 554 -1.3; 593 -0.7; 635 -0.4; 679 -0.3; 726 -0.1; 777 0.3; 832 0.3; 890 0.3; 952 0.1; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.3; 1529 -1.6; 1636 -1.8; 1751 -1.7; 1873 -1.3; 2004 -0.7; 2145 0.0; 2295 0.7; 2455 1.8; 2627 2.8; 2811 3.7; 3008 4.8; 3219 5.6; 3444 6.0; 3685 5.3; 3943 4.1; 4219 1.8; 4514 -0.3; 4830 -1.3; 5168 -1.1; 5530 -0.3; 5917 1.2; 6331 2.7; 6775 3.4; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -1.7; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Onkyo IE-HF300S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.99 | -1.6 dB |
| Peaking | 173 Hz   | 0.67 | -7.0 dB |
| Peaking | 1700 Hz  | 3.44 | -2.2 dB |
| Peaking | 3296 Hz  | 2.74 | 6.5 dB  |
| Peaking | 24000 Hz | 2.25 | 0.7 dB  |
| Peaking | 791 Hz   | 2.85 | 1.2 dB  |
| Peaking | 3900 Hz  | 6.61 | 2.0 dB  |
| Peaking | 4858 Hz  | 3.26 | -2.9 dB |
| Peaking | 6578 Hz  | 5.05 | 3.7 dB  |
| Peaking | 8956 Hz  | 7.37 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Onkyo%20IE-HF300S/Onkyo%20IE-HF300S.png)