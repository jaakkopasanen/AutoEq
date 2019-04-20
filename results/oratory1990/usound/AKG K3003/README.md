# AKG K3003
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.3; 25 -8.4; 28 -8.4; 31 -8.4; 34 -8.3; 37 -8.3; 41 -8.4; 45 -8.6; 49 -8.8; 54 -8.9; 60 -9.1; 66 -9.3; 72 -9.6; 79 -9.9; 87 -10.2; 96 -10.5; 106 -10.8; 116 -11.0; 128 -11.2; 141 -11.3; 155 -11.4; 170 -11.4; 187 -11.4; 206 -11.2; 227 -11.0; 249 -10.8; 274 -10.5; 302 -10.1; 332 -9.7; 365 -9.3; 402 -8.9; 442 -8.4; 486 -7.9; 535 -7.4; 588 -6.9; 647 -6.4; 712 -5.9; 783 -5.4; 861 -5.0; 947 -4.8; 1042 -4.9; 1146 -5.0; 1261 -5.0; 1387 -5.0; 1526 -4.8; 1678 -4.2; 1846 -3.7; 2031 -3.4; 2234 -3.0; 2457 -2.2; 2703 -1.6; 2973 -2.2; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -4.6; 5267 -6.6; 5793 -7.8; 6373 -7.3; 7010 -9.2; 7711 -10.9; 8482 -8.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -9.5; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.15 | -1.5 dB  |
| Peaking | 152 Hz   | 0.69 | -4.0 dB  |
| Peaking | 308 Hz   | 1.22 | -1.8 dB  |
| Peaking | 4252 Hz  | 0.71 | 19.9 dB  |
| Peaking | 5323 Hz  | 0.67 | -16.7 dB |
| Peaking | 854 Hz   | 4.45 | 0.9 dB   |
| Peaking | 6608 Hz  | 7.26 | 2.4 dB   |
| Peaking | 7630 Hz  | 3.48 | -4.5 dB  |
| Peaking | 9145 Hz  | 1.59 | 2.4 dB   |
| Peaking | 14778 Hz | 5.01 | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/AKG%20K3003/AKG%20K3003.png)