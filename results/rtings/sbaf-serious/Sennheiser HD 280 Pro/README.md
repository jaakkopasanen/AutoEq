# Sennheiser HD 280 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.9; 23 -1.3; 25 -1.7; 28 -2.3; 31 -2.7; 34 -3.0; 37 -3.1; 41 -3.1; 45 -2.9; 49 -2.6; 54 -2.1; 60 -1.4; 66 -0.8; 72 -0.1; 79 0.6; 87 1.1; 96 1.3; 106 1.5; 116 1.9; 128 2.5; 141 3.4; 155 4.3; 170 4.4; 187 3.4; 206 1.9; 227 0.5; 249 -0.3; 274 -0.9; 302 -1.3; 332 -1.5; 365 -1.8; 402 -2.2; 442 -2.0; 486 -1.5; 535 -1.2; 588 -1.0; 647 -0.6; 712 -0.5; 783 -0.6; 861 -0.6; 947 -0.1; 1042 0.0; 1146 -0.0; 1261 0.1; 1387 -0.1; 1526 -0.4; 1678 -0.4; 1846 -0.2; 2031 0.0; 2234 0.8; 2457 2.5; 2703 4.7; 2973 6.0; 3270 5.7; 3597 5.3; 3957 5.6; 4353 5.3; 4788 2.7; 5267 4.5; 5793 5.0; 6373 4.0; 7010 2.5; 7711 0.3; 8482 -1.8; 9330 -2.6; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 39 Hz   |  1.21 | -3.5 dB |
| Peaking | 169 Hz  |  1.15 | 7.0 dB  |
| Peaking | 266 Hz  |  0.66 | -4.0 dB |
| Peaking | 3385 Hz |  1.9  | 6.3 dB  |
| Peaking | 5804 Hz |  3.7  | 4.3 dB  |
| Peaking | 1948 Hz |  2.62 | -1.3 dB |
| Peaking | 2786 Hz |  8.43 | 2.0 dB  |
| Peaking | 6148 Hz |  7.27 | -0.6 dB |
| Peaking | 6708 Hz | 10.05 | 2.2 dB  |
| Peaking | 8977 Hz |  5.98 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)