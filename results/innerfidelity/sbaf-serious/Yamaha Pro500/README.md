# Yamaha Pro500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.4; 31 4.9; 34 4.5; 37 4.1; 41 3.7; 45 3.3; 49 3.0; 54 2.6; 60 2.2; 66 2.1; 72 2.7; 79 1.9; 87 0.9; 96 1.1; 106 0.4; 116 -0.5; 128 -1.1; 141 -1.5; 155 -1.8; 170 -1.5; 187 -2.0; 206 -2.1; 227 -1.8; 249 -1.2; 274 -0.4; 302 0.3; 332 1.8; 365 3.0; 402 4.0; 442 4.8; 486 4.2; 535 4.1; 588 3.4; 647 2.8; 712 1.9; 783 1.3; 861 0.5; 947 0.7; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -1.3; 1526 -1.6; 1678 -1.4; 1846 -0.3; 2031 1.0; 2234 2.3; 2457 4.1; 2703 5.6; 2973 6.0; 3270 4.8; 3597 3.4; 3957 4.4; 4353 5.4; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha Pro500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.03 | 6.2 dB  |
| Peaking | 72 Hz   | 4.86 | 1.8 dB  |
| Peaking | 480 Hz  | 2.34 | 5.1 dB  |
| Peaking | 2864 Hz | 3.42 | 5.7 dB  |
| Peaking | 5206 Hz | 1.96 | 6.6 dB  |
| Peaking | 192 Hz  | 0.89 | -5.6 dB |
| Peaking | 215 Hz  | 0.46 | 3.1 dB  |
| Peaking | 1630 Hz | 1.91 | -3.4 dB |
| Peaking | 2104 Hz | 1.66 | 1.7 dB  |
| Peaking | 8371 Hz | 4.36 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro500/Yamaha%20Pro500.png)