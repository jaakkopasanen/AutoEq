# AKG N60NC Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.2; 25 -2.7; 28 -3.3; 31 -3.8; 34 -4.2; 37 -4.5; 41 -4.8; 45 -5.2; 49 -5.4; 54 -5.8; 60 -6.1; 66 -6.6; 72 -6.9; 79 -7.2; 87 -7.6; 96 -7.9; 106 -8.1; 116 -8.4; 128 -8.5; 141 -8.6; 155 -8.6; 170 -8.5; 187 -8.3; 206 -8.2; 227 -8.0; 249 -7.8; 274 -7.6; 302 -7.5; 332 -7.5; 365 -7.3; 402 -6.8; 442 -6.5; 486 -6.2; 535 -5.9; 588 -5.4; 647 -4.7; 712 -3.7; 783 -2.9; 861 -2.2; 947 -1.7; 1042 -1.4; 1146 -1.2; 1261 -1.3; 1387 -1.1; 1526 -0.5; 1678 -1.1; 1846 -1.4; 2031 -1.7; 2234 -1.7; 2457 -1.8; 2703 -3.1; 2973 -5.6; 3270 -8.1; 3597 -9.4; 3957 -8.1; 4353 -5.7; 4788 -4.2; 5267 -5.5; 5793 -8.5; 6373 -10.8; 7010 -7.4; 7711 -5.3; 8482 -5.6; 9330 -6.9; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N60NC Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N60NC Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 166 Hz  | 0.29 | -3.3 dB |
| Peaking | 1294 Hz | 0.7  | 5.6 dB  |
| Peaking | 2588 Hz | 1.78 | 8.0 dB  |
| Peaking | 3107 Hz | 1.28 | -8.9 dB |
| Peaking | 18 Hz   | 0.75 | 4.4 dB  |
| Peaking | 54 Hz   | 1.28 | 0.9 dB  |
| Peaking | 3657 Hz | 5.74 | -1.4 dB |
| Peaking | 4806 Hz | 3.57 | 3.7 dB  |
| Peaking | 6235 Hz | 5.85 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20N60NC%20Wireless/AKG%20N60NC%20Wireless.png)