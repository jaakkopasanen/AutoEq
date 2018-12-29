# Sennheiser HD 202 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.9; 25 3.3; 28 2.5; 31 1.8; 34 1.2; 37 0.7; 41 0.1; 45 -0.5; 49 -1.0; 54 -1.7; 60 -2.3; 66 -2.8; 72 -3.0; 79 -3.1; 87 -3.3; 96 -3.4; 106 -3.3; 116 -2.9; 128 -2.4; 141 -1.8; 155 -1.3; 170 -0.5; 187 0.4; 206 1.4; 227 2.5; 249 3.6; 274 4.6; 302 4.8; 332 3.8; 365 3.7; 402 3.6; 442 3.2; 486 2.5; 535 1.8; 588 1.2; 647 0.9; 712 0.8; 783 0.6; 861 0.4; 947 0.1; 1042 -0.1; 1146 -0.6; 1261 -0.9; 1387 -1.6; 1526 -1.8; 1678 -1.6; 1846 -1.1; 2031 -0.0; 2234 1.1; 2457 2.1; 2703 3.5; 2973 4.6; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.9; 5267 5.3; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -2.8; 13660 -4.6; 15026 -1.7; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 2.92 | 4.4 dB  |
| Peaking | 343 Hz   | 1.57 | 4.9 dB  |
| Peaking | 3372 Hz  | 1.47 | 8.0 dB  |
| Peaking | 5225 Hz  | 0.28 | -4.4 dB |
| Peaking | 5819 Hz  | 1.3  | 8.1 dB  |
| Peaking | 94 Hz    | 0.99 | -3.8 dB |
| Peaking | 249 Hz   | 3.13 | 2.1 dB  |
| Peaking | 11495 Hz | 2.62 | 4.8 dB  |
| Peaking | 13299 Hz | 1.62 | -6.5 dB |
| Peaking | 15720 Hz | 1.46 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20202%20II/Sennheiser%20HD%20202%20II.png)