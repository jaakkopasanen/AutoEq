# HiFiMAN HE1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 0.0; 23 3.4; 25 3.3; 28 3.1; 31 2.9; 34 2.7; 37 2.5; 41 2.3; 45 2.1; 49 2.0; 54 1.8; 60 1.5; 66 1.3; 72 1.2; 79 1.0; 87 0.6; 96 0.3; 106 0.1; 116 -0.2; 128 -0.5; 141 -0.5; 155 -0.8; 170 -1.1; 187 -1.5; 206 -0.2; 227 -0.1; 249 -0.8; 274 -1.2; 302 -1.7; 332 -2.4; 365 -1.4; 402 1.8; 442 0.6; 486 0.1; 535 -1.0; 588 0.7; 647 0.9; 712 -0.7; 783 0.4; 861 -0.1; 947 0.2; 1042 -0.2; 1146 -0.1; 1261 2.4; 1387 2.1; 1526 2.4; 1678 2.6; 1846 2.9; 2031 4.0; 2234 3.6; 2457 4.1; 2703 4.0; 2973 2.6; 3270 1.0; 3597 1.9; 3957 1.8; 4353 1.1; 4788 -3.8; 5267 -3.2; 5793 0.6; 6373 -3.1; 7010 -4.8; 7711 -3.8; 8482 -3.6; 9330 -1.8; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.23 | 3.7 dB  |
| Peaking | 202 Hz  | 0.62 | -1.3 dB |
| Peaking | 2333 Hz | 1.01 | 4.0 dB  |
| Peaking | 4924 Hz | 8.28 | -5.1 dB |
| Peaking | 7410 Hz | 2.69 | -5.2 dB |
| Peaking | 341 Hz  | 5.28 | -2.3 dB |
| Peaking | 405 Hz  | 6.72 | 2.9 dB  |
| Peaking | 1071 Hz | 8.22 | -1.5 dB |
| Peaking | 3289 Hz | 5.35 | -3.1 dB |
| Peaking | 3505 Hz | 2.38 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE1000/HiFiMAN%20HE1000.png)