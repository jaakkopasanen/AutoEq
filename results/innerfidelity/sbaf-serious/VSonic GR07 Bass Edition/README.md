# VSonic GR07 Bass Edition
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 0.3; 25 0.0; 28 -0.3; 31 -0.5; 34 -0.8; 37 -0.9; 41 -1.1; 45 -1.3; 49 -1.5; 54 -1.6; 60 -1.9; 66 -2.2; 72 -2.3; 79 -2.6; 87 -2.8; 96 -3.1; 106 -3.2; 116 -3.2; 128 -3.3; 141 -3.3; 155 -3.2; 170 -3.1; 187 -3.0; 206 -2.8; 227 -2.6; 249 -2.4; 274 -2.1; 302 -1.9; 332 -1.6; 365 -1.4; 402 -1.1; 442 -0.7; 486 -0.6; 535 -0.4; 588 0.0; 647 0.2; 712 0.2; 783 0.5; 861 0.3; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.4; 1387 -0.7; 1526 -1.1; 1678 -1.3; 1846 -1.1; 2031 -0.9; 2234 -0.3; 2457 0.9; 2703 1.5; 2973 2.3; 3270 3.8; 3597 4.8; 3957 4.2; 4353 1.7; 4788 -0.3; 5267 -2.4; 5793 -3.4; 6373 0.2; 7010 2.2; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 Bass Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 Bass Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 109 Hz  | 0.64 | -3.0 dB |
| Peaking | 230 Hz  | 1.12 | -1.3 dB |
| Peaking | 3654 Hz | 3.05 | 5.7 dB  |
| Peaking | 5662 Hz | 3.46 | -4.8 dB |
| Peaking | 6765 Hz | 5.65 | 3.7 dB  |
| Peaking | 12 Hz   | 1.62 | 0.8 dB  |
| Peaking | 788 Hz  | 2.03 | 0.8 dB  |
| Peaking | 1866 Hz | 1.58 | -1.8 dB |
| Peaking | 2621 Hz | 2.61 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR07%20Bass%20Edition/VSonic%20GR07%20Bass%20Edition.png)