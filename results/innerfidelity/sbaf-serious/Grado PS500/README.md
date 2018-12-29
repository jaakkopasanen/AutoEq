# Grado PS500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.4; 37 4.4; 41 3.2; 45 2.0; 49 1.0; 54 -0.2; 60 -1.5; 66 -2.6; 72 -3.5; 79 -4.2; 87 -4.9; 96 -5.3; 106 -5.4; 116 -5.2; 128 -5.0; 141 -4.6; 155 -4.1; 170 -3.5; 187 -2.9; 206 -3.0; 227 -2.4; 249 -2.0; 274 -1.5; 302 -1.1; 332 -0.8; 365 -0.4; 402 -0.0; 442 0.2; 486 0.2; 535 0.4; 588 0.8; 647 0.8; 712 0.6; 783 0.8; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -1.0; 1387 -2.0; 1526 -3.1; 1678 -3.7; 1846 -4.5; 2031 -6.3; 2234 -5.6; 2457 -2.0; 2703 0.8; 2973 3.4; 3270 4.3; 3597 2.2; 3957 1.3; 4353 2.9; 4788 3.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.3; 9330 -4.2; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.81 | 7.3 dB  |
| Peaking | 100 Hz  | 0.79 | -6.5 dB |
| Peaking | 2054 Hz | 2.28 | -7.3 dB |
| Peaking | 3052 Hz | 3.08 | 5.6 dB  |
| Peaking | 5643 Hz | 3.19 | 6.9 dB  |
| Peaking | 639 Hz  | 0.71 | 3.0 dB  |
| Peaking | 656 Hz  | 0.39 | -1.8 dB |
| Peaking | 7734 Hz | 1.02 | 1.0 dB  |
| Peaking | 9206 Hz | 4.47 | -5.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20PS500/Grado%20PS500.png)