# Beyerdynamic DT 150 250 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 0.0; 23 1.4; 25 1.1; 28 0.7; 31 0.4; 34 0.1; 37 -0.1; 41 -0.3; 45 -0.3; 49 -0.3; 54 -0.1; 60 0.5; 66 0.5; 72 -0.4; 79 -0.9; 87 -2.5; 96 -4.2; 106 -5.1; 116 -5.6; 128 -5.9; 141 -6.1; 155 -5.8; 170 -5.2; 187 -5.5; 206 -4.6; 227 -3.7; 249 -2.5; 274 -1.1; 302 0.3; 332 1.1; 365 1.3; 402 0.9; 442 0.8; 486 0.6; 535 0.5; 588 0.7; 647 0.6; 712 0.3; 783 0.4; 861 0.2; 947 0.1; 1042 0.3; 1146 0.5; 1261 0.5; 1387 -0.1; 1526 -0.9; 1678 -1.6; 1846 -2.2; 2031 -2.8; 2234 -3.1; 2457 -2.2; 2703 -1.1; 2973 0.6; 3270 1.7; 3597 2.7; 3957 1.1; 4353 -2.6; 4788 -1.8; 5267 -0.0; 5793 0.5; 6373 5.1; 7010 2.5; 7711 0.3; 8482 -0.5; 9330 -3.6; 10263 -0.7; 11289 0.0; 12418 0.0; 13660 -1.4; 15026 -1.8; 16529 0.0; 18182 0.0; 20000 -0.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 150 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 142 Hz  | 1.39 | -6.8 dB |
| Peaking | 2142 Hz | 3.35 | -3.0 dB |
| Peaking | 3543 Hz | 3.7  | 5.1 dB  |
| Peaking | 6122 Hz | 0.92 | -5.6 dB |
| Peaking | 6446 Hz | 3.02 | 10.3 dB |
| Peaking | 20 Hz   | 2.01 | 2.0 dB  |
| Peaking | 66 Hz   | 3.35 | 1.3 dB  |
| Peaking | 101 Hz  | 3.22 | -2.4 dB |
| Peaking | 216 Hz  | 1.74 | -6.1 dB |
| Peaking | 236 Hz  | 0.75 | 4.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20150%20250%20Ohm/Beyerdynamic%20DT%20150%20250%20Ohm.png)