# Sony CD3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -2.0; 34 -2.9; 37 -3.7; 41 -4.6; 45 -5.4; 49 -6.1; 54 -6.8; 60 -7.2; 66 -7.4; 72 -7.5; 79 -7.4; 87 -7.4; 96 -7.5; 106 -7.3; 116 -7.1; 128 -7.1; 141 -6.9; 155 -6.8; 170 -6.5; 187 -6.2; 206 -6.1; 227 -5.8; 249 -5.7; 274 -5.3; 302 -4.8; 332 -4.2; 365 -3.8; 402 -3.7; 442 -4.1; 486 -5.1; 535 -6.1; 588 -6.8; 647 -6.9; 712 -6.6; 783 -6.6; 861 -7.0; 947 -7.3; 1042 -7.4; 1146 -7.7; 1261 -7.8; 1387 -7.8; 1526 -7.4; 1678 -6.8; 1846 -6.2; 2031 -5.4; 2234 -4.2; 2457 -2.9; 2703 -2.8; 2973 -4.2; 3270 -5.7; 3597 -6.5; 3957 -7.2; 4353 -8.4; 4788 -9.1; 5267 -8.7; 5793 -7.0; 6373 -6.0; 7010 -8.2; 7711 -9.9; 8482 -10.0; 9330 -10.1; 10263 -12.0; 11289 -14.0; 12418 -14.9; 13660 -14.9; 15026 -12.9; 16529 -8.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony CD3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony CD3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.91 | 6.7 dB  |
| Peaking | 376 Hz   | 2.74 | 3.2 dB  |
| Peaking | 2607 Hz  | 3.67 | 4.5 dB  |
| Peaking | 4687 Hz  | 4.82 | -2.3 dB |
| Peaking | 12758 Hz | 1.16 | -9.2 dB |
| Peaking | 74 Hz    | 0.3  | 1.6 dB  |
| Peaking | 82 Hz    | 0.71 | -2.9 dB |
| Peaking | 1328 Hz  | 1.13 | -1.7 dB |
| Peaking | 2076 Hz  | 1.95 | 1.1 dB  |
| Peaking | 16904 Hz | 3.32 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | -6.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20CD3000/Sony%20CD3000.png)