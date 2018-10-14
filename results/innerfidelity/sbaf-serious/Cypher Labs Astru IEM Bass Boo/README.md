# Cypher Labs Astru IEM Bass Boo

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 0.0; 23 0.4; 25 0.4; 28 0.4; 31 0.4; 34 0.3; 37 0.2; 41 -0.0; 45 -0.2; 49 -0.4; 54 -0.6; 60 -1.0; 66 -1.3; 72 -1.7; 79 -2.2; 87 -2.6; 96 -3.1; 106 -3.4; 116 -3.5; 128 -3.9; 141 -4.1; 155 -4.2; 170 -4.4; 187 -4.4; 206 -4.4; 227 -4.2; 249 -4.1; 274 -3.9; 302 -3.7; 332 -3.4; 365 -3.0; 402 -2.7; 442 -2.2; 486 -1.9; 535 -1.4; 588 -0.7; 647 -0.3; 712 -0.1; 783 0.4; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.9; 1387 -1.7; 1526 -2.6; 1678 -3.6; 1846 -4.4; 2031 -5.0; 2234 -4.7; 2457 -2.9; 2703 -2.0; 2973 -0.4; 3270 1.3; 3597 1.0; 3957 -1.5; 4353 -3.6; 4788 -1.1; 5267 -0.2; 5793 0.2; 6373 3.1; 7010 1.7; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.2dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cypher Labs Astru IEM Bass Boo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.4dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 197 Hz  | 0.55 | -4.7 dB  |
| Peaking | 1986 Hz | 1.32 | -10.2 dB |
| Peaking | 2094 Hz | 0.54 | 5.2 dB   |
| Peaking | 4359 Hz | 5.84 | -5.1 dB  |
| Peaking | 6418 Hz | 8.86 | 2.7 dB   |
| Peaking | 31 Hz   | 1.28 | 0.9 dB   |
| Peaking | 768 Hz  | 2.69 | 0.8 dB   |
| Peaking | 3002 Hz | 0.1  | -0.2 dB  |
| Peaking | 3010 Hz | 3.04 | -0.7 dB  |
| Peaking | 3339 Hz | 5.76 | 2.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cypher%20Labs%20Astru%20IEM%20Bass%20Boo/Cypher%20Labs%20Astru%20IEM%20Bass%20Boo.png)