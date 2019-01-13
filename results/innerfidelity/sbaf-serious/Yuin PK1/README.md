# Yuin PK1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.7; 72 4.7; 79 3.8; 87 2.9; 96 2.3; 106 2.2; 116 2.0; 128 1.9; 141 1.8; 155 1.8; 170 1.9; 187 1.7; 206 1.9; 227 1.8; 249 1.8; 274 1.7; 302 1.6; 332 1.6; 365 1.6; 402 1.4; 442 1.7; 486 1.3; 535 1.0; 588 1.3; 647 1.1; 712 0.7; 783 0.7; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.9; 1387 -1.8; 1526 -2.4; 1678 -3.0; 1846 -2.9; 2031 -2.1; 2234 -1.1; 2457 0.5; 2703 1.3; 2973 3.3; 3270 4.3; 3597 4.8; 3957 3.6; 4353 1.0; 4788 -0.5; 5267 -0.6; 5793 -1.8; 6373 -1.0; 7010 -0.2; 7711 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin PK1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.5  | 6.6 dB  |
| Peaking | 392 Hz  | 0.6  | 1.5 dB  |
| Peaking | 1765 Hz | 1.79 | -3.9 dB |
| Peaking | 3490 Hz | 2.01 | 6.0 dB  |
| Peaking | 5245 Hz | 1.97 | -2.6 dB |
| Peaking | 36 Hz   | 2.45 | -0.6 dB |
| Peaking | 62 Hz   | 2.81 | 1.4 dB  |
| Peaking | 96 Hz   | 2.65 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yuin%20PK1/Yuin%20PK1.png)