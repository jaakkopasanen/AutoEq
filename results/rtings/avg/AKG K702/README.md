# AKG K702

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.4; 28 4.8; 31 4.2; 34 3.7; 37 3.3; 41 2.9; 45 2.5; 49 2.2; 54 1.8; 60 1.4; 66 1.0; 72 0.5; 79 0.1; 87 -0.3; 96 -0.8; 106 -1.3; 116 -1.7; 128 -2.1; 141 -2.4; 155 -2.6; 170 -2.7; 187 -2.7; 206 -2.7; 227 -2.7; 249 -2.6; 274 -2.6; 302 -2.6; 332 -2.5; 365 -2.4; 402 -2.3; 442 -2.3; 486 -2.2; 535 -1.8; 588 -1.3; 647 -0.8; 712 -0.6; 783 -0.2; 861 -0.0; 947 0.0; 1042 0.0; 1146 -0.1; 1261 -0.2; 1387 -0.9; 1526 -1.7; 1678 -3.2; 1846 -4.9; 2031 -6.7; 2234 -7.7; 2457 -7.1; 2703 -6.3; 2973 -4.9; 3270 -3.7; 3597 -3.6; 3957 -3.7; 4353 -3.2; 4788 -2.7; 5267 -3.4; 5793 -5.0; 6373 -7.4; 7010 -6.8; 7711 -6.2; 8482 -5.6; 9330 -2.0; 10263 0.0; 11289 -0.8; 12418 -2.1; 13660 -0.0; 15026 0.0; 16529 -3.4; 18182 -9.6; 20000 -8.4
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

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.39 | 6.6 dB   |
| Peaking | 202 Hz   | 0.57 | -3.2 dB  |
| Peaking | 2354 Hz  | 1.92 | -7.7 dB  |
| Peaking | 6839 Hz  | 1.96 | -7.2 dB  |
| Peaking | 18797 Hz | 1.9  | -11.5 dB |
| Peaking | 1062 Hz  | 0.57 | -2.3 dB  |
| Peaking | 1062 Hz  | 1    | 3.6 dB   |
| Peaking | 8526 Hz  | 7.63 | -2.3 dB  |
| Peaking | 10022 Hz | 5.25 | 2.5 dB   |
| Peaking | 15069 Hz | 4.23 | 2.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K702/AKG%20K702.png)