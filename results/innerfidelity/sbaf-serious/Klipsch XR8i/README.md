# Klipsch XR8i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -7.0; 22 -7.1; 23 -7.2; 25 -7.2; 26 -7.2; 28 -7.2; 30 -7.2; 32 -7.1; 35 -7.0; 37 -6.9; 40 -6.8; 42 -6.7; 45 -6.6; 49 -6.4; 52 -6.2; 56 -6.0; 59 -5.9; 64 -5.7; 68 -5.5; 73 -5.4; 78 -5.3; 83 -5.3; 89 -5.3; 95 -5.5; 102 -5.7; 109 -5.9; 117 -6.1; 125 -6.3; 134 -6.4; 143 -6.4; 153 -6.3; 164 -6.2; 175 -5.8; 188 -5.5; 201 -5.3; 215 -4.8; 230 -4.5; 246 -4.3; 263 -4.0; 282 -3.7; 301 -3.4; 323 -3.0; 345 -2.7; 369 -2.4; 395 -2.1; 423 -1.7; 452 -1.4; 484 -1.2; 518 -0.9; 554 -0.5; 593 -0.1; 635 0.1; 679 0.2; 726 0.3; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -0.8; 1429 -1.1; 1529 -1.4; 1636 -1.5; 1751 -1.5; 1873 -1.3; 2004 -1.2; 2145 -1.1; 2295 -1.1; 2455 -0.6; 2627 -0.2; 2811 0.5; 3008 2.0; 3219 3.7; 3444 5.2; 3685 5.5; 3943 5.2; 4219 3.9; 4514 3.4; 4830 4.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch XR8i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.38 | -7.0 dB |
| Peaking | 163 Hz  | 0.77 | -5.1 dB |
| Peaking | 2095 Hz | 1.6  | -2.0 dB |
| Peaking | 3614 Hz | 2.96 | 5.5 dB  |
| Peaking | 5698 Hz | 2.88 | 6.3 dB  |
| Peaking | 353 Hz  | 2.17 | -0.6 dB |
| Peaking | 756 Hz  | 1.55 | 1.1 dB  |
| Peaking | 1503 Hz | 4.49 | -0.7 dB |
| Peaking | 6584 Hz | 7.88 | 2.1 dB  |
| Peaking | 7713 Hz | 2.33 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20XR8i/Klipsch%20XR8i.png)