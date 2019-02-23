# Thinksound ts02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.7; 25 -10.7; 28 -10.9; 31 -11.0; 34 -11.1; 37 -11.1; 41 -11.2; 45 -11.4; 49 -11.5; 54 -11.7; 60 -12.0; 66 -12.1; 72 -12.4; 79 -12.7; 87 -12.8; 96 -13.1; 106 -13.1; 116 -13.2; 128 -13.3; 141 -13.3; 155 -13.3; 170 -13.2; 187 -12.9; 206 -12.7; 227 -12.3; 249 -11.9; 274 -11.4; 302 -10.7; 332 -10.1; 365 -9.3; 402 -8.6; 442 -8.0; 486 -7.5; 535 -6.7; 588 -5.9; 647 -5.1; 712 -4.4; 783 -3.8; 861 -3.4; 947 -3.2; 1042 -3.4; 1146 -2.3; 1261 -2.3; 1387 -2.5; 1526 -2.8; 1678 -2.8; 1846 -2.5; 2031 -2.3; 2234 -2.0; 2457 -2.0; 2703 -2.3; 2973 -2.5; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -1.6; 4788 -3.3; 5267 -5.3; 5793 -10.8; 6373 -9.5; 7010 -5.0; 7711 -6.2; 8482 -6.6; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksound ts02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound ts02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.32 | -3.7 dB  |
| Peaking | 102 Hz  | 0.64 | -3.4 dB  |
| Peaking | 221 Hz  | 0.66 | -4.5 dB  |
| Peaking | 1310 Hz | 0.58 | 4.6 dB   |
| Peaking | 3720 Hz | 2.99 | 5.3 dB   |
| Peaking | 1560 Hz | 4.02 | -0.7 dB  |
| Peaking | 2355 Hz | 4.46 | 1.2 dB   |
| Peaking | 6014 Hz | 1.71 | 3.3 dB   |
| Peaking | 6014 Hz | 5.62 | -10.3 dB |
| Peaking | 9183 Hz | 5.35 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Thinksound%20ts02/Thinksound%20ts02.png)