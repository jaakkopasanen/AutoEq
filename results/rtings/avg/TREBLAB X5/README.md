# TREBLAB X5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.0; 25 -11.9; 28 -11.7; 31 -11.6; 34 -11.4; 37 -11.2; 41 -11.0; 45 -10.8; 49 -10.6; 54 -10.4; 60 -10.2; 66 -10.0; 72 -9.9; 79 -9.8; 87 -9.6; 96 -9.5; 106 -9.3; 116 -9.1; 128 -8.8; 141 -8.5; 155 -8.4; 170 -8.3; 187 -8.0; 206 -7.7; 227 -7.2; 249 -6.7; 274 -6.1; 302 -5.6; 332 -5.1; 365 -4.5; 402 -4.0; 442 -3.5; 486 -2.9; 535 -2.3; 588 -1.7; 647 -1.1; 712 -0.8; 783 -0.5; 861 -0.5; 947 -0.9; 1042 -1.6; 1146 -2.4; 1261 -3.1; 1387 -3.5; 1526 -3.8; 1678 -4.1; 1846 -4.4; 2031 -4.9; 2234 -5.1; 2457 -5.1; 2703 -5.2; 2973 -5.1; 3270 -4.6; 3597 -3.9; 3957 -3.3; 4353 -3.3; 4788 -3.9; 5267 -4.5; 5793 -6.1; 6373 -8.9; 7010 -9.2; 7711 -5.6; 8482 -4.7; 9330 -4.8; 10263 -8.6; 11289 -9.5; 12418 -5.3; 13660 -4.8; 15026 -8.6; 16529 -13.3; 18182 -12.3; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TREBLAB X5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TREBLAB X5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.22 | -7.0 dB |
| Peaking | 162 Hz   | 0.79 | -2.1 dB |
| Peaking | 752 Hz   | 1.1  | 4.7 dB  |
| Peaking | 6702 Hz  | 6.17 | -5.3 dB |
| Peaking | 17516 Hz | 1.1  | -9.2 dB |
| Peaking | 2542 Hz  | 1.69 | -1.0 dB |
| Peaking | 4169 Hz  | 2.87 | 2.0 dB  |
| Peaking | 9252 Hz  | 3.77 | 2.5 dB  |
| Peaking | 10822 Hz | 3.22 | -5.4 dB |
| Peaking | 13314 Hz | 3.16 | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -7.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/TREBLAB%20X5/TREBLAB%20X5.png)