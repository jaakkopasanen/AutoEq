# JPS Labs Abyss AB-1266

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.7; 31 5.5; 34 5.7; 37 5.9; 41 5.8; 45 5.2; 49 4.9; 54 5.3; 60 5.7; 66 5.9; 72 5.9; 79 5.9; 87 5.7; 96 5.5; 106 5.4; 116 5.3; 128 5.0; 141 5.0; 155 4.8; 170 4.6; 187 4.5; 206 4.3; 227 4.4; 249 4.1; 274 3.9; 302 3.6; 332 3.1; 365 3.3; 402 2.8; 442 2.1; 486 5.8; 535 5.4; 588 5.1; 647 3.7; 712 2.6; 783 1.8; 861 0.4; 947 -0.1; 1042 0.9; 1146 1.1; 1261 2.1; 1387 2.6; 1526 3.2; 1678 4.5; 1846 6.0; 2031 6.0; 2234 5.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 3.8; 7010 2.2; 7711 0.3; 8482 0.0; 9330 -0.9; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.0; 18182 -1.7; 20000 -1.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JPS Labs Abyss AB-1266 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.33 | 5.4 dB  |
| Peaking | 123 Hz  | 0.41 | 4.6 dB  |
| Peaking | 538 Hz  | 3.85 | 4.4 dB  |
| Peaking | 3787 Hz | 0.54 | 7.0 dB  |
| Peaking | 8804 Hz | 1.54 | -3.6 dB |
| Peaking | 719 Hz  | 2.25 | 1.6 dB  |
| Peaking | 918 Hz  | 2.47 | -2.6 dB |
| Peaking | 1940 Hz | 2.65 | 2.6 dB  |
| Peaking | 3034 Hz | 0.35 | -0.8 dB |
| Peaking | 5704 Hz | 4.77 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JPS%20Labs%20Abyss%20AB-1266/JPS%20Labs%20Abyss%20AB-1266.png)