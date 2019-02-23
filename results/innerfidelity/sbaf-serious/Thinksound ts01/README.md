# Thinksound ts01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.4; 25 -10.4; 28 -10.5; 31 -10.5; 34 -10.6; 37 -10.7; 41 -10.8; 45 -10.9; 49 -11.0; 54 -11.2; 60 -11.4; 66 -11.6; 72 -11.9; 79 -12.2; 87 -12.5; 96 -12.8; 106 -12.9; 116 -13.0; 128 -13.1; 141 -13.2; 155 -13.1; 170 -13.0; 187 -12.8; 206 -12.6; 227 -12.1; 249 -11.8; 274 -11.3; 302 -10.8; 332 -10.2; 365 -9.6; 402 -9.0; 442 -8.1; 486 -7.6; 535 -6.9; 588 -5.9; 647 -5.3; 712 -4.7; 783 -3.9; 861 -3.7; 947 -3.5; 1042 -3.6; 1146 -3.0; 1261 -2.7; 1387 -3.0; 1526 -3.2; 1678 -3.3; 1846 -3.1; 2031 -2.8; 2234 -2.7; 2457 -2.7; 2703 -3.0; 2973 -2.9; 3270 -1.9; 3597 -0.5; 3957 -0.5; 4353 -2.2; 4788 -3.5; 5267 -5.3; 5793 -10.5; 6373 -10.1; 7010 -4.5; 7711 -6.0; 8482 -6.2; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksound ts01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound ts01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.36 | -3.6 dB |
| Peaking | 101 Hz  | 0.69 | -2.8 dB |
| Peaking | 218 Hz  | 0.53 | -5.2 dB |
| Peaking | 1184 Hz | 0.55 | 4.0 dB  |
| Peaking | 3736 Hz | 3.41 | 5.4 dB  |
| Peaking | 1592 Hz | 3.48 | -0.6 dB |
| Peaking | 2343 Hz | 3.25 | 1.0 dB  |
| Peaking | 5007 Hz | 3.47 | 2.1 dB  |
| Peaking | 6059 Hz | 4.93 | -8.0 dB |
| Peaking | 6957 Hz | 7.34 | 3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20ts01/Thinksound%20ts01.png)