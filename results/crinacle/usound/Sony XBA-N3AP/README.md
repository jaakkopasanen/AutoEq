# Sony XBA-N3AP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.1; 25 -7.5; 28 -7.9; 31 -8.2; 34 -8.4; 37 -8.6; 41 -8.7; 45 -8.9; 49 -9.0; 54 -9.1; 60 -9.1; 66 -9.2; 72 -9.3; 79 -9.4; 87 -9.5; 96 -9.5; 106 -9.5; 116 -9.4; 128 -9.4; 141 -9.2; 155 -9.0; 170 -8.7; 187 -8.4; 206 -8.0; 227 -7.6; 249 -7.3; 274 -6.8; 302 -6.4; 332 -6.0; 365 -5.7; 402 -5.3; 442 -5.0; 486 -4.8; 535 -4.5; 588 -4.3; 647 -4.1; 712 -3.8; 783 -3.6; 861 -3.4; 947 -3.5; 1042 -4.0; 1146 -4.6; 1261 -5.1; 1387 -5.7; 1526 -5.8; 1678 -5.4; 1846 -4.8; 2031 -4.5; 2234 -4.2; 2457 -3.6; 2703 -2.6; 2973 -1.4; 3270 -1.2; 3597 -2.4; 3957 -3.0; 4353 -1.8; 4788 -2.2; 5267 -2.4; 5793 -1.0; 6373 -0.5; 7010 -3.4; 7711 -6.2; 8482 -5.8; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -6.7; 16529 -9.5; 18182 -8.4; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-N3AP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-N3AP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 82 Hz    | 0.34 | -4.6 dB |
| Peaking | 657 Hz   | 1.26 | 1.8 dB  |
| Peaking | 4695 Hz  | 0.91 | 3.8 dB  |
| Peaking | 13872 Hz | 1.61 | 5.0 dB  |
| Peaking | 15671 Hz | 0.7  | -6.1 dB |
| Peaking | 1516 Hz  | 4.12 | -1.5 dB |
| Peaking | 3133 Hz  | 3.39 | 3.4 dB  |
| Peaking | 3619 Hz  | 1.53 | -1.9 dB |
| Peaking | 6324 Hz  | 4.94 | 3.2 dB  |
| Peaking | 7737 Hz  | 5.43 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20XBA-N3AP/Sony%20XBA-N3AP.png)