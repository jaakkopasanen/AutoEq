# HiFiMAN HE-400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.8; 66 5.6; 72 5.5; 79 5.3; 87 5.0; 96 4.6; 106 4.4; 116 4.2; 128 4.0; 141 3.7; 155 3.3; 170 3.1; 187 4.7; 206 4.7; 227 3.9; 249 3.6; 274 3.4; 302 3.5; 332 3.3; 365 2.5; 402 2.7; 442 5.9; 486 5.7; 535 5.0; 588 3.8; 647 3.3; 712 2.2; 783 1.3; 861 1.1; 947 0.9; 1042 0.4; 1146 1.8; 1261 2.4; 1387 4.3; 1526 5.2; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.0; 9330 -2.6; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.34 | 5.5 dB  |
| Peaking | 76 Hz   | 0.69 | 2.8 dB  |
| Peaking | 223 Hz  | 1.42 | 2.9 dB  |
| Peaking | 490 Hz  | 2.99 | 5.0 dB  |
| Peaking | 2998 Hz | 0.62 | 6.9 dB  |
| Peaking | 1035 Hz | 3.71 | -2.1 dB |
| Peaking | 1642 Hz | 2.9  | 2.0 dB  |
| Peaking | 2975 Hz | 2.15 | -1.2 dB |
| Peaking | 5922 Hz | 2.5  | 3.2 dB  |
| Peaking | 8841 Hz | 2.57 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-400/HiFiMAN%20HE-400.png)