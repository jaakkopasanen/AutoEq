# Shure SE846 White Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.5; 23 -3.5; 25 -3.5; 28 -3.5; 31 -3.5; 34 -3.5; 37 -3.4; 41 -3.4; 45 -3.4; 49 -3.4; 54 -3.4; 60 -3.4; 66 -3.5; 72 -3.5; 79 -3.5; 87 -3.5; 96 -3.4; 106 -3.3; 116 -3.2; 128 -3.1; 141 -3.0; 155 -2.8; 170 -2.7; 187 -2.4; 206 -2.2; 227 -1.9; 249 -1.7; 274 -1.5; 302 -1.4; 332 -1.1; 365 -0.8; 402 -0.6; 442 -0.4; 486 -0.3; 535 -0.1; 588 0.1; 647 0.3; 712 0.5; 783 0.6; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.5; 1526 -2.1; 1678 -2.6; 1846 -2.7; 2031 -2.5; 2234 -1.7; 2457 0.0; 2703 2.8; 2973 5.5; 3270 6.0; 3597 6.0; 3957 5.6; 4353 3.9; 4788 4.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.1; 8482 -0.9; 9330 -0.8; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 White Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.25 | -3.7 dB |
| Peaking | 2033 Hz | 1.73 | -4.8 dB |
| Peaking | 3236 Hz | 1.73 | 7.0 dB  |
| Peaking | 6026 Hz | 2.04 | 6.3 dB  |
| Peaking | 8044 Hz | 2.26 | -3.3 dB |
| Peaking | 27 Hz   | 0.17 | -1.0 dB |
| Peaking | 48 Hz   | 0.63 | 1.3 dB  |
| Peaking | 744 Hz  | 1.46 | 1.0 dB  |
| Peaking | 1451 Hz | 3.59 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20White%20Filter/Shure%20SE846%20White%20Filter.png)