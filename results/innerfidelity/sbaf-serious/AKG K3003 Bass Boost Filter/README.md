# AKG K3003 Bass Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -5.0; 25 -5.5; 28 -6.1; 31 -6.5; 34 -7.0; 37 -7.4; 41 -7.8; 45 -8.2; 49 -8.6; 54 -9.0; 60 -9.4; 66 -9.9; 72 -10.3; 79 -10.7; 87 -11.2; 96 -11.6; 106 -11.9; 116 -12.0; 128 -12.3; 141 -12.4; 155 -12.5; 170 -12.5; 187 -12.4; 206 -12.2; 227 -11.9; 249 -11.6; 274 -11.2; 302 -10.7; 332 -10.2; 365 -9.6; 402 -8.9; 442 -8.1; 486 -7.6; 535 -6.9; 588 -5.9; 647 -5.2; 712 -4.8; 783 -4.1; 861 -4.0; 947 -3.9; 1042 -3.8; 1146 -3.9; 1261 -4.0; 1387 -4.0; 1526 -4.2; 1678 -5.1; 1846 -5.6; 2031 -5.9; 2234 -6.1; 2457 -5.5; 2703 -4.1; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -3.8; 4788 -6.8; 5267 -8.5; 5793 -5.7; 6373 -2.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 Bass Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 92 Hz    | 0.96 | -2.4 dB |
| Peaking | 203 Hz   | 0.58 | -5.4 dB |
| Peaking | 897 Hz   | 0.95 | 3.6 dB  |
| Peaking | 3474 Hz  | 2.85 | 6.7 dB  |
| Peaking | 21587 Hz | 2.31 | 1.3 dB  |
| Peaking | 20 Hz    | 2.14 | 2.3 dB  |
| Peaking | 1450 Hz  | 6.13 | 0.9 dB  |
| Peaking | 2214 Hz  | 5.32 | -1.2 dB |
| Peaking | 5209 Hz  | 6.54 | -3.8 dB |
| Peaking | 6472 Hz  | 6.22 | 4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20Bass%20Boost%20Filter/AKG%20K3003%20Bass%20Boost%20Filter.png)