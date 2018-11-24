# JVC HA-S500-Z

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.6; 25 3.9; 28 3.0; 31 2.2; 34 1.6; 37 1.1; 41 0.7; 45 0.3; 49 0.1; 54 -0.1; 60 -0.3; 66 -0.5; 72 -0.7; 79 -1.0; 87 -1.2; 96 -1.4; 106 -1.4; 116 -1.5; 128 -1.8; 141 -2.1; 155 -2.3; 170 -2.1; 187 -2.1; 206 -2.2; 227 -2.1; 249 -2.1; 274 -2.9; 302 -3.2; 332 -2.4; 365 -1.4; 402 -0.1; 442 1.5; 486 3.2; 535 4.7; 588 4.4; 647 3.0; 712 1.7; 783 1.2; 861 0.5; 947 0.1; 1042 -0.0; 1146 0.1; 1261 0.1; 1387 0.2; 1526 0.6; 1678 1.3; 1846 2.4; 2031 3.8; 2234 5.3; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.6; 4788 5.4; 5267 6.0; 5793 6.0; 6373 5.5; 7010 1.3; 7711 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-S500-Z GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-S500-Z ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.24 | 5.8 dB  |
| Peaking | 312 Hz  | 3.49 | -1.7 dB |
| Peaking | 460 Hz  | 0.21 | -3.1 dB |
| Peaking | 552 Hz  | 1.77 | 7.5 dB  |
| Peaking | 3288 Hz | 0.74 | 7.6 dB  |
| Peaking | 1575 Hz | 3.45 | -0.8 dB |
| Peaking | 2329 Hz | 3.76 | 1.6 dB  |
| Peaking | 3329 Hz | 2.22 | -1.0 dB |
| Peaking | 6201 Hz | 2.55 | 6.5 dB  |
| Peaking | 7207 Hz | 1.72 | -5.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20HA-S500-Z/JVC%20HA-S500-Z.png)