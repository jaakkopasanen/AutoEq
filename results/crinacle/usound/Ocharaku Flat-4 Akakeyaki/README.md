# Ocharaku Flat-4 Akakeyaki
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.2; 25 -4.4; 28 -4.7; 31 -4.9; 34 -5.1; 37 -5.3; 41 -5.5; 45 -5.6; 49 -5.7; 54 -5.7; 60 -5.8; 66 -6.1; 72 -6.3; 79 -6.6; 87 -7.0; 96 -7.4; 106 -7.6; 116 -7.8; 128 -7.9; 141 -8.0; 155 -8.2; 170 -8.3; 187 -8.2; 206 -8.1; 227 -8.0; 249 -7.9; 274 -7.7; 302 -7.5; 332 -7.3; 365 -7.1; 402 -6.9; 442 -6.8; 486 -6.6; 535 -6.5; 588 -6.4; 647 -6.3; 712 -6.1; 783 -5.9; 861 -5.7; 947 -5.7; 1042 -5.8; 1146 -6.2; 1261 -6.5; 1387 -6.1; 1526 -4.6; 1678 -2.4; 1846 -0.6; 2031 -0.5; 2234 -0.7; 2457 -2.9; 2703 -6.3; 2973 -8.2; 3270 -6.7; 3597 -4.2; 3957 -3.5; 4353 -4.5; 4788 -8.9; 5267 -8.8; 5793 -0.5; 6373 -2.5; 7010 -14.8; 7711 -20.7; 8482 -14.9; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -7.4; 15026 -6.5; 16529 -6.5; 18182 -11.8; 20000 -18.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat-4 Akakeyaki GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat-4 Akakeyaki ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 23 Hz   |  1.51 | 2.4 dB   |
| Peaking | 2002 Hz |  2.86 | 6.9 dB   |
| Peaking | 5765 Hz | 12.54 | 6.5 dB   |
| Peaking | 6220 Hz |  9.22 | 8.6 dB   |
| Peaking | 7617 Hz |  4.51 | -16.2 dB |
| Peaking | 178 Hz  |  1.02 | -1.9 dB  |
| Peaking | 3009 Hz |  5.53 | -4.2 dB  |
| Peaking | 3961 Hz |  2.32 | 3.6 dB   |
| Peaking | 5032 Hz |  9.79 | -6.6 dB  |
| Peaking | 9718 Hz |  7.5  | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ocharaku%20Flat-4%20Akakeyaki/Ocharaku%20Flat-4%20Akakeyaki.png)