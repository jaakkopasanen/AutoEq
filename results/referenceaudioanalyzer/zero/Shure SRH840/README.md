# Shure SRH840
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.8; 25 -2.3; 28 -2.7; 31 -2.8; 34 -2.7; 37 -2.7; 41 -2.9; 45 -3.2; 49 -3.4; 54 -3.2; 60 -3.2; 66 -3.6; 72 -4.4; 79 -5.8; 87 -7.2; 96 -7.9; 106 -8.1; 116 -8.0; 128 -7.7; 141 -7.2; 155 -6.6; 170 -5.7; 187 -4.7; 206 -3.5; 227 -2.6; 249 -2.0; 274 -1.8; 302 -2.0; 332 -2.4; 365 -2.1; 402 -1.8; 442 -1.8; 486 -1.8; 535 -1.8; 588 -1.6; 647 -1.3; 712 -1.1; 783 -0.9; 861 -0.7; 947 -0.5; 1042 -0.7; 1146 -0.8; 1261 -0.8; 1387 -0.8; 1526 -1.0; 1678 -1.2; 1846 -1.4; 2031 -1.7; 2234 -2.5; 2457 -3.9; 2703 -4.9; 2973 -5.3; 3270 -5.2; 3597 -5.0; 3957 -5.0; 4353 -5.7; 4788 -7.2; 5267 -8.6; 5793 -10.0; 6373 -10.6; 7010 -8.5; 7711 -3.7; 8482 -3.4; 9330 -3.4; 10263 -3.4; 11289 -3.4; 12418 -5.2; 13660 -4.5; 15026 -3.4; 16529 -3.4; 18182 -3.4; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH840 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 114 Hz   | 0.91 | -9.1 dB |
| Peaking | 115 Hz   | 0.31 | 4.1 dB  |
| Peaking | 2355 Hz  | 0.38 | 4.5 dB  |
| Peaking | 3058 Hz  | 1.09 | -5.6 dB |
| Peaking | 5994 Hz  | 2.35 | -8.8 dB |
| Peaking | 67 Hz    | 5.77 | 0.6 dB  |
| Peaking | 246 Hz   | 2.49 | 2.3 dB  |
| Peaking | 250 Hz   | 1.25 | -1.5 dB |
| Peaking | 8038 Hz  | 7.97 | 1.9 dB  |
| Peaking | 12966 Hz | 5.93 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SRH840/Shure%20SRH840.png)