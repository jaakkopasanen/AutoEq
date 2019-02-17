# Creative HN-900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.6; 45 -3.1; 49 -4.7; 54 -6.4; 60 -7.2; 66 -6.4; 72 -8.2; 79 -11.1; 87 -13.2; 96 -14.3; 106 -15.0; 116 -15.4; 128 -15.5; 141 -15.3; 155 -15.2; 170 -15.0; 187 -14.4; 206 -13.9; 227 -13.3; 249 -12.8; 274 -12.3; 302 -11.8; 332 -11.4; 365 -11.0; 402 -10.9; 442 -11.0; 486 -11.4; 535 -12.1; 588 -13.0; 647 -13.8; 712 -13.5; 783 -12.0; 861 -9.5; 947 -7.2; 1042 -6.9; 1146 -8.4; 1261 -6.5; 1387 -4.5; 1526 -3.6; 1678 -2.5; 1846 -0.6; 2031 -1.5; 2234 -2.9; 2457 -4.7; 2703 -2.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.3; 5267 -7.5; 5793 -6.2; 6373 -7.4; 7010 -6.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.9; 13660 -14.2; 15026 -13.8; 16529 -11.5; 18182 -10.9; 20000 -13.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative HN-900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative HN-900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.38 | 10.4 dB  |
| Peaking | 113 Hz   | 0.5  | -13.9 dB |
| Peaking | 673 Hz   | 1.98 | -6.7 dB  |
| Peaking | 2888 Hz  | 0.64 | 5.8 dB   |
| Peaking | 17103 Hz | 0.44 | -6.4 dB  |
| Peaking | 2499 Hz  | 8.61 | -4.2 dB  |
| Peaking | 4701 Hz  | 2.23 | 8.0 dB   |
| Peaking | 5208 Hz  | 2.76 | -9.4 dB  |
| Peaking | 10876 Hz | 4.23 | 2.9 dB   |
| Peaking | 20028 Hz | 4.02 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -9.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -5.1 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -8.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20HN-900/Creative%20HN-900.png)