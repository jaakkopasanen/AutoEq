# Sennheiser CXC-700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.5dB
GraphicEQ: 21 -0.3; 23 -0.8; 25 -1.2; 28 -1.6; 31 -2.0; 34 -2.3; 37 -2.5; 41 -2.7; 45 -2.8; 49 -2.9; 54 -3.1; 60 -3.4; 66 -3.6; 72 -3.7; 79 -3.7; 87 -3.9; 96 -4.2; 106 -4.5; 116 -4.9; 128 -5.2; 141 -5.4; 155 -5.4; 170 -5.3; 187 -5.2; 206 -5.0; 227 -4.6; 249 -4.1; 274 -3.5; 302 -3.0; 332 -2.5; 365 -1.8; 402 -1.1; 442 -0.3; 486 0.4; 535 1.1; 588 1.7; 647 2.3; 712 2.4; 783 2.0; 861 1.2; 947 0.4; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.6; 1526 -2.1; 1678 -2.3; 1846 -2.0; 2031 -1.7; 2234 -1.0; 2457 0.0; 2703 0.8; 2973 1.5; 3270 2.2; 3597 2.3; 3957 1.0; 4353 -1.0; 4788 -1.5; 5267 -1.6; 5793 -2.5; 6373 -3.3; 7010 -1.4; 7711 -0.5; 8482 -3.5; 9330 -6.1; 10263 -1.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CXC-700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CXC-700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 47 Hz    | 0.83 | -1.9 dB |
| Peaking | 163 Hz   | 0.61 | -5.3 dB |
| Peaking | 635 Hz   | 2.17 | 3.5 dB  |
| Peaking | 6105 Hz  | 4.36 | -3.2 dB |
| Peaking | 9269 Hz  | 5.77 | -6.6 dB |
| Peaking | 808 Hz   | 4.45 | 1.0 dB  |
| Peaking | 1733 Hz  | 1.61 | -2.7 dB |
| Peaking | 3546 Hz  | 1.79 | 3.7 dB  |
| Peaking | 4505 Hz  | 3.06 | -2.8 dB |
| Peaking | 11038 Hz | 7.32 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20CXC-700/Sennheiser%20CXC-700.png)