# Shure SE846 Black Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -6.4; 23 -6.5; 25 -6.5; 28 -6.4; 31 -6.4; 34 -6.3; 37 -6.3; 41 -6.2; 45 -6.2; 49 -6.2; 54 -6.1; 60 -6.1; 66 -6.1; 72 -6.1; 79 -6.1; 87 -6.0; 96 -5.9; 106 -5.7; 116 -5.5; 128 -5.4; 141 -5.3; 155 -5.0; 170 -4.8; 187 -4.5; 206 -4.2; 227 -3.9; 249 -3.6; 274 -3.2; 302 -2.9; 332 -2.5; 365 -2.1; 402 -1.8; 442 -1.5; 486 -1.2; 535 -0.9; 588 -0.6; 647 -0.2; 712 0.0; 783 0.2; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.3; 1261 -0.5; 1387 -0.8; 1526 -1.1; 1678 -1.1; 1846 -0.7; 2031 -0.2; 2234 0.6; 2457 2.0; 2703 4.2; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Black Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.32 | -5.9 dB |
| Peaking | 136 Hz  | 0.49 | -4.2 dB |
| Peaking | 1831 Hz | 1.85 | -3.2 dB |
| Peaking | 3894 Hz | 0.92 | 7.2 dB  |
| Peaking | 771 Hz  | 3.1  | 0.8 dB  |
| Peaking | 2970 Hz | 4.79 | 2.4 dB  |
| Peaking | 3439 Hz | 1.22 | -1.2 dB |
| Peaking | 6203 Hz | 2.44 | 5.1 dB  |
| Peaking | 7511 Hz | 1.55 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20Black%20Filter/Shure%20SE846%20Black%20Filter.png)