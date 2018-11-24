# Audeze LCD-3 sn2312454

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 3.1; 25 3.1; 28 3.1; 31 3.0; 34 2.7; 37 2.6; 41 2.6; 45 2.8; 49 2.5; 54 1.3; 60 1.0; 66 1.0; 72 0.8; 79 0.7; 87 0.3; 96 -0.0; 106 -0.3; 116 -0.4; 128 -0.7; 141 -1.0; 155 -1.1; 170 -1.3; 187 -1.5; 206 -1.6; 227 -1.6; 249 -1.7; 274 -1.7; 302 -1.9; 332 -2.0; 365 -1.9; 402 -1.8; 442 -1.6; 486 -1.5; 535 -1.5; 588 -1.4; 647 -1.7; 712 -1.8; 783 -1.4; 861 -1.1; 947 -0.2; 1042 0.2; 1146 0.3; 1261 0.7; 1387 0.3; 1526 -0.0; 1678 0.2; 1846 0.9; 2031 1.2; 2234 0.9; 2457 1.1; 2703 0.8; 2973 1.0; 3270 1.5; 3597 2.5; 3957 2.5; 4353 3.3; 4788 5.4; 5267 5.1; 5793 4.6; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.2; 16529 -3.0; 18182 -6.6; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2312454 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312454 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.65 | 3.2 dB  |
| Peaking | 267 Hz   | 0.64 | -2.0 dB |
| Peaking | 691 Hz   | 3.56 | -1.3 dB |
| Peaking | 5252 Hz  | 1.62 | 5.6 dB  |
| Peaking | 18517 Hz | 1.79 | -7.3 dB |
| Peaking | 1982 Hz  | 1.94 | 0.7 dB  |
| Peaking | 5632 Hz  | 7.78 | -2.0 dB |
| Peaking | 6416 Hz  | 3.81 | 3.5 dB  |
| Peaking | 7498 Hz  | 2.38 | -2.4 dB |
| Peaking | 14616 Hz | 3.86 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312454/Audeze%20LCD-3%20sn2312454.png)