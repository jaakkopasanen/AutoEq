# Yamaha Pro400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.4; 25 0.9; 28 0.3; 31 -0.1; 34 -0.3; 37 -0.6; 41 -0.8; 45 -0.9; 49 -1.1; 54 -1.3; 60 -1.4; 66 -0.5; 72 2.0; 79 0.3; 87 -2.6; 96 -3.0; 106 0.1; 116 -2.6; 128 -4.1; 141 -4.7; 155 -4.5; 170 -2.9; 187 -3.3; 206 -1.3; 227 1.8; 249 5.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 5.8; 442 5.1; 486 3.6; 535 2.9; 588 2.1; 647 1.1; 712 0.1; 783 -0.2; 861 -0.5; 947 -0.3; 1042 0.2; 1146 0.7; 1261 1.1; 1387 1.0; 1526 0.6; 1678 0.7; 1846 1.6; 2031 2.8; 2234 3.7; 2457 4.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 4.9; 3957 4.9; 4353 5.8; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha Pro400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 2.72 | 2.1 dB  |
| Peaking | 163 Hz  | 1.28 | -7.0 dB |
| Peaking | 303 Hz  | 1.21 | 8.7 dB  |
| Peaking | 2896 Hz | 1.83 | 5.7 dB  |
| Peaking | 5308 Hz | 2.06 | 5.9 dB  |
| Peaking | 65 Hz   | 1.75 | -1.9 dB |
| Peaking | 73 Hz   | 6.74 | 4.8 dB  |
| Peaking | 446 Hz  | 4.47 | 1.3 dB  |
| Peaking | 823 Hz  | 2.79 | -1.6 dB |
| Peaking | 8356 Hz | 4.31 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro400/Yamaha%20Pro400.png)