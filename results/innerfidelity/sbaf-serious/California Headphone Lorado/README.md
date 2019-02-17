# California Headphone Lorado
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -2.0; 45 -3.2; 49 -4.1; 54 -5.0; 60 -6.1; 66 -6.8; 72 -7.0; 79 -7.4; 87 -8.7; 96 -9.3; 106 -8.8; 116 -8.9; 128 -9.5; 141 -9.7; 155 -9.7; 170 -9.2; 187 -9.8; 206 -10.2; 227 -9.7; 249 -9.3; 274 -8.6; 302 -7.8; 332 -7.1; 365 -6.7; 402 -6.5; 442 -6.3; 486 -6.3; 535 -6.1; 588 -5.7; 647 -5.6; 712 -5.7; 783 -5.5; 861 -5.9; 947 -6.2; 1042 -6.6; 1146 -6.9; 1261 -7.4; 1387 -8.4; 1526 -8.5; 1678 -9.7; 1846 -9.4; 2031 -8.4; 2234 -6.6; 2457 -4.7; 2703 -2.8; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -8.4; 11289 -6.6; 12418 -6.5; 13660 -7.8; 15026 -6.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`California Headphone Lorado GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `California Headphone Lorado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.91 | 7.0 dB  |
| Peaking | 137 Hz   | 0.74 | -3.8 dB |
| Peaking | 1816 Hz  | 2.3  | -5.0 dB |
| Peaking | 3510 Hz  | 1.28 | 6.9 dB  |
| Peaking | 5898 Hz  | 4.25 | 4.4 dB  |
| Peaking | 230 Hz   | 3.72 | -1.4 dB |
| Peaking | 571 Hz   | 1.14 | 1.2 dB  |
| Peaking | 9990 Hz  | 4.01 | -2.4 dB |
| Peaking | 14235 Hz | 6.29 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/California%20Headphone%20Lorado/California%20Headphone%20Lorado.png)