# Westone W10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.6; 28 5.2; 31 4.7; 34 4.4; 37 4.1; 41 3.7; 45 3.3; 49 3.0; 54 2.6; 60 2.2; 66 1.8; 72 1.3; 79 0.9; 87 0.4; 96 -0.2; 106 -0.4; 116 -0.8; 128 -1.1; 141 -1.5; 155 -1.7; 170 -1.8; 187 -1.9; 206 -2.1; 227 -2.0; 249 -2.2; 274 -2.0; 302 -2.0; 332 -1.8; 365 -1.8; 402 -1.8; 442 -1.4; 486 -1.3; 535 -1.0; 588 -0.4; 647 -0.2; 712 -0.2; 783 0.2; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.0; 1261 0.0; 1387 -0.1; 1526 -0.0; 1678 0.3; 1846 1.1; 2031 2.3; 2234 3.3; 2457 4.6; 2703 5.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.65 | 5.7 dB  |
| Peaking | 55 Hz   | 0.76 | 1.6 dB  |
| Peaking | 206 Hz  | 0.45 | -2.4 dB |
| Peaking | 3941 Hz | 0.95 | 7.0 dB  |
| Peaking | 1612 Hz | 2.64 | -1.5 dB |
| Peaking | 2662 Hz | 2.12 | 1.7 dB  |
| Peaking | 3869 Hz | 2.61 | -1.4 dB |
| Peaking | 6352 Hz | 2.56 | 5.1 dB  |
| Peaking | 7301 Hz | 1.55 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W10/Westone%20W10.png)