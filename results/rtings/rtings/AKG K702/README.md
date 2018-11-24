# AKG K702

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.4; 28 4.8; 31 4.2; 34 3.7; 37 3.3; 41 2.9; 45 2.5; 49 2.2; 54 1.8; 60 1.4; 66 1.0; 72 0.5; 79 0.1; 87 -0.3; 96 -0.8; 106 -1.3; 116 -1.7; 128 -2.1; 141 -2.4; 155 -2.6; 170 -2.7; 187 -2.7; 206 -2.7; 227 -2.7; 249 -2.6; 274 -2.6; 302 -2.6; 332 -2.5; 365 -2.4; 402 -2.3; 442 -2.3; 486 -2.2; 535 -1.8; 588 -1.3; 647 -0.8; 712 -0.6; 783 -0.2; 861 -0.0; 947 0.0; 1042 0.0; 1146 -0.1; 1261 -0.2; 1387 -0.9; 1526 -1.7; 1678 -3.2; 1846 -4.9; 2031 -6.7; 2234 -7.8; 2457 -7.1; 2703 -6.0; 2973 -4.4; 3270 -3.0; 3597 -2.5; 3957 -2.5; 4353 -1.9; 4788 -0.9; 5267 -0.9; 5793 -2.6; 6373 -6.2; 7010 -6.2; 7711 -5.8; 8482 -6.5; 9330 -4.6; 10263 -0.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.8; 18182 -5.3; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.38 | 6.6 dB  |
| Peaking | 201 Hz   | 0.56 | -3.2 dB |
| Peaking | 2314 Hz  | 2.14 | -8.0 dB |
| Peaking | 7582 Hz  | 2.09 | -6.8 dB |
| Peaking | 18681 Hz | 2.6  | -6.1 dB |
| Peaking | 1082 Hz  | 1.3  | 1.8 dB  |
| Peaking | 5130 Hz  | 6.37 | 2.0 dB  |
| Peaking | 6961 Hz  | 0.05 | -0.8 dB |
| Peaking | 9036 Hz  | 7.39 | -2.8 dB |
| Peaking | 11803 Hz | 0.89 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/AKG%20K702/AKG%20K702.png)