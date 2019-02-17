# Beyerdynamic Aventho Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.1; 28 -3.0; 31 -3.7; 34 -4.3; 37 -4.8; 41 -5.3; 45 -5.6; 49 -6.0; 54 -6.4; 60 -7.0; 66 -7.7; 72 -8.4; 79 -9.2; 87 -9.9; 96 -10.6; 106 -11.1; 116 -11.4; 128 -11.3; 141 -11.0; 155 -10.3; 170 -9.3; 187 -8.0; 206 -7.0; 227 -6.3; 249 -5.5; 274 -4.7; 302 -4.8; 332 -5.3; 365 -5.7; 402 -5.7; 442 -5.6; 486 -5.8; 535 -5.9; 588 -6.0; 647 -6.2; 712 -6.5; 783 -6.7; 861 -6.9; 947 -6.8; 1042 -6.8; 1146 -6.7; 1261 -6.4; 1387 -6.0; 1526 -5.5; 1678 -4.7; 1846 -3.7; 2031 -2.6; 2234 -1.2; 2457 -0.7; 2703 -0.7; 2973 -0.7; 3270 -0.7; 3597 -0.7; 3957 -0.7; 4353 -0.7; 4788 -2.6; 5267 -4.4; 5793 -3.9; 6373 -1.5; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Aventho Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Aventho Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.64 | 8.2 dB  |
| Peaking | 124 Hz  | 0.96 | -5.6 dB |
| Peaking | 269 Hz  | 1.23 | 3.2 dB  |
| Peaking | 2388 Hz | 2.39 | 3.9 dB  |
| Peaking | 3908 Hz | 1.18 | 5.6 dB  |
| Peaking | 539 Hz  | 2.86 | 0.5 dB  |
| Peaking | 996 Hz  | 2.02 | -0.7 dB |
| Peaking | 5336 Hz | 6.94 | -1.7 dB |
| Peaking | 6506 Hz | 5.99 | 4.0 dB  |
| Peaking | 7988 Hz | 2.08 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | 2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20Aventho%20Wireless/Beyerdynamic%20Aventho%20Wireless.png)