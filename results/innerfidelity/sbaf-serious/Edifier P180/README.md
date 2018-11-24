# Edifier P180

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.1; 54 3.5; 60 1.6; 66 -0.1; 72 -1.6; 79 -3.2; 87 -4.8; 96 -6.1; 106 -6.8; 116 -7.1; 128 -6.9; 141 -6.7; 155 -6.3; 170 -5.7; 187 -5.2; 206 -4.8; 227 -4.1; 249 -3.8; 274 -3.5; 302 -3.1; 332 -2.9; 365 -2.8; 402 -2.0; 442 -1.7; 486 -1.0; 535 -0.7; 588 -0.0; 647 0.0; 712 0.1; 783 0.3; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.9; 1261 -2.4; 1387 -4.9; 1526 -8.1; 1678 -11.1; 1846 -13.6; 2031 -15.1; 2234 -15.1; 2457 -13.1; 2703 -10.8; 2973 -7.3; 3270 -4.2; 3597 -2.4; 3957 -2.8; 4353 -4.9; 4788 -6.4; 5267 -7.4; 5793 -9.7; 6373 -10.6; 7010 -9.3; 7711 -9.1; 8482 -8.7; 9330 -6.4; 10263 -2.7; 11289 -0.0; 12418 0.0; 13660 -0.2; 15026 -2.1; 16529 -0.5; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Edifier P180 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Edifier P180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.55 | 9.4 dB   |
| Peaking | 109 Hz   | 0.69 | -10.5 dB |
| Peaking | 2104 Hz  | 2.12 | -16.3 dB |
| Peaking | 6841 Hz  | 1.52 | -10.4 dB |
| Peaking | 13999 Hz | 3.57 | -0.7 dB  |
| Peaking | 1040 Hz  | 0.63 | 5.9 dB   |
| Peaking | 1331 Hz  | 0.27 | -3.6 dB  |
| Peaking | 1600 Hz  | 4.51 | -3.6 dB  |
| Peaking | 3681 Hz  | 4.15 | 4.4 dB   |
| Peaking | 11819 Hz | 3.53 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Edifier%20P180/Edifier%20P180.png)