# Unique Melody Martian
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.7; 34 -0.9; 37 -1.0; 41 -1.3; 45 -1.5; 49 -1.8; 54 -2.1; 60 -2.5; 66 -2.9; 72 -3.3; 79 -3.7; 87 -4.2; 96 -4.7; 106 -5.1; 116 -5.5; 128 -5.9; 141 -6.3; 155 -6.6; 170 -6.8; 187 -7.0; 206 -7.1; 227 -7.2; 249 -7.2; 274 -7.3; 302 -7.3; 332 -7.3; 365 -7.3; 402 -7.3; 442 -7.3; 486 -7.3; 535 -7.3; 588 -7.4; 647 -7.4; 712 -7.3; 783 -7.2; 861 -7.3; 947 -7.5; 1042 -8.0; 1146 -8.9; 1261 -9.7; 1387 -10.3; 1526 -10.3; 1678 -9.8; 1846 -9.0; 2031 -8.0; 2234 -7.2; 2457 -6.2; 2703 -4.7; 2973 -2.9; 3270 -1.7; 3597 -2.0; 3957 -3.3; 4353 -4.1; 4788 -2.5; 5267 -2.2; 5793 -3.5; 6373 -4.7; 7010 -8.8; 7711 -8.3; 8482 -6.5; 9330 -6.5; 10263 -7.8; 11289 -7.0; 12418 -6.5; 13660 -7.3; 15026 -14.1; 16529 -11.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Martian GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Martian ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.89 | 6.0 dB  |
| Peaking | 58 Hz    | 1.44 | 2.8 dB  |
| Peaking | 3949 Hz  | 1.87 | 4.5 dB  |
| Peaking | 13380 Hz | 3.77 | 2.7 dB  |
| Peaking | 15436 Hz | 2.34 | -9.2 dB |
| Peaking | 1529 Hz  | 1.19 | -4.1 dB |
| Peaking | 3180 Hz  | 2.53 | 3.2 dB  |
| Peaking | 4229 Hz  | 3.28 | -4.3 dB |
| Peaking | 5162 Hz  | 2.14 | 3.9 dB  |
| Peaking | 7240 Hz  | 6    | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -5.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Unique%20Melody%20Martian/Unique%20Melody%20Martian.png)