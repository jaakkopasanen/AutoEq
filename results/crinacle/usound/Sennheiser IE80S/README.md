# Sennheiser IE80S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.2; 25 -1.7; 28 -2.5; 31 -3.1; 34 -3.7; 37 -4.2; 41 -4.7; 45 -5.1; 49 -5.5; 54 -5.9; 60 -6.4; 66 -6.8; 72 -7.2; 79 -7.6; 87 -8.0; 96 -8.4; 106 -8.7; 116 -8.9; 128 -9.0; 141 -9.1; 155 -9.2; 170 -9.1; 187 -9.0; 206 -8.8; 227 -8.6; 249 -8.3; 274 -8.0; 302 -7.6; 332 -7.3; 365 -7.0; 402 -6.7; 442 -6.3; 486 -6.0; 535 -5.7; 588 -5.3; 647 -5.0; 712 -4.6; 783 -4.2; 861 -3.8; 947 -3.7; 1042 -3.5; 1146 -3.8; 1261 -4.5; 1387 -4.7; 1526 -4.4; 1678 -3.7; 1846 -3.0; 2031 -2.6; 2234 -2.4; 2457 -2.6; 2703 -3.1; 2973 -3.8; 3270 -4.4; 3597 -4.8; 3957 -5.7; 4353 -7.7; 4788 -10.9; 5267 -9.3; 5793 -3.7; 6373 -0.5; 7010 -3.1; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -6.2; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.74 | 5.9 dB  |
| Peaking | 151 Hz   | 0.54 | -3.9 dB |
| Peaking | 1927 Hz  | 0.43 | 2.6 dB  |
| Peaking | 4947 Hz  | 3.7  | -7.8 dB |
| Peaking | 6335 Hz  | 5.09 | 6.0 dB  |
| Peaking | 989 Hz   | 1.97 | 0.9 dB  |
| Peaking | 1391 Hz  | 2.47 | -1.7 dB |
| Peaking | 2198 Hz  | 3.26 | 1.1 dB  |
| Peaking | 17801 Hz | 1.43 | 2.5 dB  |
| Peaking | 19920 Hz | 0.9  | -8.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sennheiser%20IE80S/Sennheiser%20IE80S.png)