# Ultrasone Edition 15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -3.2; 25 -4.0; 28 -5.0; 31 -5.8; 34 -6.6; 37 -7.2; 41 -7.8; 45 -8.3; 49 -8.8; 54 -9.5; 60 -10.2; 66 -10.5; 72 -10.9; 79 -11.3; 87 -12.0; 96 -12.4; 106 -12.9; 116 -13.0; 128 -13.1; 141 -12.9; 155 -12.7; 170 -12.2; 187 -12.0; 206 -11.7; 227 -11.4; 249 -11.2; 274 -10.5; 302 -10.3; 332 -9.7; 365 -9.2; 402 -8.4; 442 -9.2; 486 -9.7; 535 -9.2; 588 -8.7; 647 -8.1; 712 -7.5; 783 -7.1; 861 -6.9; 947 -6.7; 1042 -6.2; 1146 -5.7; 1261 -5.2; 1387 -4.7; 1526 -4.5; 1678 -4.6; 1846 -4.2; 2031 -5.5; 2234 -7.0; 2457 -6.5; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -3.5; 4788 -4.4; 5267 -6.0; 5793 -3.8; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -12.8; 15026 -12.9; 16529 -9.3; 18182 -8.1; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.85 | 6.1 dB  |
| Peaking | 127 Hz   | 0.43 | -6.5 dB |
| Peaking | 3363 Hz  | 1.93 | 6.7 dB  |
| Peaking | 6425 Hz  | 6.61 | 5.2 dB  |
| Peaking | 14712 Hz | 2.48 | -7.9 dB |
| Peaking | 529 Hz   | 3.74 | -1.4 dB |
| Peaking | 1963 Hz  | 0.95 | 2.8 dB  |
| Peaking | 2287 Hz  | 4.89 | -5.1 dB |
| Peaking | 11669 Hz | 2.84 | 2.0 dB  |
| Peaking | 15489 Hz | 0.05 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -6.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Ultrasone%20Edition%2015/Ultrasone%20Edition%2015.png)