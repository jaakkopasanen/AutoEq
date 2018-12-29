# Stax SR-3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 4.0; 106 1.8; 116 0.2; 128 -1.1; 141 -2.1; 155 -2.4; 170 -2.4; 187 -2.4; 206 -2.1; 227 -1.6; 249 -1.0; 274 -0.4; 302 -0.1; 332 0.4; 365 0.8; 402 1.1; 442 1.2; 486 1.2; 535 1.4; 588 0.7; 647 -1.2; 712 0.6; 783 1.8; 861 1.1; 947 0.6; 1042 -0.4; 1146 -0.6; 1261 0.2; 1387 -0.3; 1526 -0.4; 1678 0.5; 1846 -0.0; 2031 -0.6; 2234 -0.4; 2457 -0.8; 2703 -1.0; 2973 -1.7; 3270 -1.1; 3597 -1.1; 3957 -0.0; 4353 0.3; 4788 3.5; 5267 4.9; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.4; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 63 Hz   | 0.3  | 8.0 dB  |
| Peaking | 159 Hz  | 1    | -8.5 dB |
| Peaking | 454 Hz  | 2.57 | 1.0 dB  |
| Peaking | 3267 Hz | 1.65 | -2.0 dB |
| Peaking | 5714 Hz | 2.79 | 6.9 dB  |
| Peaking | 19 Hz   | 1.04 | 2.3 dB  |
| Peaking | 39 Hz   | 0.6  | -1.2 dB |
| Peaking | 86 Hz   | 5    | 2.1 dB  |
| Peaking | 797 Hz  | 8.83 | 1.6 dB  |
| Peaking | 8715 Hz | 3.38 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-3/Stax%20SR-3.png)