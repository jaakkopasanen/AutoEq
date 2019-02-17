# Philips SHP9500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.2; 45 -1.9; 49 -2.6; 54 -3.3; 60 -4.1; 66 -4.9; 72 -5.5; 79 -6.0; 87 -6.5; 96 -7.0; 106 -7.4; 116 -7.7; 128 -7.9; 141 -7.8; 155 -7.8; 170 -7.7; 187 -7.6; 206 -7.3; 227 -6.9; 249 -6.7; 274 -6.5; 302 -6.5; 332 -6.5; 365 -6.4; 402 -6.6; 442 -6.7; 486 -6.7; 535 -6.7; 588 -6.7; 647 -6.6; 712 -6.5; 783 -6.5; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.6; 1261 -7.1; 1387 -7.5; 1526 -7.4; 1678 -7.2; 1846 -7.0; 2031 -6.2; 2234 -5.2; 2457 -5.4; 2703 -7.1; 2973 -8.1; 3270 -8.2; 3597 -8.7; 3957 -10.6; 4353 -10.9; 4788 -11.0; 5267 -10.8; 5793 -11.3; 6373 -8.9; 7010 -6.6; 7711 -6.8; 8482 -8.6; 9330 -9.3; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -11.0; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHP9500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHP9500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.6  | 6.5 dB  |
| Peaking | 114 Hz   | 0.92 | -2.4 dB |
| Peaking | 4871 Hz  | 1.7  | -5.0 dB |
| Peaking | 18460 Hz | 2.17 | -4.6 dB |
| Peaking | 19518 Hz | 2.07 | -3.0 dB |
| Peaking | 1476 Hz  | 3.77 | -0.9 dB |
| Peaking | 2306 Hz  | 5.7  | 2.3 dB  |
| Peaking | 7441 Hz  | 3.77 | 4.2 dB  |
| Peaking | 8804 Hz  | 1.48 | -4.9 dB |
| Peaking | 10578 Hz | 1.29 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Philips%20SHP9500/Philips%20SHP9500.png)