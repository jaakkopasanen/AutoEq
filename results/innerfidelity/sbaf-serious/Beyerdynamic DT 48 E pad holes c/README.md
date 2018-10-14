# Beyerdynamic DT 48 E pad holes c

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.8; 72 0.3; 79 -3.9; 87 -1.2; 96 0.2; 106 -2.1; 116 -1.5; 128 -1.0; 141 -0.5; 155 0.4; 170 -0.5; 187 -0.2; 206 0.3; 227 1.0; 249 1.6; 274 2.3; 302 3.0; 332 3.6; 365 4.2; 402 5.1; 442 6.0; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 6.0; 783 4.8; 861 2.7; 947 1.1; 1042 -0.6; 1146 -1.6; 1261 -2.1; 1387 -2.6; 1526 -3.5; 1678 -4.7; 1846 -4.9; 2031 -4.9; 2234 -3.6; 2457 -0.6; 2703 2.1; 2973 3.5; 3270 3.7; 3597 4.9; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -2.9; 8482 -7.4; 9330 -4.6; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -4.3; 16529 -6.6; 18182 -4.2; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 E pad holes c ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 1.11 | 7.3 dB   |
| Peaking | 512 Hz   | 1.56 | 7.1 dB   |
| Peaking | 5212 Hz  | 1.52 | 7.6 dB   |
| Peaking | 8505 Hz  | 4.77 | -10.0 dB |
| Peaking | 16702 Hz | 2.25 | -7.4 dB  |
| Peaking | 65 Hz    | 2.77 | 5.4 dB   |
| Peaking | 78 Hz    | 5.61 | -7.7 dB  |
| Peaking | 115 Hz   | 2.92 | -2.6 dB  |
| Peaking | 731 Hz   | 5.28 | 3.4 dB   |
| Peaking | 1747 Hz  | 2.18 | -6.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20E%20pad%20holes%20c/Beyerdynamic%20DT%2048%20E%20pad%20holes%20c.png)