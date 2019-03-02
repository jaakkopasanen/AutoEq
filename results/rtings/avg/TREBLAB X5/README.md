# TREBLAB X5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.3; 25 -7.2; 28 -7.0; 31 -6.8; 34 -6.7; 37 -6.5; 41 -6.3; 45 -6.1; 49 -5.9; 54 -5.8; 60 -5.9; 66 -6.0; 72 -6.0; 79 -6.1; 87 -6.3; 96 -6.5; 106 -6.7; 116 -7.0; 128 -7.2; 141 -7.4; 155 -7.6; 170 -7.8; 187 -7.7; 206 -7.7; 227 -7.4; 249 -6.9; 274 -6.3; 302 -5.8; 332 -5.3; 365 -4.7; 402 -4.2; 442 -3.6; 486 -3.0; 535 -2.4; 588 -1.8; 647 -1.2; 712 -0.8; 783 -0.5; 861 -0.5; 947 -0.9; 1042 -1.6; 1146 -2.4; 1261 -3.0; 1387 -3.5; 1526 -3.8; 1678 -4.0; 1846 -4.3; 2031 -4.5; 2234 -4.4; 2457 -4.3; 2703 -4.8; 2973 -5.2; 3270 -4.9; 3597 -4.3; 3957 -3.8; 4353 -3.9; 4788 -3.6; 5267 -4.2; 5793 -6.3; 6373 -10.1; 7010 -9.1; 7711 -5.0; 8482 -4.6; 9330 -5.6; 10263 -9.2; 11289 -8.6; 12418 -5.1; 13660 -4.8; 15026 -9.2; 16529 -13.5; 18182 -12.5; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TREBLAB X5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TREBLAB X5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 167 Hz   | 0.51 | -3.1 dB |
| Peaking | 736 Hz   | 1.05 | 4.8 dB  |
| Peaking | 10620 Hz | 4.51 | -4.7 dB |
| Peaking | 16546 Hz | 2.54 | -6.4 dB |
| Peaking | 18320 Hz | 1.18 | -6.8 dB |
| Peaking | 24 Hz    | 1.48 | -2.7 dB |
| Peaking | 5037 Hz  | 2.99 | 2.2 dB  |
| Peaking | 6634 Hz  | 3.54 | -6.9 dB |
| Peaking | 8028 Hz  | 3.53 | 2.6 dB  |
| Peaking | 13321 Hz | 4.97 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -8.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/TREBLAB%20X5/TREBLAB%20X5.png)