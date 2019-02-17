# RHA T10i Reference Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.6; 23 -15.9; 25 -16.2; 28 -16.4; 31 -16.6; 34 -16.7; 37 -16.8; 41 -17.0; 45 -17.0; 49 -17.0; 54 -17.1; 60 -17.2; 66 -17.3; 72 -17.3; 79 -17.4; 87 -17.5; 96 -17.5; 106 -17.4; 116 -17.2; 128 -17.1; 141 -16.9; 155 -16.6; 170 -16.2; 187 -15.8; 206 -15.4; 227 -14.8; 249 -14.3; 274 -13.6; 302 -12.9; 332 -12.3; 365 -11.6; 402 -11.0; 442 -10.2; 486 -9.7; 535 -9.1; 588 -8.2; 647 -7.7; 712 -7.6; 783 -6.9; 861 -6.5; 947 -6.2; 1042 -6.7; 1146 -7.0; 1261 -7.4; 1387 -8.2; 1526 -9.2; 1678 -10.0; 1846 -10.7; 2031 -11.1; 2234 -11.2; 2457 -10.1; 2703 -8.3; 2973 -6.2; 3270 -5.4; 3597 -5.4; 3957 -4.0; 4353 -2.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -11.2; 9330 -13.7; 10263 -16.2; 11289 -12.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T10i Reference Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.24 | -10.0 dB |
| Peaking | 187 Hz   | 0.64 | -4.7 dB  |
| Peaking | 2110 Hz  | 2.06 | -5.7 dB  |
| Peaking | 5490 Hz  | 1.36 | 7.7 dB   |
| Peaking | 9869 Hz  | 2.52 | -11.4 dB |
| Peaking | 380 Hz   | 2.42 | -0.6 dB  |
| Peaking | 902 Hz   | 1.9  | 1.4 dB   |
| Peaking | 1564 Hz  | 4.7  | -1.1 dB  |
| Peaking | 10921 Hz | 7.05 | -3.7 dB  |
| Peaking | 12150 Hz | 2.94 | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.9 dB |
| Peaking | 62 Hz    | 1.41 | -7.9 dB |
| Peaking | 125 Hz   | 1.41 | -8.7 dB |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Reference%20Filter/RHA%20T10i%20Reference%20Filter.png)