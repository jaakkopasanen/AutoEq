# Shure SRH940

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.1; 41 4.1; 45 3.4; 49 2.7; 54 2.1; 60 1.6; 66 1.3; 72 1.3; 79 2.0; 87 2.9; 96 3.4; 106 2.2; 116 1.3; 128 0.9; 141 0.3; 155 -0.3; 170 -0.8; 187 -2.5; 206 -3.3; 227 -3.6; 249 -3.8; 274 -3.6; 302 -3.3; 332 -4.5; 365 -3.7; 402 -3.0; 442 -2.5; 486 -2.2; 535 -1.7; 588 -0.9; 647 -0.4; 712 -0.2; 783 0.3; 861 0.3; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.2; 1387 -1.0; 1526 -1.8; 1678 -2.6; 1846 -3.1; 2031 -3.1; 2234 -3.0; 2457 -2.0; 2703 -2.2; 2973 -1.8; 3270 -1.7; 3597 -2.1; 3957 -2.1; 4353 -2.6; 4788 -1.9; 5267 -0.0; 5793 1.4; 6373 1.1; 7010 0.1; 7711 -3.4; 8482 -7.7; 9330 -9.5; 10263 -5.2; 11289 -0.0; 12418 0.0; 13660 -1.9; 15026 -2.8; 16529 -0.0; 18182 -0.4; 20000 -5.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH940 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.93 | 6.5 dB   |
| Peaking | 97 Hz    | 2.55 | 3.1 dB   |
| Peaking | 289 Hz   | 1.13 | -4.4 dB  |
| Peaking | 2235 Hz  | 1.35 | -3.0 dB  |
| Peaking | 9147 Hz  | 4.21 | -10.6 dB |
| Peaking | 885 Hz   | 2.15 | 1.2 dB   |
| Peaking | 4470 Hz  | 3.69 | -2.1 dB  |
| Peaking | 6095 Hz  | 2.81 | 3.7 dB   |
| Peaking | 11635 Hz | 4.05 | 3.2 dB   |
| Peaking | 21242 Hz | 0.08 | -1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH940/Shure%20SRH940.png)