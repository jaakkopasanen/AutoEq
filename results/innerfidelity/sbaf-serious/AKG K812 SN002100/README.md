# AKG K812 sn002100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.6; 25 -4.9; 28 -5.2; 31 -5.4; 34 -5.6; 37 -5.8; 41 -6.0; 45 -6.2; 49 -6.3; 54 -6.5; 60 -6.7; 66 -6.8; 72 -7.0; 79 -7.2; 87 -7.6; 96 -8.0; 106 -8.2; 116 -8.5; 128 -8.9; 141 -8.9; 155 -9.1; 170 -9.1; 187 -9.1; 206 -9.3; 227 -9.1; 249 -8.9; 274 -8.8; 302 -8.7; 332 -8.5; 365 -8.3; 402 -8.1; 442 -7.6; 486 -7.5; 535 -7.2; 588 -6.6; 647 -6.3; 712 -5.9; 783 -5.1; 861 -4.6; 947 -4.6; 1042 -4.0; 1146 -3.5; 1261 -3.3; 1387 -3.5; 1526 -4.5; 1678 -3.7; 1846 -2.8; 2031 -3.4; 2234 -3.4; 2457 -1.8; 2703 -0.9; 2973 -5.2; 3270 -6.2; 3597 -5.1; 3957 -1.7; 4353 -0.5; 4788 -5.3; 5267 -9.3; 5793 -12.7; 6373 -9.3; 7010 -4.5; 7711 -6.0; 8482 -7.3; 9330 -7.0; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K812 sn002100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 sn002100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 219 Hz  |  0.55 | -3.1 dB |
| Peaking | 1334 Hz |  0.85 | 3.1 dB  |
| Peaking | 2585 Hz |  6.82 | 4.8 dB  |
| Peaking | 4249 Hz |  6.34 | 6.7 dB  |
| Peaking | 5782 Hz |  5.92 | -7.8 dB |
| Peaking | 19 Hz   |  0.99 | 2.2 dB  |
| Peaking | 1923 Hz |  7.82 | 1.1 dB  |
| Peaking | 3199 Hz |  8.68 | -1.8 dB |
| Peaking | 6957 Hz | 10.13 | 3.1 dB  |
| Peaking | 8802 Hz |  7.01 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812%20sn002100/AKG%20K812%20sn002100.png)