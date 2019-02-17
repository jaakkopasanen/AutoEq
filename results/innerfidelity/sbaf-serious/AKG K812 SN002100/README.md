# AKG K812 sn002100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.1; 25 -5.4; 28 -5.7; 31 -5.9; 34 -6.1; 37 -6.3; 41 -6.5; 45 -6.6; 49 -6.7; 54 -7.0; 60 -7.2; 66 -7.3; 72 -7.4; 79 -7.6; 87 -8.1; 96 -8.4; 106 -8.7; 116 -9.0; 128 -9.4; 141 -9.4; 155 -9.6; 170 -9.5; 187 -9.6; 206 -9.7; 227 -9.5; 249 -9.4; 274 -9.3; 302 -9.1; 332 -9.0; 365 -8.8; 402 -8.5; 442 -8.1; 486 -8.0; 535 -7.6; 588 -7.0; 647 -6.7; 712 -6.3; 783 -5.6; 861 -5.1; 947 -5.1; 1042 -4.4; 1146 -4.0; 1261 -3.8; 1387 -3.9; 1526 -4.9; 1678 -4.2; 1846 -3.3; 2031 -3.8; 2234 -3.9; 2457 -2.3; 2703 -1.0; 2973 -5.7; 3270 -6.7; 3597 -5.5; 3957 -2.1; 4353 -0.5; 4788 -5.7; 5267 -9.8; 5793 -13.1; 6373 -9.8; 7010 -5.0; 7711 -6.2; 8482 -7.7; 9330 -7.5; 10263 -5.2; 11289 -4.8; 12418 -4.8; 13660 -4.8; 15026 -4.8; 16529 -4.8; 18182 -5.4; 20000 -13.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K812 sn002100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 sn002100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 186 Hz   | 0.42 | -5.0 dB |
| Peaking | 2800 Hz  | 1.99 | 6.2 dB  |
| Peaking | 3142 Hz  | 3.43 | -7.0 dB |
| Peaking | 4245 Hz  | 6.15 | 6.2 dB  |
| Peaking | 5772 Hz  | 3.86 | -9.2 dB |
| Peaking | 1021 Hz  | 0.63 | -1.6 dB |
| Peaking | 1099 Hz  | 1.25 | 2.8 dB  |
| Peaking | 7004 Hz  | 7.97 | 3.2 dB  |
| Peaking | 9130 Hz  | 2.73 | -3.5 dB |
| Peaking | 10340 Hz | 2.86 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812%20sn002100/AKG%20K812%20sn002100.png)