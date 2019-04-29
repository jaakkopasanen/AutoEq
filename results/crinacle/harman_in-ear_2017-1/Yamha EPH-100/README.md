# Yamha EPH-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.9; 25 -11.1; 28 -11.4; 31 -11.6; 34 -11.7; 37 -11.8; 41 -11.8; 45 -11.9; 49 -11.9; 54 -12.0; 60 -12.1; 66 -12.2; 72 -12.3; 79 -12.4; 87 -12.5; 96 -12.6; 106 -12.7; 116 -12.6; 128 -12.6; 141 -12.5; 155 -12.4; 170 -12.2; 187 -11.9; 206 -11.6; 227 -11.2; 249 -10.9; 274 -10.5; 302 -10.0; 332 -9.5; 365 -9.1; 402 -8.6; 442 -8.3; 486 -7.9; 535 -7.5; 588 -7.1; 647 -6.8; 712 -6.4; 783 -6.1; 861 -5.9; 947 -6.0; 1042 -6.5; 1146 -7.4; 1261 -8.3; 1387 -8.6; 1526 -8.5; 1678 -8.5; 1846 -8.8; 2031 -9.2; 2234 -9.2; 2457 -7.8; 2703 -4.9; 2973 -1.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.6; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.0; 13660 -20.3; 15026 -32.6; 16529 -37.8; 18182 -32.7; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamha EPH-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamha EPH-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.54 | -3.6 dB  |
| Peaking | 132 Hz   | 0.42 | -5.6 dB  |
| Peaking | 8173 Hz  | 0.46 | 14.9 dB  |
| Peaking | 16597 Hz | 0.75 | -39.1 dB |
| Peaking | 2112 Hz  | 0.96 | -15.0 dB |
| Peaking | 2721 Hz  | 0.52 | 11.3 dB  |
| Peaking | 7865 Hz  | 2.15 | -6.5 dB  |
| Peaking | 12234 Hz | 2.79 | 8.6 dB   |
| Peaking | 14780 Hz | 2.56 | -8.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 9.7 dB   |
| Peaking | 16000 Hz | 1.41 | -36.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Yamha%20EPH-100/Yamha%20EPH-100.png)