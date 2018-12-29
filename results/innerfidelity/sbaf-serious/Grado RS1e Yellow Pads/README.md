# Grado RS1e Yellow Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.3; 45 4.3; 49 3.4; 54 2.4; 60 1.4; 66 0.5; 72 -0.3; 79 -1.0; 87 -1.7; 96 -2.2; 106 -2.6; 116 -2.8; 128 -3.1; 141 -3.2; 155 -3.2; 170 -3.1; 187 -2.9; 206 -2.7; 227 -2.1; 249 -1.9; 274 -1.7; 302 -2.1; 332 -1.7; 365 -1.4; 402 -1.1; 442 -0.7; 486 -0.5; 535 -0.4; 588 0.1; 647 0.1; 712 0.1; 783 0.4; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.0; 1261 -0.1; 1387 -0.3; 1526 0.5; 1678 -1.4; 1846 -7.5; 2031 -6.7; 2234 -3.9; 2457 -0.3; 2703 2.6; 2973 4.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1e Yellow Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e Yellow Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 32 Hz   |  0.5  | 7.6 dB   |
| Peaking | 88 Hz   |  0.63 | -4.4 dB  |
| Peaking | 182 Hz  |  0.78 | -1.8 dB  |
| Peaking | 1990 Hz |  3.77 | -10.4 dB |
| Peaking | 4012 Hz |  0.97 | 7.2 dB   |
| Peaking | 1583 Hz | 12.58 | 2.3 dB   |
| Peaking | 4251 Hz |  5.14 | -1.1 dB  |
| Peaking | 6455 Hz |  2.6  | 4.0 dB   |
| Peaking | 7406 Hz |  2.96 | -3.1 dB  |
| Peaking | 9269 Hz |  1.11 | -1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20Yellow%20Pads/Grado%20RS1e%20Yellow%20Pads.png)