# AKG K3003 Bass Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.7; 25 -7.2; 28 -7.8; 31 -8.3; 34 -8.7; 37 -9.1; 41 -9.5; 45 -9.9; 49 -10.3; 54 -10.7; 60 -11.1; 66 -11.6; 72 -12.0; 79 -12.4; 87 -12.9; 96 -13.4; 106 -13.6; 116 -13.7; 128 -14.1; 141 -14.2; 155 -14.2; 170 -14.2; 187 -14.1; 206 -13.9; 227 -13.6; 249 -13.3; 274 -12.9; 302 -12.4; 332 -11.9; 365 -11.3; 402 -10.6; 442 -9.8; 486 -9.3; 535 -8.6; 588 -7.6; 647 -7.0; 712 -6.5; 783 -5.8; 861 -5.7; 947 -5.6; 1042 -5.6; 1146 -5.6; 1261 -5.7; 1387 -5.8; 1526 -6.0; 1678 -6.8; 1846 -7.3; 2031 -7.6; 2234 -7.8; 2457 -7.2; 2703 -5.8; 2973 -3.1; 3270 -1.0; 3597 -0.5; 3957 -2.0; 4353 -5.6; 4788 -8.6; 5267 -10.2; 5793 -7.4; 6373 -3.8; 7010 -3.2; 7711 -5.3; 8482 -5.5; 9330 -7.7; 10263 -6.8; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 Bass Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 110 Hz  | 0.45 | -7.3 dB |
| Peaking | 268 Hz  | 0.9  | -3.8 dB |
| Peaking | 2432 Hz | 1.64 | -8.1 dB |
| Peaking | 3292 Hz | 1.05 | 9.3 dB  |
| Peaking | 5013 Hz | 3.4  | -8.6 dB |
| Peaking | 483 Hz  | 2.38 | -0.8 dB |
| Peaking | 802 Hz  | 1.41 | 0.9 dB  |
| Peaking | 1769 Hz | 6.35 | -0.9 dB |
| Peaking | 6745 Hz | 8.65 | 2.8 dB  |
| Peaking | 9616 Hz | 5.17 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20Bass%20Boost%20Filter/AKG%20K3003%20Bass%20Boost%20Filter.png)