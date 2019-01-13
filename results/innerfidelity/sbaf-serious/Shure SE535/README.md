# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.4; 28 4.2; 31 4.1; 34 4.0; 37 3.8; 41 3.6; 45 3.5; 49 3.3; 54 3.0; 60 2.6; 66 2.2; 72 1.9; 79 1.5; 87 1.1; 96 0.7; 106 0.4; 116 0.1; 128 -0.2; 141 -0.6; 155 -0.8; 170 -1.0; 187 -1.1; 206 -1.3; 227 -1.4; 249 -1.4; 274 -1.3; 302 -1.3; 332 -1.2; 365 -1.1; 402 -0.9; 442 -0.7; 486 -0.6; 535 -0.5; 588 0.0; 647 0.1; 712 0.2; 783 0.4; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.3; 1387 -0.7; 1526 -0.9; 1678 -0.9; 1846 -0.7; 2031 -0.4; 2234 0.2; 2457 2.1; 2703 3.7; 2973 5.5; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.65 | 4.2 dB  |
| Peaking | 51 Hz   | 0.94 | 1.8 dB  |
| Peaking | 225 Hz  | 0.8  | -1.7 dB |
| Peaking | 1869 Hz | 1.81 | -3.0 dB |
| Peaking | 3972 Hz | 0.96 | 7.2 dB  |
| Peaking | 778 Hz  | 3.94 | 0.6 dB  |
| Peaking | 3067 Hz | 3.85 | 2.2 dB  |
| Peaking | 3600 Hz | 1.43 | -1.4 dB |
| Peaking | 6247 Hz | 2.49 | 5.1 dB  |
| Peaking | 7447 Hz | 1.56 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE535/Shure%20SE535.png)