# California Headphone Lorado
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.3; 37 -2.2; 41 -3.4; 45 -4.5; 49 -5.5; 54 -6.4; 60 -7.4; 66 -8.2; 72 -8.4; 79 -8.8; 87 -10.1; 96 -10.7; 106 -10.2; 116 -10.3; 128 -10.9; 141 -11.0; 155 -11.1; 170 -10.5; 187 -11.2; 206 -11.6; 227 -11.1; 249 -10.7; 274 -10.0; 302 -9.2; 332 -8.5; 365 -8.1; 402 -7.8; 442 -7.7; 486 -7.7; 535 -7.5; 588 -7.1; 647 -7.0; 712 -7.1; 783 -6.9; 861 -7.3; 947 -7.6; 1042 -8.0; 1146 -8.3; 1261 -8.8; 1387 -9.8; 1526 -9.9; 1678 -11.0; 1846 -10.8; 2031 -9.8; 2234 -7.9; 2457 -6.1; 2703 -4.2; 2973 -1.4; 3270 -0.8; 3597 -0.7; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -3.4; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.2; 10263 -9.8; 11289 -7.3; 12418 -6.5; 13660 -9.1; 15026 -7.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`California Headphone Lorado GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `California Headphone Lorado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.96 | 7.2 dB  |
| Peaking | 141 Hz   | 0.56 | -5.1 dB |
| Peaking | 1786 Hz  | 1.67 | -5.8 dB |
| Peaking | 3570 Hz  | 1.48 | 7.3 dB  |
| Peaking | 6069 Hz  | 5.13 | 4.9 dB  |
| Peaking | 235 Hz   | 2.42 | -1.8 dB |
| Peaking | 278 Hz   | 0.77 | 0.9 dB  |
| Peaking | 5918 Hz  | 1.23 | 0.5 dB  |
| Peaking | 10578 Hz | 2.98 | -3.0 dB |
| Peaking | 16519 Hz | 2.17 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/California%20Headphone%20Lorado/California%20Headphone%20Lorado.png)