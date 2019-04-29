# Ocharaku Flat-4 Akazakura
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.3; 25 -6.6; 28 -6.9; 31 -7.1; 34 -7.3; 37 -7.5; 41 -7.7; 45 -7.9; 49 -8.0; 54 -8.2; 60 -8.4; 66 -8.7; 72 -8.9; 79 -9.2; 87 -9.5; 96 -9.8; 106 -10.1; 116 -10.3; 128 -10.5; 141 -10.5; 155 -10.6; 170 -10.5; 187 -10.4; 206 -10.2; 227 -10.0; 249 -9.7; 274 -9.4; 302 -9.1; 332 -8.6; 365 -8.1; 402 -7.8; 442 -7.5; 486 -7.2; 535 -7.0; 588 -6.8; 647 -6.5; 712 -6.3; 783 -6.1; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -7.1; 1261 -7.2; 1387 -6.4; 1526 -4.5; 1678 -1.7; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.2; 2973 -5.1; 3270 -6.6; 3597 -4.6; 3957 -3.2; 4353 -3.5; 4788 -7.2; 5267 -6.5; 5793 -0.5; 6373 -2.4; 7010 -10.8; 7711 -15.1; 8482 -15.0; 9330 -10.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.3; 15026 -27.1; 16529 -31.7; 18182 -29.8; 20000 -31.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat-4 Akazakura GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat-4 Akazakura ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 149 Hz   |  0.53 | -4.2 dB  |
| Peaking | 2151 Hz  |  2.1  | 6.4 dB   |
| Peaking | 8268 Hz  |  3.7  | -15.0 dB |
| Peaking | 10171 Hz |  0.32 | 29.1 dB  |
| Peaking | 16854 Hz |  0.26 | -43.0 dB |
| Peaking | 1256 Hz  |  5.54 | -2.3 dB  |
| Peaking | 5057 Hz  | 13.69 | -6.3 dB  |
| Peaking | 5834 Hz  |  5.53 | 7.2 dB   |
| Peaking | 12904 Hz |  2.99 | 13.3 dB  |
| Peaking | 13555 Hz |  1.08 | -7.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -27.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ocharaku%20Flat-4%20Akazakura/Ocharaku%20Flat-4%20Akazakura.png)