# Final Audio Heaven S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.7; 25 -5.8; 28 -6.0; 31 -6.1; 34 -6.3; 37 -6.4; 41 -6.6; 45 -6.8; 49 -7.0; 54 -7.1; 60 -7.4; 66 -7.8; 72 -8.2; 79 -8.6; 87 -8.8; 96 -9.2; 106 -9.5; 116 -9.8; 128 -10.0; 141 -10.3; 155 -10.4; 170 -10.6; 187 -10.7; 206 -10.6; 227 -10.5; 249 -10.4; 274 -10.2; 302 -9.8; 332 -9.6; 365 -9.3; 402 -8.9; 442 -8.5; 486 -8.0; 535 -7.6; 588 -7.1; 647 -6.5; 712 -5.8; 783 -5.2; 861 -4.6; 947 -4.2; 1042 -4.2; 1146 -4.6; 1261 -5.0; 1387 -5.1; 1526 -4.7; 1678 -4.1; 1846 -3.5; 2031 -3.2; 2234 -3.4; 2457 -4.4; 2703 -6.5; 2973 -8.0; 3270 -6.4; 3597 -3.4; 3957 -1.1; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -5.9; 6373 -12.8; 7010 -13.0; 7711 -10.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 199 Hz  | 0.53 | -4.3 dB |
| Peaking | 944 Hz  | 1.57 | 2.8 dB  |
| Peaking | 1956 Hz | 3.49 | 3.1 dB  |
| Peaking | 4817 Hz | 2.33 | 8.2 dB  |
| Peaking | 6745 Hz | 3.61 | -9.8 dB |
| Peaking | 22 Hz   | 1.05 | 1.1 dB  |
| Peaking | 2413 Hz | 4.22 | 2.2 dB  |
| Peaking | 2951 Hz | 3.03 | -3.6 dB |
| Peaking | 3821 Hz | 5.75 | 2.7 dB  |
| Peaking | 8452 Hz | 8.51 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20Heaven%20S/Final%20Audio%20Heaven%20S.png)