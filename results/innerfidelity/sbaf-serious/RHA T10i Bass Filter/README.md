# RHA T10i Bass Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.4; 23 -16.5; 25 -16.7; 28 -16.9; 31 -17.1; 34 -17.3; 37 -17.4; 41 -17.4; 45 -17.4; 49 -17.6; 54 -17.6; 60 -17.6; 66 -17.7; 72 -17.7; 79 -17.9; 87 -17.9; 96 -18.0; 106 -17.7; 116 -17.5; 128 -17.4; 141 -17.2; 155 -16.9; 170 -16.6; 187 -16.1; 206 -15.6; 227 -15.0; 249 -14.5; 274 -13.8; 302 -13.2; 332 -12.5; 365 -11.9; 402 -11.2; 442 -10.4; 486 -9.9; 535 -9.3; 588 -8.4; 647 -7.8; 712 -7.7; 783 -7.0; 861 -6.6; 947 -6.2; 1042 -6.6; 1146 -6.9; 1261 -7.3; 1387 -8.0; 1526 -8.9; 1678 -9.6; 1846 -10.0; 2031 -10.1; 2234 -9.9; 2457 -8.8; 2703 -7.4; 2973 -5.8; 3270 -5.1; 3597 -5.3; 3957 -4.1; 4353 -2.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.1; 8482 -15.5; 9330 -18.0; 10263 -15.6; 11289 -7.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T10i Bass Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Bass Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.23 | -10.5 dB |
| Peaking | 188 Hz   | 0.62 | -4.7 dB  |
| Peaking | 2061 Hz  | 2.02 | -4.6 dB  |
| Peaking | 5847 Hz  | 1.18 | 8.5 dB   |
| Peaking | 9168 Hz  | 2.8  | -15.9 dB |
| Peaking | 940 Hz   | 2.4  | 1.5 dB   |
| Peaking | 1758 Hz  | 1.82 | -1.1 dB  |
| Peaking | 1972 Hz  | 4.95 | 1.3 dB   |
| Peaking | 10347 Hz | 6.48 | -4.4 dB  |
| Peaking | 11476 Hz | 2.86 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB  |
| Peaking | 125 Hz   | 1.41 | -9.0 dB  |
| Peaking | 250 Hz   | 1.41 | -6.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Bass%20Filter/RHA%20T10i%20Bass%20Filter.png)