# Custom Art FIBAE 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.6; 25 -3.7; 28 -3.9; 31 -4.0; 34 -4.1; 37 -4.1; 41 -4.3; 45 -4.4; 49 -4.5; 54 -4.6; 60 -4.9; 66 -5.1; 72 -5.4; 79 -5.7; 87 -6.0; 96 -6.4; 106 -6.8; 116 -7.1; 128 -7.3; 141 -7.6; 155 -7.9; 170 -8.0; 187 -8.1; 206 -8.1; 227 -8.1; 249 -8.1; 274 -8.0; 302 -7.9; 332 -7.8; 365 -7.6; 402 -7.5; 442 -7.3; 486 -7.1; 535 -6.8; 588 -6.5; 647 -6.1; 712 -5.7; 783 -5.2; 861 -4.8; 947 -4.7; 1042 -4.9; 1146 -5.5; 1261 -6.2; 1387 -6.7; 1526 -6.8; 1678 -6.7; 1846 -6.8; 2031 -7.5; 2234 -8.8; 2457 -10.3; 2703 -9.7; 2973 -7.2; 3270 -5.2; 3597 -4.7; 3957 -6.3; 4353 -10.6; 4788 -8.4; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -4.3; 7711 -9.2; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art FIBAE 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art FIBAE 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.3  | 3.0 dB  |
| Peaking | 692 Hz  | 0.12 | -2.8 dB |
| Peaking | 884 Hz  | 0.86 | 4.4 dB  |
| Peaking | 6025 Hz | 3.37 | 8.3 dB  |
| Peaking | 7827 Hz | 7.01 | -4.1 dB |
| Peaking | 1889 Hz | 4.56 | 1.1 dB  |
| Peaking | 2577 Hz | 3.57 | -3.9 dB |
| Peaking | 3551 Hz | 2.31 | 4.7 dB  |
| Peaking | 4483 Hz | 4.9  | -6.7 dB |
| Peaking | 5261 Hz | 9.33 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Custom%20Art%20FIBAE%201/Custom%20Art%20FIBAE%201.png)