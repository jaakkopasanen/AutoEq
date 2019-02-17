# AKG K3003 Reference Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.8; 25 -3.3; 28 -3.9; 31 -4.4; 34 -4.8; 37 -5.2; 41 -5.7; 45 -6.1; 49 -6.4; 54 -6.9; 60 -7.4; 66 -7.8; 72 -8.3; 79 -8.7; 87 -9.2; 96 -9.7; 106 -10.0; 116 -10.1; 128 -10.5; 141 -10.8; 155 -10.9; 170 -10.9; 187 -10.9; 206 -10.8; 227 -10.6; 249 -10.5; 274 -10.2; 302 -9.9; 332 -9.6; 365 -9.2; 402 -8.8; 442 -8.2; 486 -8.0; 535 -7.6; 588 -6.9; 647 -6.6; 712 -6.5; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.7; 1146 -6.9; 1261 -7.2; 1387 -7.6; 1526 -8.0; 1678 -8.7; 1846 -8.7; 2031 -8.5; 2234 -8.2; 2457 -7.1; 2703 -5.6; 2973 -3.7; 3270 -1.8; 3597 -0.5; 3957 -0.6; 4353 -5.8; 4788 -10.1; 5267 -9.2; 5793 -6.1; 6373 -2.7; 7010 -4.0; 7711 -6.2; 8482 -8.2; 9330 -12.1; 10263 -12.8; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 Reference Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.88 | 4.4 dB   |
| Peaking | 165 Hz   | 0.61 | -4.7 dB  |
| Peaking | 3688 Hz  | 2.1  | 14.8 dB  |
| Peaking | 5272 Hz  | 0.72 | -12.2 dB |
| Peaking | 6520 Hz  | 2.74 | 13.1 dB  |
| Peaking | 825 Hz   | 2.07 | 1.4 dB   |
| Peaking | 1835 Hz  | 3.33 | -1.4 dB  |
| Peaking | 8131 Hz  | 6.55 | 2.5 dB   |
| Peaking | 10033 Hz | 3.01 | -7.0 dB  |
| Peaking | 11562 Hz | 1.56 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20Reference%20Filter/AKG%20K3003%20Reference%20Filter.png)