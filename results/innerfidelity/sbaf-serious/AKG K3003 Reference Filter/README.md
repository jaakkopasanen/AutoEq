# AKG K3003 Reference Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.7; 25 -2.1; 28 -2.7; 31 -3.2; 34 -3.7; 37 -4.1; 41 -4.5; 45 -4.9; 49 -5.3; 54 -5.7; 60 -6.2; 66 -6.7; 72 -7.1; 79 -7.6; 87 -8.0; 96 -8.6; 106 -8.8; 116 -9.0; 128 -9.3; 141 -9.6; 155 -9.7; 170 -9.8; 187 -9.7; 206 -9.7; 227 -9.5; 249 -9.4; 274 -9.1; 302 -8.8; 332 -8.4; 365 -8.0; 402 -7.6; 442 -7.1; 486 -6.9; 535 -6.5; 588 -5.8; 647 -5.5; 712 -5.3; 783 -4.9; 861 -5.0; 947 -5.2; 1042 -5.5; 1146 -5.8; 1261 -6.0; 1387 -6.4; 1526 -6.9; 1678 -7.5; 1846 -7.6; 2031 -7.4; 2234 -7.1; 2457 -6.0; 2703 -4.5; 2973 -2.6; 3270 -0.8; 3597 -0.5; 3957 -0.5; 4353 -4.6; 4788 -8.9; 5267 -8.1; 5793 -5.0; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -10.9; 10263 -11.6; 11289 -7.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 Reference Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.74 | 5.4 dB  |
| Peaking | 161 Hz  | 0.78 | -3.7 dB |
| Peaking | 3509 Hz | 3.65 | 7.1 dB  |
| Peaking | 6522 Hz | 7.3  | 5.4 dB  |
| Peaking | 9848 Hz | 4.52 | -6.2 dB |
| Peaking | 323 Hz  | 1.95 | -0.8 dB |
| Peaking | 799 Hz  | 1.25 | 1.9 dB  |
| Peaking | 1876 Hz | 2.36 | -1.9 dB |
| Peaking | 4472 Hz | 2.24 | 3.6 dB  |
| Peaking | 4828 Hz | 4.73 | -7.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20Reference%20Filter/AKG%20K3003%20Reference%20Filter.png)