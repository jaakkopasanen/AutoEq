# Superlux HD 681
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -3.0; 25 -3.6; 28 -4.4; 31 -4.9; 34 -5.4; 37 -5.7; 41 -5.9; 45 -6.0; 49 -6.0; 54 -5.9; 60 -5.8; 66 -5.7; 72 -5.6; 79 -5.6; 87 -5.6; 96 -5.7; 106 -5.7; 116 -5.7; 128 -5.6; 141 -5.4; 155 -5.1; 170 -4.6; 187 -4.0; 206 -3.1; 227 -3.5; 249 -3.9; 274 -3.7; 302 -3.7; 332 -3.6; 365 -3.5; 402 -3.5; 442 -3.6; 486 -3.9; 535 -3.2; 588 -2.6; 647 -3.1; 712 -3.2; 783 -3.2; 861 -3.1; 947 -3.1; 1042 -3.2; 1146 -3.2; 1261 -3.3; 1387 -3.5; 1526 -4.1; 1678 -5.3; 1846 -7.4; 2031 -8.8; 2234 -9.3; 2457 -8.2; 2703 -6.7; 2973 -6.1; 3270 -5.9; 3597 -3.6; 3957 -0.5; 4353 -4.0; 4788 -10.0; 5267 -10.8; 5793 -7.9; 6373 -6.5; 7010 -7.9; 7711 -11.8; 8482 -12.8; 9330 -12.2; 10263 -13.1; 11289 -12.3; 12418 -8.7; 13660 -7.8; 15026 -8.4; 16529 -7.4; 18182 -8.2; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 3.01 | 3.1 dB  |
| Peaking | 2136 Hz  | 2.52 | -6.6 dB |
| Peaking | 3925 Hz  | 0.07 | 3.3 dB  |
| Peaking | 9179 Hz  | 1.16 | -7.0 dB |
| Peaking | 19148 Hz | 0.08 | -4.4 dB |
| Peaking | 212 Hz   | 7.7  | 1.3 dB  |
| Peaking | 3312 Hz  | 2.39 | -2.1 dB |
| Peaking | 4033 Hz  | 3.96 | 8.1 dB  |
| Peaking | 4936 Hz  | 3.3  | -7.0 dB |
| Peaking | 6431 Hz  | 5.84 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Superlux%20HD%20681/Superlux%20HD%20681.png)