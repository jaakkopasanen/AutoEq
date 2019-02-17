# V-Moda XS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.7; 25 -7.0; 28 -7.5; 31 -7.8; 34 -8.1; 37 -8.3; 41 -8.5; 45 -8.7; 49 -8.8; 54 -8.9; 60 -8.9; 66 -9.0; 72 -9.1; 79 -9.1; 87 -9.2; 96 -9.3; 106 -9.1; 116 -9.0; 128 -9.2; 141 -9.2; 155 -9.0; 170 -8.5; 187 -8.3; 206 -7.7; 227 -7.4; 249 -7.9; 274 -6.8; 302 -5.6; 332 -4.5; 365 -3.3; 402 -3.1; 442 -2.6; 486 -2.3; 535 -2.0; 588 -1.5; 647 -1.5; 712 -1.9; 783 -2.0; 861 -2.8; 947 -3.6; 1042 -4.4; 1146 -4.9; 1261 -5.2; 1387 -5.2; 1526 -5.1; 1678 -4.9; 1846 -4.5; 2031 -4.8; 2234 -4.5; 2457 -4.7; 2703 -5.7; 2973 -6.4; 3270 -6.0; 3597 -4.0; 3957 -0.9; 4353 -0.6; 4788 -3.3; 5267 -0.5; 5793 -1.8; 6373 -1.3; 7010 -2.0; 7711 -3.8; 8482 -4.1; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda XS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda XS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 190 Hz  | 0.13 | -6.0 dB |
| Peaking | 550 Hz  | 0.74 | 8.0 dB  |
| Peaking | 3122 Hz | 3.83 | -2.5 dB |
| Peaking | 4093 Hz | 5.4  | 4.2 dB  |
| Peaking | 5857 Hz | 2.59 | 3.1 dB  |
| Peaking | 256 Hz  | 7.31 | -1.1 dB |
| Peaking | 360 Hz  | 4.81 | 0.9 dB  |
| Peaking | 511 Hz  | 2.87 | -1.0 dB |
| Peaking | 1056 Hz | 0.86 | 1.5 dB  |
| Peaking | 1197 Hz | 1.77 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20XS/V-Moda%20XS.png)