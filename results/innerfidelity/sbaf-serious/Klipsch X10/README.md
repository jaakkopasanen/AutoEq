# Klipsch X10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.0; 23 -1.0; 25 -1.0; 28 -1.1; 31 -1.1; 34 -1.2; 37 -1.3; 41 -1.4; 45 -1.5; 49 -1.7; 54 -1.9; 60 -2.2; 66 -2.5; 72 -2.8; 79 -3.1; 87 -3.4; 96 -3.9; 106 -4.0; 116 -4.2; 128 -4.3; 141 -4.5; 155 -4.7; 170 -4.6; 187 -4.6; 206 -4.5; 227 -4.3; 249 -4.2; 274 -3.9; 302 -3.7; 332 -3.3; 365 -3.0; 402 -2.7; 442 -2.2; 486 -1.9; 535 -1.5; 588 -0.9; 647 -0.5; 712 -0.4; 783 0.1; 861 0.1; 947 0.0; 1042 -0.1; 1146 -0.2; 1261 -0.3; 1387 -0.6; 1526 -0.8; 1678 -1.0; 1846 -0.6; 2031 -0.3; 2234 -0.1; 2457 0.3; 2703 -0.1; 2973 0.0; 3270 2.5; 3597 5.7; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.5; 8482 -4.3; 9330 -1.7; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.17 | -0.7 dB |
| Peaking | 114 Hz  | 0.77 | -2.5 dB |
| Peaking | 243 Hz  | 0.72 | -3.2 dB |
| Peaking | 5093 Hz | 1.4  | 7.2 dB  |
| Peaking | 8550 Hz | 4.75 | -6.6 dB |
| Peaking | 806 Hz  | 2.57 | 1.0 dB  |
| Peaking | 3337 Hz | 1.01 | -2.8 dB |
| Peaking | 3730 Hz | 3.67 | 5.2 dB  |
| Peaking | 6349 Hz | 6.04 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X10/Klipsch%20X10.png)