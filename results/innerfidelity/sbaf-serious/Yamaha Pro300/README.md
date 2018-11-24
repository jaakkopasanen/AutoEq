# Yamaha Pro300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 5.7; 206 5.3; 227 5.0; 249 5.3; 274 5.4; 302 4.7; 332 4.4; 365 3.5; 402 3.1; 442 2.4; 486 1.6; 535 1.4; 588 3.0; 647 2.7; 712 1.9; 783 1.7; 861 1.1; 947 0.5; 1042 -0.3; 1146 -1.0; 1261 -2.0; 1387 -3.5; 1526 -4.3; 1678 -5.4; 1846 -5.4; 2031 -3.8; 2234 -1.2; 2457 1.5; 2703 3.6; 2973 5.5; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 3.8; 6373 3.7; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha Pro300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.14 | 6.0 dB  |
| Peaking | 233 Hz  | 0.7  | 2.8 dB  |
| Peaking | 684 Hz  | 2.75 | 1.6 dB  |
| Peaking | 1779 Hz | 1.7  | -8.6 dB |
| Peaking | 3596 Hz | 0.94 | 7.9 dB  |
| Peaking | 504 Hz  | 9.36 | -1.1 dB |
| Peaking | 2987 Hz | 3.19 | 1.8 dB  |
| Peaking | 3758 Hz | 1.42 | -2.9 dB |
| Peaking | 5397 Hz | 1.15 | 3.4 dB  |
| Peaking | 8111 Hz | 1.39 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro300/Yamaha%20Pro300.png)