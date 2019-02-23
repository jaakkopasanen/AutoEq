# Yamaha HP1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.4; 25 -3.8; 28 -4.3; 31 -4.7; 34 -5.1; 37 -5.3; 41 -5.6; 45 -5.9; 49 -6.1; 54 -6.3; 60 -6.6; 66 -6.8; 72 -7.0; 79 -7.2; 87 -7.5; 96 -7.9; 106 -8.2; 116 -8.4; 128 -8.8; 141 -9.0; 155 -9.2; 170 -9.2; 187 -9.4; 206 -9.5; 227 -9.5; 249 -9.6; 274 -9.3; 302 -9.3; 332 -9.3; 365 -9.3; 402 -9.4; 442 -9.2; 486 -9.3; 535 -9.4; 588 -9.1; 647 -9.2; 712 -9.3; 783 -9.0; 861 -8.8; 947 -8.5; 1042 -8.0; 1146 -7.2; 1261 -6.0; 1387 -5.5; 1526 -5.5; 1678 -5.0; 1846 -5.2; 2031 -6.2; 2234 -7.8; 2457 -7.0; 2703 -7.1; 2973 -5.3; 3270 -3.8; 3597 -3.1; 3957 -3.7; 4353 -4.8; 4788 -3.7; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HP1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 778 Hz  | 0.1  | -3.3 dB |
| Peaking | 1550 Hz | 1.53 | 4.5 dB  |
| Peaking | 3534 Hz | 3.14 | 4.8 dB  |
| Peaking | 5778 Hz | 2.37 | 8.1 dB  |
| Peaking | 17 Hz   | 0.72 | 4.0 dB  |
| Peaking | 68 Hz   | 1.78 | 0.6 dB  |
| Peaking | 1927 Hz | 6.39 | 0.8 dB  |
| Peaking | 2255 Hz | 5.63 | -1.0 dB |
| Peaking | 3016 Hz | 5.71 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP1/Yamaha%20HP1.png)