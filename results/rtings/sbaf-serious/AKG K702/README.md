# AKG K702

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.6; 28 4.9; 31 4.3; 34 3.7; 37 3.2; 41 2.7; 45 2.2; 49 1.9; 54 1.5; 60 1.1; 66 0.8; 72 0.5; 79 0.3; 87 0.0; 96 -0.3; 106 -0.8; 116 -1.2; 128 -1.6; 141 -1.8; 155 -2.0; 170 -2.1; 187 -2.2; 206 -2.2; 227 -2.2; 249 -2.0; 274 -1.9; 302 -1.8; 332 -1.6; 365 -1.4; 402 -1.3; 442 -1.2; 486 -1.0; 535 -0.6; 588 -0.2; 647 0.3; 712 0.3; 783 0.2; 861 0.1; 947 0.0; 1042 0.1; 1146 0.1; 1261 0.0; 1387 -0.9; 1526 -2.1; 1678 -3.5; 1846 -4.9; 2031 -6.3; 2234 -7.3; 2457 -6.7; 2703 -5.4; 2973 -3.3; 3270 -1.1; 3597 -0.4; 3957 -1.3; 4353 -1.9; 4788 -1.1; 5267 -0.5; 5793 -1.1; 6373 -3.6; 7010 -3.7; 7711 -4.6; 8482 -6.1; 9330 -3.1; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.0; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.68 | 6.1 dB  |
| Peaking | 190 Hz   | 0.82 | -2.5 dB |
| Peaking | 2253 Hz  | 2.29 | -7.7 dB |
| Peaking | 6689 Hz  | 4.54 | -3.0 dB |
| Peaking | 8412 Hz  | 4.77 | -6.1 dB |
| Peaking | 1136 Hz  | 1.48 | 1.1 dB  |
| Peaking | 1698 Hz  | 4.07 | -1.3 dB |
| Peaking | 3454 Hz  | 9.93 | 1.3 dB  |
| Peaking | 10389 Hz | 6.32 | 1.2 dB  |
| Peaking | 18837 Hz | 3.29 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/AKG%20K702/AKG%20K702.png)