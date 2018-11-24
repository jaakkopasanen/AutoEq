# Klipsch Mode M40

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.2; 25 2.6; 28 1.8; 31 1.3; 34 0.8; 37 0.5; 41 0.2; 45 -0.0; 49 -0.2; 54 -0.2; 60 -0.3; 66 -0.2; 72 -0.2; 79 -0.3; 87 -0.3; 96 -0.4; 106 -0.4; 116 -0.2; 128 -0.3; 141 -0.4; 155 -0.4; 170 -0.2; 187 -0.2; 206 -0.1; 227 0.1; 249 0.5; 274 0.4; 302 0.6; 332 1.1; 365 1.0; 402 1.0; 442 1.0; 486 1.1; 535 1.1; 588 1.4; 647 1.3; 712 1.2; 783 1.2; 861 0.8; 947 0.3; 1042 -0.2; 1146 -0.9; 1261 -2.0; 1387 -3.8; 1526 -5.3; 1678 -4.8; 1846 -3.0; 2031 0.4; 2234 3.2; 2457 5.4; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Mode M40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Mode M40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.33 | 4.8 dB  |
| Peaking | 99 Hz   | 0.24 | -0.7 dB |
| Peaking | 511 Hz  | 0.6  | 1.5 dB  |
| Peaking | 1601 Hz | 2.05 | -9.5 dB |
| Peaking | 3261 Hz | 0.7  | 7.7 dB  |
| Peaking | 1927 Hz | 7.57 | -0.9 dB |
| Peaking | 2504 Hz | 3.31 | 1.5 dB  |
| Peaking | 3357 Hz | 2.46 | -1.3 dB |
| Peaking | 6235 Hz | 2.17 | 5.6 dB  |
| Peaking | 7422 Hz | 1.45 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Mode%20M40/Klipsch%20Mode%20M40.png)