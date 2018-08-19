# A Audio Elite Bass Mode

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.7; 22 3.2; 23 3.4; 25 3.9; 26 4.0; 28 4.4; 30 4.7; 32 4.9; 35 5.1; 37 5.3; 40 5.4; 42 5.5; 45 5.7; 49 5.7; 52 5.7; 56 5.8; 59 5.9; 64 5.8; 68 5.8; 73 5.7; 78 5.6; 83 5.4; 89 5.2; 95 4.9; 102 4.5; 109 4.3; 117 4.3; 125 4.3; 134 4.0; 143 3.6; 153 3.6; 164 3.6; 175 3.6; 188 3.5; 201 3.4; 215 3.5; 230 3.7; 246 3.8; 263 4.3; 282 4.6; 301 4.5; 323 4.7; 345 4.8; 369 5.1; 395 4.8; 423 4.3; 452 3.8; 484 3.7; 518 3.4; 554 2.9; 593 2.5; 635 2.0; 679 2.2; 726 2.5; 777 2.6; 832 1.4; 890 1.0; 952 0.5; 1019 -0.2; 1090 -0.3; 1167 0.6; 1248 1.9; 1336 2.9; 1429 3.7; 1529 4.5; 1636 5.2; 1751 5.9; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `A Audio Elite Bass Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.87 | 1.0 dB  |
| Peaking | 61 Hz    | 0.44 | 5.4 dB  |
| Peaking | 359 Hz   | 1.17 | 4.2 dB  |
| Peaking | 2287 Hz  | 1.12 | 5.9 dB  |
| Peaking | 4967 Hz  | 1.58 | 5.4 dB  |
| Peaking | 1072 Hz  | 5.34 | -2.7 dB |
| Peaking | 1616 Hz  | 4.19 | 1.4 dB  |
| Peaking | 6378 Hz  | 4.51 | 3.6 dB  |
| Peaking | 7484 Hz  | 2    | -2.4 dB |
| Peaking | 11096 Hz | 1.22 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/A%20Audio%20Elite%20Bass%20Mode/A%20Audio%20Elite%20Bass%20Mode.png)