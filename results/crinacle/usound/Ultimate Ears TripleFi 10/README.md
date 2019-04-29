# Ultimate Ears TripleFi 10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.3; 28 -6.6; 31 -6.7; 34 -6.8; 37 -7.0; 41 -7.2; 45 -7.4; 49 -7.5; 54 -7.7; 60 -7.9; 66 -8.2; 72 -8.6; 79 -9.0; 87 -9.4; 96 -9.7; 106 -10.0; 116 -10.3; 128 -10.6; 141 -10.8; 155 -11.0; 170 -11.0; 187 -11.1; 206 -10.9; 227 -10.8; 249 -10.6; 274 -10.5; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.3; 442 -9.1; 486 -8.7; 535 -8.4; 588 -8.0; 647 -7.7; 712 -7.2; 783 -6.8; 861 -6.4; 947 -6.2; 1042 -6.3; 1146 -6.8; 1261 -7.2; 1387 -7.2; 1526 -6.6; 1678 -5.5; 1846 -4.4; 2031 -3.4; 2234 -2.8; 2457 -2.6; 2703 -1.9; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.9; 5793 -3.1; 6373 -6.8; 7010 -8.9; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.9; 13660 -9.5; 15026 -10.2; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears TripleFi 10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears TripleFi 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 122 Hz   | 0.88 | -1.2 dB |
| Peaking | 220 Hz   | 0.48 | -3.8 dB |
| Peaking | 4124 Hz  | 0.82 | 7.1 dB  |
| Peaking | 6966 Hz  | 3.38 | -6.1 dB |
| Peaking | 14359 Hz | 2.11 | -4.3 dB |
| Peaking | 17 Hz    | 1.37 | 0.9 dB  |
| Peaking | 931 Hz   | 2.68 | 1.1 dB  |
| Peaking | 1425 Hz  | 1.84 | -2.9 dB |
| Peaking | 1858 Hz  | 1.17 | 1.6 dB  |
| Peaking | 3941 Hz  | 5.78 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ultimate%20Ears%20TripleFi%2010/Ultimate%20Ears%20TripleFi%2010.png)