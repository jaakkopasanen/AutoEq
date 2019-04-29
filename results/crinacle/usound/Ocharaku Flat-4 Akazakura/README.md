# Ocharaku Flat-4 Akazakura
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.2; 25 -5.4; 28 -5.8; 31 -6.0; 34 -6.2; 37 -6.3; 41 -6.5; 45 -6.7; 49 -6.9; 54 -7.1; 60 -7.3; 66 -7.5; 72 -7.8; 79 -8.1; 87 -8.4; 96 -8.7; 106 -8.9; 116 -9.1; 128 -9.3; 141 -9.4; 155 -9.4; 170 -9.4; 187 -9.2; 206 -9.1; 227 -8.8; 249 -8.5; 274 -8.2; 302 -8.0; 332 -7.6; 365 -7.3; 402 -7.0; 442 -6.7; 486 -6.5; 535 -6.3; 588 -6.1; 647 -5.9; 712 -5.7; 783 -5.5; 861 -5.4; 947 -5.5; 1042 -5.8; 1146 -6.3; 1261 -6.7; 1387 -6.3; 1526 -4.6; 1678 -1.9; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -3.2; 2973 -7.4; 3270 -8.9; 3597 -6.6; 3957 -4.8; 4353 -4.6; 4788 -8.0; 5267 -7.4; 5793 -0.5; 6373 -3.6; 7010 -13.1; 7711 -18.0; 8482 -16.7; 9330 -9.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.8; 16529 -12.9; 18182 -13.3; 20000 -19.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat-4 Akazakura GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat-4 Akazakura ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 21 Hz   |  1.26 | 1.8 dB   |
| Peaking | 147 Hz  |  0.79 | -3.1 dB  |
| Peaking | 2062 Hz |  2.42 | 7.1 dB   |
| Peaking | 5972 Hz |  6.45 | 9.9 dB   |
| Peaking | 7803 Hz |  3.37 | -13.6 dB |
| Peaking | 797 Hz  |  1.63 | 1.0 dB   |
| Peaking | 1299 Hz |  3.88 | -2.0 dB  |
| Peaking | 3223 Hz |  4.23 | -7.5 dB  |
| Peaking | 3481 Hz |  1.29 | 3.8 dB   |
| Peaking | 5022 Hz | 11.78 | -6.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.8 dB |
| Peaking | 16000 Hz | 1.41 | -5.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ocharaku%20Flat-4%20Akazakura/Ocharaku%20Flat-4%20Akazakura.png)