# Sennheiser Game One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.5; 45 5.0; 49 4.6; 54 4.1; 60 3.5; 66 2.9; 72 2.4; 79 1.9; 87 1.3; 96 0.7; 106 0.2; 116 -0.3; 128 -0.8; 141 -1.1; 155 -1.3; 170 -1.4; 187 -1.4; 206 -1.3; 227 -1.1; 249 -1.1; 274 -1.1; 302 -1.1; 332 -1.1; 365 -1.0; 402 -1.0; 442 -1.1; 486 -1.1; 535 -0.9; 588 -0.8; 647 -0.6; 712 -0.1; 783 0.1; 861 0.1; 947 0.1; 1042 -0.0; 1146 0.1; 1261 -0.2; 1387 -0.3; 1526 0.1; 1678 -0.2; 1846 -0.5; 2031 -1.3; 2234 -1.6; 2457 -1.1; 2703 -0.5; 2973 0.1; 3270 0.8; 3597 1.9; 3957 3.7; 4353 2.7; 4788 1.7; 5267 4.0; 5793 4.1; 6373 1.4; 7010 0.4; 7711 0.3; 8482 -0.6; 9330 -1.2; 10263 -0.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Game One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Game One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.34 | 6.8 dB  |
| Peaking | 128 Hz  | 0.48 | -3.3 dB |
| Peaking | 3945 Hz | 3.09 | 5.3 dB  |
| Peaking | 4219 Hz | 0.76 | -2.3 dB |
| Peaking | 5576 Hz | 3.71 | 5.7 dB  |
| Peaking | 535 Hz  | 1.52 | -1.6 dB |
| Peaking | 611 Hz  | 0.87 | 1.2 dB  |
| Peaking | 1723 Hz | 3.19 | 0.6 dB  |
| Peaking | 2170 Hz | 3.42 | -1.2 dB |
| Peaking | 2925 Hz | 6    | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20Game%20One/Sennheiser%20Game%20One.png)