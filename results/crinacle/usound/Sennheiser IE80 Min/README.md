# Sennheiser IE80 Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.9; 28 -2.7; 31 -3.4; 34 -4.0; 37 -4.6; 41 -5.2; 45 -5.7; 49 -6.2; 54 -6.7; 60 -7.1; 66 -7.6; 72 -8.1; 79 -8.6; 87 -9.0; 96 -9.4; 106 -9.8; 116 -10.0; 128 -10.2; 141 -10.4; 155 -10.5; 170 -10.4; 187 -10.4; 206 -10.2; 227 -10.0; 249 -9.8; 274 -9.6; 302 -9.3; 332 -9.0; 365 -8.8; 402 -8.5; 442 -8.3; 486 -8.0; 535 -7.8; 588 -7.6; 647 -7.3; 712 -6.9; 783 -6.5; 861 -6.1; 947 -5.7; 1042 -5.6; 1146 -5.9; 1261 -6.2; 1387 -6.1; 1526 -5.5; 1678 -4.6; 1846 -3.5; 2031 -2.7; 2234 -2.0; 2457 -1.6; 2703 -1.6; 2973 -1.8; 3270 -2.3; 3597 -2.9; 3957 -3.8; 4353 -5.3; 4788 -8.2; 5267 -11.7; 5793 -8.7; 6373 -3.9; 7010 -4.0; 7711 -6.3; 8482 -6.5; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.7; 15026 -9.0; 16529 -8.1; 18182 -7.9; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80 Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80 Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.62 | 7.5 dB  |
| Peaking | 158 Hz   | 0.48 | -4.1 dB |
| Peaking | 2761 Hz  | 1.09 | 5.4 dB  |
| Peaking | 5317 Hz  | 4.36 | -7.3 dB |
| Peaking | 6571 Hz  | 6.14 | 4.3 dB  |
| Peaking | 976 Hz   | 3.59 | 0.8 dB  |
| Peaking | 1375 Hz  | 4.41 | -1.0 dB |
| Peaking | 8861 Hz  | 0.49 | 0.8 dB  |
| Peaking | 12444 Hz | 1.85 | 2.1 dB  |
| Peaking | 14625 Hz | 0.51 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sennheiser%20IE80%20Min/Sennheiser%20IE80%20Min.png)