# Teknmotion London Underground
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.7; 41 5.0; 45 4.3; 49 3.7; 54 3.0; 60 2.3; 66 1.8; 72 1.5; 79 1.2; 87 1.1; 96 0.9; 106 0.8; 116 0.9; 128 1.0; 141 1.2; 155 1.4; 170 1.8; 187 2.2; 206 2.6; 227 3.1; 249 3.5; 274 3.9; 302 4.6; 332 5.2; 365 5.9; 402 6.0; 442 6.0; 486 6.0; 535 5.7; 588 4.9; 647 3.3; 712 1.7; 783 1.0; 861 0.5; 947 0.3; 1042 -0.0; 1146 0.6; 1261 0.6; 1387 -0.5; 1526 -0.1; 1678 1.0; 1846 2.8; 2031 4.9; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Teknmotion London Underground GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teknmotion London Underground ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.82 | 6.5 dB  |
| Peaking | 335 Hz  | 1.28 | 4.8 dB  |
| Peaking | 514 Hz  | 2.77 | 4.0 dB  |
| Peaking | 2622 Hz | 1.86 | 5.6 dB  |
| Peaking | 4940 Hz | 1.57 | 6.0 dB  |
| Peaking | 948 Hz  | 3.94 | -0.9 dB |
| Peaking | 1493 Hz | 4.2  | -2.0 dB |
| Peaking | 2088 Hz | 6.44 | 1.9 dB  |
| Peaking | 6416 Hz | 4.51 | 3.6 dB  |
| Peaking | 7482 Hz | 1.77 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Teknmotion%20London%20Underground/Teknmotion%20London%20Underground.png)