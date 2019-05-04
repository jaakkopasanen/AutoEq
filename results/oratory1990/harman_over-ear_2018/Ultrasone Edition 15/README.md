# Ultrasone Edition 15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -3.3; 25 -4.1; 28 -5.1; 31 -5.9; 34 -6.6; 37 -7.2; 41 -7.8; 45 -8.4; 49 -8.9; 54 -9.6; 60 -10.2; 66 -10.6; 72 -11.0; 79 -11.4; 87 -12.0; 96 -12.5; 106 -12.9; 116 -13.1; 128 -13.1; 141 -13.0; 155 -12.7; 170 -12.3; 187 -12.0; 206 -11.8; 227 -11.5; 249 -11.2; 274 -10.7; 302 -10.4; 332 -9.8; 365 -9.3; 402 -8.6; 442 -9.2; 486 -9.8; 535 -9.3; 588 -8.8; 647 -8.1; 712 -7.6; 783 -7.2; 861 -7.0; 947 -6.8; 1042 -6.3; 1146 -5.8; 1261 -5.2; 1387 -4.8; 1526 -4.6; 1678 -4.6; 1846 -4.3; 2031 -5.5; 2234 -7.1; 2457 -6.5; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -3.4; 4788 -4.6; 5267 -6.0; 5793 -3.9; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -12.9; 15026 -13.0; 16529 -9.3; 18182 -8.2; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.82 | 6.2 dB  |
| Peaking | 128 Hz   | 0.42 | -6.6 dB |
| Peaking | 3363 Hz  | 1.97 | 6.8 dB  |
| Peaking | 6388 Hz  | 6.62 | 5.2 dB  |
| Peaking | 14600 Hz | 2.46 | -8.0 dB |
| Peaking | 532 Hz   | 3.78 | -1.4 dB |
| Peaking | 1997 Hz  | 0.96 | 2.8 dB  |
| Peaking | 2316 Hz  | 4.96 | -5.2 dB |
| Peaking | 11606 Hz | 2.19 | 2.2 dB  |
| Peaking | 15803 Hz | 0.04 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Ultrasone%20Edition%2015/Ultrasone%20Edition%2015.png)