# AKG K702

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.4; 37 4.9; 41 4.3; 45 3.9; 49 3.4; 54 2.8; 60 2.3; 66 3.1; 72 3.3; 79 1.4; 87 0.7; 96 0.2; 106 0.0; 116 -0.4; 128 -0.8; 141 -1.1; 155 -1.1; 170 -1.2; 187 -1.4; 206 -1.4; 227 -1.4; 249 -1.4; 274 -1.4; 302 -1.2; 332 -1.1; 365 -0.9; 402 -0.8; 442 -0.7; 486 -0.3; 535 0.3; 588 1.6; 647 1.0; 712 1.1; 783 1.0; 861 0.5; 947 0.1; 1042 0.1; 1146 -0.2; 1261 -0.5; 1387 -0.6; 1526 -1.2; 1678 -1.6; 1846 -2.8; 2031 -4.0; 2234 -4.4; 2457 -4.1; 2703 -3.1; 2973 -2.2; 3270 -0.9; 3597 -0.2; 3957 -0.7; 4353 -1.5; 4788 -1.1; 5267 -3.1; 5793 -6.9; 6373 -4.6; 7010 -2.8; 7711 -3.2; 8482 -1.5; 9330 -0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.7; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.36 | 6.2 dB  |
| Peaking | 207 Hz  | 0.53 | -2.8 dB |
| Peaking | 1108 Hz | 0.22 | 1.7 dB  |
| Peaking | 2199 Hz | 1.56 | -5.8 dB |
| Peaking | 6010 Hz | 3.1  | -6.8 dB |
| Peaking | 70 Hz   | 8.24 | 1.3 dB  |
| Peaking | 621 Hz  | 1.18 | -1.6 dB |
| Peaking | 629 Hz  | 2.28 | 2.6 dB  |
| Peaking | 7509 Hz | 2.32 | 2.0 dB  |
| Peaking | 7780 Hz | 4.93 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K702/AKG%20K702.png)