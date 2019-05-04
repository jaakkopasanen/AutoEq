# AKG N60NC Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.8; 25 -2.2; 28 -2.8; 31 -3.3; 34 -3.7; 37 -4.0; 41 -4.4; 45 -4.7; 49 -5.0; 54 -5.3; 60 -5.7; 66 -6.1; 72 -6.4; 79 -6.7; 87 -7.0; 96 -7.4; 106 -7.6; 116 -7.8; 128 -8.0; 141 -8.1; 155 -8.1; 170 -8.0; 187 -7.9; 206 -7.8; 227 -7.6; 249 -7.4; 274 -7.3; 302 -7.2; 332 -7.1; 365 -6.9; 402 -6.5; 442 -6.2; 486 -6.0; 535 -5.7; 588 -5.2; 647 -4.5; 712 -3.6; 783 -2.8; 861 -2.1; 947 -1.6; 1042 -1.2; 1146 -1.0; 1261 -1.1; 1387 -0.9; 1526 -0.5; 1678 -1.0; 1846 -1.4; 2031 -1.8; 2234 -2.2; 2457 -2.5; 2703 -3.4; 2973 -5.4; 3270 -7.6; 3597 -8.9; 3957 -7.4; 4353 -5.1; 4788 -4.3; 5267 -5.5; 5793 -8.3; 6373 -9.4; 7010 -7.2; 7711 -5.2; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N60NC Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N60NC Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.35 | 5.1 dB  |
| Peaking | 285 Hz  | 0.2  | -3.5 dB |
| Peaking | 1271 Hz | 0.52 | 6.6 dB  |
| Peaking | 3507 Hz | 3.7  | -5.8 dB |
| Peaking | 6243 Hz | 5.06 | -5.2 dB |
| Peaking | 268 Hz  | 2.95 | 0.5 dB  |
| Peaking | 757 Hz  | 1.11 | -0.9 dB |
| Peaking | 844 Hz  | 2.1  | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20N60NC%20Wireless/AKG%20N60NC%20Wireless.png)