# AKG K81DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.2; 31 -2.8; 34 -3.3; 37 -3.8; 41 -4.3; 45 -4.6; 49 -4.8; 54 -5.4; 60 -6.0; 66 -6.5; 72 -6.7; 79 -7.1; 87 -7.5; 96 -6.9; 106 -7.3; 116 -8.4; 128 -9.4; 141 -10.1; 155 -10.1; 170 -9.9; 187 -10.0; 206 -8.8; 227 -8.3; 249 -7.8; 274 -8.0; 302 -7.7; 332 -7.3; 365 -5.8; 402 -5.0; 442 -5.0; 486 -5.2; 535 -5.5; 588 -5.4; 647 -5.8; 712 -6.3; 783 -6.3; 861 -6.7; 947 -7.0; 1042 -7.4; 1146 -7.5; 1261 -7.7; 1387 -8.3; 1526 -9.1; 1678 -9.6; 1846 -9.8; 2031 -9.2; 2234 -8.7; 2457 -6.8; 2703 -5.4; 2973 -3.9; 3270 -3.6; 3597 -4.1; 3957 -4.5; 4353 -5.2; 4788 -4.5; 5267 -3.8; 5793 -5.5; 6373 -2.6; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -7.8; 16529 -9.4; 18182 -9.0; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K81DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K81DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  0.81 | 6.2 dB  |
| Peaking | 156 Hz   |  1.75 | -3.9 dB |
| Peaking | 1968 Hz  |  1.66 | -5.5 dB |
| Peaking | 3018 Hz  |  1.02 | 4.2 dB  |
| Peaking | 6475 Hz  |  6.72 | 3.8 dB  |
| Peaking | 313 Hz   |  1.78 | -2.1 dB |
| Peaking | 419 Hz   |  1.57 | 3.1 dB  |
| Peaking | 5083 Hz  | 15.08 | 1.9 dB  |
| Peaking | 8258 Hz  |  4.15 | -0.6 dB |
| Peaking | 17223 Hz |  1.7  | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K81DJ/AKG%20K81DJ.png)