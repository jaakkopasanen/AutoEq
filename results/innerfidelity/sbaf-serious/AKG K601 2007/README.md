# AKG K601 2007
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.2; 45 -1.7; 49 -2.1; 54 -2.5; 60 -2.0; 66 -1.4; 72 -2.7; 79 -3.7; 87 -4.1; 96 -4.9; 106 -5.5; 116 -5.8; 128 -6.3; 141 -6.7; 155 -6.9; 170 -7.1; 187 -7.3; 206 -7.5; 227 -7.5; 249 -7.5; 274 -7.5; 302 -7.3; 332 -7.2; 365 -7.1; 402 -6.9; 442 -6.7; 486 -6.6; 535 -6.4; 588 -6.0; 647 -6.0; 712 -5.9; 783 -6.2; 861 -6.6; 947 -6.6; 1042 -6.5; 1146 -6.4; 1261 -6.3; 1387 -6.6; 1526 -7.4; 1678 -8.0; 1846 -9.3; 2031 -10.2; 2234 -9.9; 2457 -9.7; 2703 -9.4; 2973 -8.6; 3270 -6.7; 3597 -7.5; 3957 -8.2; 4353 -8.9; 4788 -9.4; 5267 -7.8; 5793 -10.3; 6373 -11.5; 7010 -8.5; 7711 -8.9; 8482 -10.9; 9330 -11.0; 10263 -9.5; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 2007 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 2007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.65 | 6.5 dB  |
| Peaking | 2248 Hz  | 1.96 | -3.7 dB |
| Peaking | 6127 Hz  | 4.21 | -4.6 dB |
| Peaking | 9098 Hz  | 2.99 | -4.7 dB |
| Peaking | 22050 Hz | 2.4  | -2.0 dB |
| Peaking | 67 Hz    | 4.32 | 2.2 dB  |
| Peaking | 233 Hz   | 0.78 | -1.5 dB |
| Peaking | 676 Hz   | 0.8  | 0.8 dB  |
| Peaking | 4661 Hz  | 5.19 | -2.9 dB |
| Peaking | 5233 Hz  | 4.15 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K601%202007/AKG%20K601%202007.png)