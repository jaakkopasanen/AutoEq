# VSonic VSD3S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.6; 25 -11.7; 28 -11.8; 31 -11.8; 34 -11.9; 37 -11.9; 41 -11.9; 45 -12.0; 49 -12.0; 54 -12.0; 60 -12.1; 66 -12.2; 72 -12.3; 79 -12.4; 87 -12.5; 96 -12.6; 106 -12.6; 116 -12.7; 128 -12.6; 141 -12.5; 155 -12.4; 170 -12.1; 187 -11.9; 206 -11.5; 227 -11.2; 249 -10.8; 274 -10.3; 302 -9.9; 332 -9.5; 365 -9.1; 402 -8.7; 442 -8.4; 486 -8.1; 535 -7.8; 588 -7.5; 647 -7.1; 712 -6.6; 783 -6.0; 861 -5.4; 947 -4.9; 1042 -4.6; 1146 -4.6; 1261 -4.6; 1387 -4.1; 1526 -3.0; 1678 -1.8; 1846 -0.6; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.4; 3597 -1.7; 3957 -1.2; 4353 -0.6; 4788 -0.9; 5267 -2.4; 5793 -5.8; 6373 -9.7; 7010 -10.6; 7711 -13.1; 8482 -11.7; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.2; 15026 -6.5; 16529 -6.5; 18182 -8.7; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD3S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD3S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.41 | -4.3 dB |
| Peaking | 138 Hz   | 0.43 | -5.4 dB |
| Peaking | 2366 Hz  | 0.8  | 6.3 dB  |
| Peaking | 4713 Hz  | 2.88 | 4.6 dB  |
| Peaking | 7490 Hz  | 2.56 | -7.9 dB |
| Peaking | 954 Hz   | 4    | 0.6 dB  |
| Peaking | 1329 Hz  | 6.02 | -0.9 dB |
| Peaking | 8370 Hz  | 8.17 | -2.9 dB |
| Peaking | 9277 Hz  | 3.7  | 2.3 dB  |
| Peaking | 18985 Hz | 1.58 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/VSonic%20VSD3S/VSonic%20VSD3S.png)