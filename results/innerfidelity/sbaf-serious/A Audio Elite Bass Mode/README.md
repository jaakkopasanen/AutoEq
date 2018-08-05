# A Audio Elite Bass Mode

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 2.7; 22 3.2; 23 3.5; 25 3.9; 26 4.1; 28 4.4; 30 4.7; 32 4.9; 35 5.2; 37 5.4; 40 5.6; 42 5.7; 45 5.8; 49 5.9; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 5.6; 102 5.1; 109 4.7; 117 4.5; 125 4.3; 134 3.8; 143 3.4; 153 3.3; 164 3.4; 175 3.4; 188 3.3; 201 3.2; 215 3.4; 230 3.6; 246 3.7; 263 4.2; 282 4.5; 301 4.5; 323 4.7; 345 4.8; 369 5.1; 395 4.8; 423 4.3; 452 3.8; 484 3.7; 518 3.4; 554 2.9; 593 2.5; 635 2.0; 679 2.2; 726 2.5; 777 2.6; 832 1.4; 890 1.0; 952 0.5; 1019 -0.2; 1090 -0.3; 1167 0.6; 1248 1.9; 1336 2.9; 1429 3.7; 1529 4.5; 1636 5.2; 1751 5.9; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `A Audio Elite Bass Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.74 | 3.4 dB  |
| Peaking | 79 Hz    | 0.69 | 4.7 dB  |
| Peaking | 356 Hz   | 1.15 | 4.4 dB  |
| Peaking | 2287 Hz  | 1.12 | 5.9 dB  |
| Peaking | 4969 Hz  | 1.58 | 5.4 dB  |
| Peaking | 1071 Hz  | 5.36 | -2.7 dB |
| Peaking | 1615 Hz  | 4.16 | 1.4 dB  |
| Peaking | 36953 Hz | 1.12 | -0.3 dB |
| Peaking | 6440 Hz  | 4.54 | 3.6 dB  |
| Peaking | 7395 Hz  | 2.02 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/A%20Audio%20Elite%20Bass%20Mode/A%20Audio%20Elite%20Bass%20Mode.png)