# Westone W40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.7; 31 -2.4; 34 -2.9; 37 -3.4; 41 -4.0; 45 -4.5; 49 -4.9; 54 -5.4; 60 -5.9; 66 -6.4; 72 -6.9; 79 -7.4; 87 -8.0; 96 -8.5; 106 -9.0; 116 -9.5; 128 -9.9; 141 -10.2; 155 -10.4; 170 -10.7; 187 -11.0; 206 -11.2; 227 -11.2; 249 -11.1; 274 -11.0; 302 -10.9; 332 -10.7; 365 -10.6; 402 -10.3; 442 -9.9; 486 -9.4; 535 -8.6; 588 -7.9; 647 -7.2; 712 -6.5; 783 -6.2; 861 -6.0; 947 -6.3; 1042 -7.1; 1146 -7.7; 1261 -7.9; 1387 -7.7; 1526 -7.3; 1678 -6.7; 1846 -6.0; 2031 -5.0; 2234 -3.7; 2457 -2.1; 2703 -1.3; 2973 -1.5; 3270 -2.2; 3597 -2.4; 3957 -2.0; 4353 -1.3; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.9; 9330 -11.4; 10263 -11.8; 11289 -8.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.1; 18182 -6.9; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.63 | 6.2 dB  |
| Peaking | 216 Hz   | 0.55 | -5.0 dB |
| Peaking | 2722 Hz  | 2.94 | 4.3 dB  |
| Peaking | 5363 Hz  | 1.28 | 6.7 dB  |
| Peaking | 9731 Hz  | 2.62 | -7.3 dB |
| Peaking | 473 Hz   | 1.19 | -2.6 dB |
| Peaking | 853 Hz   | 0.61 | 3.8 dB  |
| Peaking | 1279 Hz  | 1.36 | -4.1 dB |
| Peaking | 12602 Hz | 3.24 | 1.3 dB  |
| Peaking | 17226 Hz | 0.21 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Westone%20W40/Westone%20W40.png)