# Sennheiser HD 280 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.0; 25 -0.2; 28 -0.5; 31 -0.6; 34 -0.7; 37 -0.8; 41 -0.7; 45 -0.5; 49 -0.2; 54 0.5; 60 1.8; 66 4.0; 72 6.0; 79 5.9; 87 2.6; 96 0.9; 106 5.0; 116 6.0; 128 4.2; 141 3.5; 155 4.2; 170 3.5; 187 1.7; 206 0.7; 227 0.2; 249 -0.2; 274 -0.5; 302 -0.3; 332 -0.4; 365 -0.2; 402 -0.3; 442 -0.0; 486 0.1; 535 0.1; 588 -0.3; 647 -0.2; 712 -0.1; 783 -0.0; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.1; 1387 0.2; 1526 0.7; 1678 -0.2; 1846 -0.8; 2031 -1.1; 2234 -1.6; 2457 -1.8; 2703 -0.1; 2973 3.1; 3270 3.0; 3597 1.4; 3957 1.1; 4353 1.6; 4788 1.8; 5267 3.3; 5793 2.8; 6373 1.1; 7010 0.4; 7711 -1.2; 8482 -3.6; 9330 -5.6; 10263 -4.9; 11289 -1.4; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 73 Hz   |  5.02 | 5.7 dB  |
| Peaking | 125 Hz  |  2.01 | 5.1 dB  |
| Peaking | 3145 Hz |  8.09 | 3.8 dB  |
| Peaking | 5456 Hz |  2.87 | 3.7 dB  |
| Peaking | 9480 Hz |  3.21 | -6.4 dB |
| Peaking | 38 Hz   |  2.43 | -1.1 dB |
| Peaking | 163 Hz  | 10.35 | 2.8 dB  |
| Peaking | 268 Hz  |  1.3  | -0.8 dB |
| Peaking | 2314 Hz |  4.2  | -2.4 dB |
| Peaking | 7362 Hz |  0.15 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)