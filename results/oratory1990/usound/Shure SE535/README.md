# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 0.0; 23 4.3; 25 4.2; 28 4.1; 31 4.0; 34 3.8; 37 3.7; 41 3.5; 45 3.4; 49 3.2; 54 3.0; 60 2.6; 66 2.3; 72 1.9; 79 1.5; 87 1.0; 96 0.6; 106 0.1; 116 -0.3; 128 -0.7; 141 -1.1; 155 -1.3; 170 -1.6; 187 -1.8; 206 -1.9; 227 -2.0; 249 -2.1; 274 -2.1; 302 -2.1; 332 -2.1; 365 -2.0; 402 -2.0; 442 -1.9; 486 -1.7; 535 -1.5; 588 -1.3; 647 -1.0; 712 -0.7; 783 -0.3; 861 -0.1; 947 0.0; 1042 -0.0; 1146 -0.2; 1261 -0.2; 1387 -0.0; 1526 0.4; 1678 1.0; 1846 1.5; 2031 2.0; 2234 2.6; 2457 3.4; 2703 3.7; 2973 3.3; 3270 3.1; 3597 3.8; 3957 4.8; 4353 5.5; 4788 5.4; 5267 4.8; 5793 4.0; 6373 3.4; 7010 0.7; 7711 -0.8; 8482 -1.2; 9330 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.49 | 4.1 dB  |
| Peaking | 58 Hz   | 0.92 | 1.6 dB  |
| Peaking | 255 Hz  | 0.51 | -2.4 dB |
| Peaking | 2587 Hz | 1.69 | 3.0 dB  |
| Peaking | 4714 Hz | 2.05 | 5.5 dB  |
| Peaking | 887 Hz  | 4.21 | 0.5 dB  |
| Peaking | 1307 Hz | 4.91 | -0.5 dB |
| Peaking | 6270 Hz | 5.28 | 2.0 dB  |
| Peaking | 7873 Hz | 3.1  | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Shure%20SE535/Shure%20SE535.png)