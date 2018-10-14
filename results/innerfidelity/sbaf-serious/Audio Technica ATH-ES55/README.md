# Audio Technica ATH-ES55

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 5.6; 128 4.5; 141 3.9; 155 3.5; 170 3.6; 187 2.9; 206 2.6; 227 2.4; 249 2.2; 274 2.5; 302 3.0; 332 2.9; 365 2.5; 402 2.5; 442 2.7; 486 2.6; 535 2.7; 588 2.8; 647 2.4; 712 1.8; 783 1.4; 861 0.7; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.8; 1387 -1.4; 1526 -2.0; 1678 -2.2; 1846 -1.6; 2031 -0.6; 2234 0.9; 2457 2.8; 2703 4.2; 2973 5.4; 3270 5.5; 3597 5.1; 3957 5.4; 4353 5.6; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.3; 16529 -1.1; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ES55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.27 | 6.4 dB  |
| Peaking | 541 Hz   | 1.16 | 2.3 dB  |
| Peaking | 1734 Hz  | 1.34 | -4.1 dB |
| Peaking | 3122 Hz  | 1.3  | 6.1 dB  |
| Peaking | 5488 Hz  | 2.43 | 5.2 dB  |
| Peaking | 104 Hz   | 5.69 | 1.0 dB  |
| Peaking | 6532 Hz  | 6.67 | 2.4 dB  |
| Peaking | 7799 Hz  | 2.31 | -1.7 dB |
| Peaking | 15474 Hz | 4.1  | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ES55/Audio%20Technica%20ATH-ES55.png)