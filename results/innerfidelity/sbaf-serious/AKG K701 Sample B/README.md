# AKG K701 sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.3; 45 -1.7; 49 -2.1; 54 -2.6; 60 -2.6; 66 -2.1; 72 -2.3; 79 -3.8; 87 -3.8; 96 -5.0; 106 -5.5; 116 -5.9; 128 -6.3; 141 -6.6; 155 -6.8; 170 -6.9; 187 -7.0; 206 -7.1; 227 -7.0; 249 -7.0; 274 -7.0; 302 -6.8; 332 -6.4; 365 -6.2; 402 -6.1; 442 -5.5; 486 -5.2; 535 -5.0; 588 -4.5; 647 -4.1; 712 -3.4; 783 -3.0; 861 -4.0; 947 -4.9; 1042 -5.5; 1146 -5.9; 1261 -5.9; 1387 -6.1; 1526 -6.3; 1678 -7.0; 1846 -7.8; 2031 -8.5; 2234 -8.3; 2457 -8.0; 2703 -7.5; 2973 -6.2; 3270 -4.6; 3597 -5.0; 3957 -5.6; 4353 -7.2; 4788 -7.3; 5267 -6.4; 5793 -8.2; 6373 -10.1; 7010 -8.9; 7711 -9.1; 8482 -9.8; 9330 -8.5; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.9; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.63 | 6.4 dB  |
| Peaking | 747 Hz   | 2.01 | 3.4 dB  |
| Peaking | 2214 Hz  | 2.44 | -2.3 dB |
| Peaking | 3430 Hz  | 4.04 | 2.8 dB  |
| Peaking | 7357 Hz  | 1.69 | -3.2 dB |
| Peaking | 55 Hz    | 1.44 | -0.8 dB |
| Peaking | 69 Hz    | 2.75 | 2.3 dB  |
| Peaking | 177 Hz   | 1.17 | -1.2 dB |
| Peaking | 10935 Hz | 4.71 | 0.9 dB  |
| Peaking | 19782 Hz | 1.86 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701%20sample%20B/AKG%20K701%20sample%20B.png)