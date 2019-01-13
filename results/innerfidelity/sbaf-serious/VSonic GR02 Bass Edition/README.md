# VSonic GR02 Bass Edition
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.4; 23 -5.4; 25 -5.4; 28 -5.3; 31 -5.3; 34 -5.2; 37 -5.2; 41 -5.2; 45 -5.1; 49 -5.1; 54 -5.1; 60 -5.1; 66 -5.2; 72 -5.2; 79 -5.3; 87 -5.4; 96 -5.4; 106 -5.3; 116 -5.1; 128 -5.0; 141 -4.9; 155 -4.7; 170 -4.4; 187 -4.1; 206 -3.7; 227 -3.3; 249 -2.9; 274 -2.5; 302 -2.1; 332 -1.7; 365 -1.3; 402 -1.0; 442 -0.5; 486 -0.4; 535 -0.0; 588 0.5; 647 0.6; 712 0.6; 783 0.7; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -0.9; 1526 -1.2; 1678 -1.2; 1846 -0.5; 2031 0.8; 2234 2.3; 2457 4.4; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.1; 4788 3.2; 5267 3.7; 5793 3.0; 6373 0.7; 7010 0.8; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR02 Bass Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR02 Bass Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.38 | -4.8 dB |
| Peaking | 122 Hz  | 0.48 | -4.4 dB |
| Peaking | 656 Hz  | 1.19 | 1.3 dB  |
| Peaking | 1702 Hz | 1.46 | -3.7 dB |
| Peaking | 3116 Hz | 1.09 | 7.4 dB  |
| Peaking | 3298 Hz | 4.31 | -2.3 dB |
| Peaking | 3559 Hz | 1.6  | 3.1 dB  |
| Peaking | 4945 Hz | 0.86 | -2.2 dB |
| Peaking | 5516 Hz | 5.47 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR02%20Bass%20Edition/VSonic%20GR02%20Bass%20Edition.png)