# HyperX Cloud Alpha

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.6; 23 -1.7; 25 -1.8; 28 -2.0; 31 -2.1; 34 -2.2; 37 -2.2; 41 -2.2; 45 -2.2; 49 -2.2; 54 -2.1; 60 -2.0; 66 -2.0; 72 -2.0; 79 -2.0; 87 -2.1; 96 -2.4; 106 -2.7; 116 -2.9; 128 -3.1; 141 -3.2; 155 -3.2; 170 -3.2; 187 -3.0; 206 -2.9; 227 -2.8; 249 -2.5; 274 -2.4; 302 -2.4; 332 -2.3; 365 -1.8; 402 -1.3; 442 -0.9; 486 -0.6; 535 -0.2; 588 0.1; 647 0.5; 712 0.6; 783 0.4; 861 0.1; 947 0.0; 1042 0.1; 1146 -0.1; 1261 -0.4; 1387 -1.4; 1526 -2.5; 1678 -3.3; 1846 -3.6; 2031 -3.3; 2234 -2.4; 2457 -1.3; 2703 -0.5; 2973 0.5; 3270 1.6; 3597 3.5; 3957 4.8; 4353 5.6; 4788 6.0; 5267 6.0; 5793 5.4; 6373 4.0; 7010 2.5; 7711 -0.8; 8482 -4.2; 9330 -5.4; 10263 -2.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Alpha GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Alpha ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.5  | -2.0 dB |
| Peaking | 175 Hz  | 0.78 | -3.1 dB |
| Peaking | 1973 Hz | 1.87 | -4.7 dB |
| Peaking | 5111 Hz | 1.12 | 7.0 dB  |
| Peaking | 8947 Hz | 3.05 | -7.9 dB |
| Peaking | 339 Hz  | 2.25 | -1.1 dB |
| Peaking | 682 Hz  | 4.24 | 0.6 dB  |
| Peaking | 978 Hz  | 0.32 | 0.7 dB  |
| Peaking | 1579 Hz | 4.41 | -1.3 dB |
| Peaking | 2912 Hz | 3.72 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/HyperX%20Cloud%20Alpha/HyperX%20Cloud%20Alpha.png)