# Shure SE112
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.9; 23 -2.9; 25 -3.0; 28 -3.1; 31 -3.2; 34 -3.3; 37 -3.4; 41 -3.5; 45 -3.6; 49 -3.8; 54 -4.0; 60 -4.2; 66 -4.5; 72 -4.7; 79 -5.0; 87 -5.3; 96 -5.7; 106 -6.0; 116 -6.2; 128 -6.4; 141 -6.5; 155 -6.5; 170 -6.5; 187 -6.4; 206 -6.2; 227 -5.9; 249 -5.6; 274 -5.3; 302 -4.9; 332 -4.5; 365 -4.0; 402 -3.6; 442 -3.1; 486 -2.6; 535 -2.1; 588 -1.6; 647 -1.1; 712 -0.6; 783 -0.2; 861 0.1; 947 0.1; 1042 0.0; 1146 -0.4; 1261 -0.9; 1387 -1.2; 1526 -1.3; 1678 -1.4; 1846 -1.4; 2031 -1.5; 2234 -1.4; 2457 -0.5; 2703 0.8; 2973 1.8; 3270 2.3; 3597 1.7; 3957 -0.2; 4353 -4.3; 4788 -4.1; 5267 2.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE112 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE112 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.23 | -2.9 dB |
| Peaking | 141 Hz  | 0.73 | -3.7 dB |
| Peaking | 287 Hz  | 0.89 | -2.9 dB |
| Peaking | 4639 Hz | 6.94 | -8.0 dB |
| Peaking | 5891 Hz | 3.26 | 7.1 dB  |
| Peaking | 896 Hz  | 2.24 | 1.3 dB  |
| Peaking | 2286 Hz | 1.02 | -3.0 dB |
| Peaking | 3137 Hz | 1.63 | 4.3 dB  |
| Peaking | 4218 Hz | 8.14 | -2.5 dB |
| Peaking | 8060 Hz | 4.24 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Shure%20SE112/Shure%20SE112.png)