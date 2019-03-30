# Shure SRH940
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.0; 28 -2.9; 31 -3.7; 34 -4.4; 37 -4.9; 41 -5.6; 45 -6.2; 49 -6.6; 54 -6.9; 60 -6.8; 66 -6.3; 72 -5.4; 79 -3.9; 87 -3.0; 96 -3.9; 106 -5.2; 116 -5.6; 128 -5.4; 141 -5.0; 155 -4.7; 170 -4.5; 187 -4.1; 206 -3.9; 227 -3.6; 249 -3.6; 274 -3.7; 302 -4.0; 332 -4.2; 365 -4.2; 402 -3.7; 442 -3.3; 486 -3.0; 535 -2.7; 588 -2.5; 647 -2.3; 712 -2.5; 783 -2.7; 861 -3.0; 947 -3.2; 1042 -3.5; 1146 -3.6; 1261 -3.4; 1387 -3.2; 1526 -3.0; 1678 -2.9; 1846 -2.6; 2031 -2.9; 2234 -3.0; 2457 -3.3; 2703 -4.1; 2973 -5.0; 3270 -5.8; 3597 -6.7; 3957 -7.5; 4353 -8.3; 4788 -8.9; 5267 -9.5; 5793 -10.1; 6373 -10.5; 7010 -9.5; 7711 -6.4; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -5.1; 12418 -6.9; 13660 -7.3; 15026 -5.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH940 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH940 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.8  | 4.3 dB  |
| Peaking | 52 Hz    | 2.25 | -2.9 dB |
| Peaking | 3514 Hz  | 0.12 | 2.3 dB  |
| Peaking | 5509 Hz  | 1.14 | -8.1 dB |
| Peaking | 13469 Hz | 2.45 | -4.2 dB |
| Peaking | 88 Hz    | 5.54 | 2.2 dB  |
| Peaking | 117 Hz   | 3.1  | -1.4 dB |
| Peaking | 1129 Hz  | 4.85 | -1.0 dB |
| Peaking | 6925 Hz  | 5.25 | -2.5 dB |
| Peaking | 8182 Hz  | 3.01 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.3 dB |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SRH940/Shure%20SRH940.png)