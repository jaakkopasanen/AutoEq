# Beyerdynamic Aventho Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.7; 25 -3.4; 28 -4.3; 31 -5.1; 34 -5.7; 37 -6.1; 41 -6.6; 45 -7.0; 49 -7.3; 54 -7.7; 60 -8.4; 66 -9.1; 72 -9.8; 79 -10.5; 87 -11.2; 96 -11.9; 106 -12.5; 116 -12.7; 128 -12.7; 141 -12.3; 155 -11.6; 170 -10.6; 187 -9.4; 206 -8.3; 227 -7.6; 249 -6.8; 274 -6.1; 302 -6.2; 332 -6.7; 365 -7.0; 402 -7.0; 442 -6.9; 486 -7.1; 535 -7.2; 588 -7.3; 647 -7.5; 712 -7.8; 783 -8.1; 861 -8.2; 947 -8.1; 1042 -8.1; 1146 -8.0; 1261 -7.8; 1387 -7.4; 1526 -6.8; 1678 -6.1; 1846 -5.1; 2031 -3.9; 2234 -2.5; 2457 -0.5; 2703 -1.3; 2973 -1.8; 3270 -1.2; 3597 -0.7; 3957 -0.6; 4353 -1.5; 4788 -3.9; 5267 -5.7; 5793 -5.3; 6373 -1.6; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Aventho Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Aventho Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.71 | 4.4 dB  |
| Peaking | 115 Hz   | 0.95 | -7.1 dB |
| Peaking | 2496 Hz  | 4.47 | 4.6 dB  |
| Peaking | 3773 Hz  | 2.28 | 5.4 dB  |
| Peaking | 21810 Hz | 2.27 | 0.9 dB  |
| Peaking | 155 Hz   | 5.59 | -0.7 dB |
| Peaking | 269 Hz   | 3.12 | 1.6 dB  |
| Peaking | 932 Hz   | 1.19 | -2.5 dB |
| Peaking | 5433 Hz  | 5.81 | -1.8 dB |
| Peaking | 6546 Hz  | 7.69 | 4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20Aventho%20Wireless/Beyerdynamic%20Aventho%20Wireless.png)