# Dunu DN2000J

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 0.0; 23 0.7; 25 0.2; 28 -0.3; 31 -0.8; 34 -1.2; 37 -1.5; 41 -1.8; 45 -2.2; 49 -2.5; 54 -2.8; 60 -3.1; 66 -3.5; 72 -3.8; 79 -4.2; 87 -4.5; 96 -4.8; 106 -5.0; 116 -5.1; 128 -5.2; 141 -5.3; 155 -5.3; 170 -5.1; 187 -5.0; 206 -4.8; 227 -4.5; 249 -4.2; 274 -3.8; 302 -3.5; 332 -3.1; 365 -2.7; 402 -2.3; 442 -1.8; 486 -1.5; 535 -1.2; 588 -0.6; 647 -0.3; 712 -0.1; 783 0.3; 861 0.3; 947 0.1; 1042 -0.0; 1146 -0.3; 1261 -0.4; 1387 -1.0; 1526 -1.9; 1678 -2.2; 1846 -2.1; 2031 -1.9; 2234 -1.6; 2457 -1.0; 2703 -0.9; 2973 -0.4; 3270 0.7; 3597 2.6; 3957 2.5; 4353 -1.8; 4788 -6.1; 5267 -6.7; 5793 -9.1; 6373 -8.4; 7010 -6.3; 7711 -6.8; 8482 -7.2; 9330 -5.5; 10263 -1.4; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.6; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN2000J GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2000J ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 105 Hz   | 0.63 | -4.4 dB |
| Peaking | 236 Hz   | 0.89 | -2.5 dB |
| Peaking | 5821 Hz  | 3.4  | -8.4 dB |
| Peaking | 8596 Hz  | 2.04 | -7.3 dB |
| Peaking | 10829 Hz | 2.72 | 3.0 dB  |
| Peaking | 19 Hz    | 2.14 | 1.9 dB  |
| Peaking | 890 Hz   | 1.66 | 1.1 dB  |
| Peaking | 1811 Hz  | 1.57 | -2.2 dB |
| Peaking | 3813 Hz  | 3.88 | 5.1 dB  |
| Peaking | 4692 Hz  | 7.05 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN2000J/Dunu%20DN2000J.png)