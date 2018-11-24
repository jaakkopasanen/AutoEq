# Sennheiser HD 280 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -1.3; 23 -1.6; 25 -2.0; 28 -2.4; 31 -2.8; 34 -3.0; 37 -3.0; 41 -2.8; 45 -2.6; 49 -2.2; 54 -1.7; 60 -1.1; 66 -0.6; 72 -0.1; 79 0.4; 87 0.7; 96 0.9; 106 1.0; 116 1.4; 128 2.0; 141 2.9; 155 3.7; 170 3.8; 187 2.8; 206 1.4; 227 0.0; 249 -0.8; 274 -1.6; 302 -2.1; 332 -2.5; 365 -2.8; 402 -3.3; 442 -3.2; 486 -2.7; 535 -2.4; 588 -2.1; 647 -1.7; 712 -1.3; 783 -1.1; 861 -0.8; 947 -0.2; 1042 -0.0; 1146 -0.2; 1261 -0.2; 1387 -0.1; 1526 0.0; 1678 -0.1; 1846 -0.2; 2031 -0.4; 2234 0.3; 2457 2.1; 2703 4.1; 2973 5.5; 3270 3.9; 3597 3.1; 3957 4.4; 4353 5.5; 4788 2.9; 5267 4.1; 5793 3.6; 6373 1.5; 7010 2.2; 7711 0.3; 8482 -2.2; 9330 -4.1; 10263 -1.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 165 Hz  |  1.98 | 4.9 dB  |
| Peaking | 386 Hz  |  0.86 | -3.4 dB |
| Peaking | 2901 Hz |  5.52 | 4.3 dB  |
| Peaking | 4631 Hz |  1.32 | 4.5 dB  |
| Peaking | 9203 Hz |  4.66 | -5.3 dB |
| Peaking | 36 Hz   |  1.45 | -3.4 dB |
| Peaking | 992 Hz  |  5.86 | 0.6 dB  |
| Peaking | 2040 Hz |  5.98 | -1.3 dB |
| Peaking | 4232 Hz | 10.84 | 2.0 dB  |
| Peaking | 4713 Hz | 11.69 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)