# AKG K3003 High Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.1; 31 -2.6; 34 -3.0; 37 -3.4; 41 -3.8; 45 -4.2; 49 -4.6; 54 -5.0; 60 -5.5; 66 -6.0; 72 -6.4; 79 -6.8; 87 -7.3; 96 -7.8; 106 -8.1; 116 -8.3; 128 -8.6; 141 -8.8; 155 -9.0; 170 -9.0; 187 -9.0; 206 -9.0; 227 -8.8; 249 -8.6; 274 -8.3; 302 -8.1; 332 -7.7; 365 -7.3; 402 -6.9; 442 -6.4; 486 -6.2; 535 -5.8; 588 -5.1; 647 -4.8; 712 -4.6; 783 -4.2; 861 -4.3; 947 -4.4; 1042 -4.7; 1146 -4.9; 1261 -5.1; 1387 -5.3; 1526 -5.8; 1678 -6.3; 1846 -6.3; 2031 -6.2; 2234 -6.2; 2457 -6.0; 2703 -6.2; 2973 -5.9; 3270 -4.2; 3597 -1.2; 3957 -1.4; 4353 -6.6; 4788 -11.2; 5267 -10.6; 5793 -10.3; 6373 -5.6; 7010 -3.2; 7711 -4.4; 8482 -8.6; 9330 -13.4; 10263 -13.6; 11289 -7.6; 12418 -4.5; 13660 -4.5; 15026 -4.6; 16529 -4.9; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 High Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 High Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.75 | 4.6 dB   |
| Peaking | 166 Hz   | 0.55 | -4.8 dB  |
| Peaking | 5338 Hz  | 3.9  | -7.5 dB  |
| Peaking | 7181 Hz  | 3.55 | 3.8 dB   |
| Peaking | 9721 Hz  | 3.46 | -10.9 dB |
| Peaking | 815 Hz   | 1.94 | 1.3 dB   |
| Peaking | 2613 Hz  | 0.86 | -2.3 dB  |
| Peaking | 3787 Hz  | 3.53 | 6.8 dB   |
| Peaking | 4591 Hz  | 8.99 | -4.2 dB  |
| Peaking | 12391 Hz | 5.74 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20High%20Boost%20Filter/AKG%20K3003%20High%20Boost%20Filter.png)