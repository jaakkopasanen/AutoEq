# AKG K3003 High Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.1; 25 -2.6; 28 -3.2; 31 -3.7; 34 -4.1; 37 -4.4; 41 -4.8; 45 -5.3; 49 -5.7; 54 -6.1; 60 -6.6; 66 -6.9; 72 -7.4; 79 -7.7; 87 -8.1; 96 -8.4; 106 -8.6; 116 -8.8; 128 -9.2; 141 -9.2; 155 -9.4; 170 -9.4; 187 -9.4; 206 -9.3; 227 -9.1; 249 -8.9; 274 -8.6; 302 -8.2; 332 -7.8; 365 -7.3; 402 -6.8; 442 -6.6; 486 -6.2; 535 -5.7; 588 -5.2; 647 -4.8; 712 -4.5; 783 -4.1; 861 -4.2; 947 -4.3; 1042 -4.8; 1146 -5.0; 1261 -5.2; 1387 -5.3; 1526 -5.7; 1678 -6.3; 1846 -6.4; 2031 -6.3; 2234 -6.1; 2457 -6.0; 2703 -6.0; 2973 -6.0; 3270 -4.3; 3597 -0.5; 3957 -0.7; 4353 -5.8; 4788 -10.7; 5267 -10.2; 5793 -9.0; 6373 -4.2; 7010 -2.5; 7711 -4.4; 8482 -9.0; 9330 -14.7; 10263 -14.5; 11289 -7.0; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 High Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 High Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 1.2  | 3.3 dB   |
| Peaking | 157 Hz  | 0.51 | -5.1 dB  |
| Peaking | 5324 Hz | 3.48 | -10.5 dB |
| Peaking | 6756 Hz | 0.96 | 5.6 dB   |
| Peaking | 9555 Hz | 3.12 | -14.9 dB |
| Peaking | 896 Hz  | 0.7  | 4.4 dB   |
| Peaking | 1610 Hz | 0.31 | -4.2 dB  |
| Peaking | 3802 Hz | 4.58 | 6.6 dB   |
| Peaking | 4655 Hz | 8.48 | -4.0 dB  |
| Peaking | 5661 Hz | 0.89 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20High%20Boost%20Filter/AKG%20K3003%20High%20Boost%20Filter.png)