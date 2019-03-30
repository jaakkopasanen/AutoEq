# Beyerdynamic Custom One Studio switch position 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.5; 25 -2.4; 28 -3.4; 31 -4.2; 34 -4.8; 37 -5.3; 41 -5.7; 45 -6.1; 49 -6.4; 54 -6.6; 60 -6.3; 66 -5.8; 72 -5.4; 79 -5.4; 87 -5.9; 96 -6.5; 106 -7.3; 116 -7.9; 128 -8.0; 141 -7.9; 155 -8.3; 170 -8.8; 187 -8.9; 206 -8.9; 227 -8.9; 249 -8.9; 274 -8.9; 302 -8.9; 332 -8.8; 365 -8.5; 402 -8.2; 442 -7.9; 486 -7.6; 535 -7.4; 588 -7.1; 647 -6.8; 712 -6.2; 783 -5.5; 861 -5.2; 947 -5.0; 1042 -4.9; 1146 -4.7; 1261 -4.7; 1387 -4.6; 1526 -4.4; 1678 -4.4; 1846 -4.9; 2031 -5.5; 2234 -5.9; 2457 -6.0; 2703 -5.9; 2973 -6.2; 3270 -6.4; 3597 -6.5; 3957 -5.5; 4353 -3.7; 4788 -3.5; 5267 -6.6; 5793 -9.5; 6373 -10.4; 7010 -8.7; 7711 -6.5; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.8; 12418 -7.6; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Studio switch position 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Studio switch position 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 1.03 | 9.0 dB  |
| Peaking | 264 Hz   | 0.72 | -2.6 dB |
| Peaking | 1272 Hz  | 0.95 | 2.5 dB  |
| Peaking | 4639 Hz  | 4.99 | 4.3 dB  |
| Peaking | 6172 Hz  | 3.98 | -4.6 dB |
| Peaking | 54 Hz    | 1.57 | -1.4 dB |
| Peaking | 76 Hz    | 1.72 | 2.1 dB  |
| Peaking | 115 Hz   | 2.14 | -0.9 dB |
| Peaking | 7916 Hz  | 7.99 | 0.8 dB  |
| Peaking | 12354 Hz | 7.63 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20Custom%20One%20Studio%20switch%20position%203/Beyerdynamic%20Custom%20One%20Studio%20switch%20position%203.png)