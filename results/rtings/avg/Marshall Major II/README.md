# Marshall Major II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.6; 25 -7.5; 28 -7.4; 31 -7.4; 34 -7.3; 37 -7.1; 41 -6.9; 45 -6.7; 49 -6.6; 54 -6.7; 60 -6.8; 66 -7.0; 72 -7.0; 79 -7.2; 87 -7.3; 96 -7.4; 106 -7.5; 116 -7.6; 128 -7.6; 141 -7.5; 155 -7.4; 170 -7.2; 187 -6.8; 206 -6.2; 227 -5.7; 249 -5.4; 274 -5.6; 302 -6.1; 332 -6.6; 365 -7.1; 402 -7.9; 442 -8.8; 486 -9.2; 535 -9.3; 588 -9.1; 647 -8.7; 712 -8.3; 783 -7.9; 861 -7.6; 947 -7.6; 1042 -7.3; 1146 -6.8; 1261 -6.9; 1387 -6.7; 1526 -5.9; 1678 -5.2; 1846 -4.7; 2031 -3.9; 2234 -2.3; 2457 -0.9; 2703 -0.6; 2973 -1.1; 3270 -1.6; 3597 -1.4; 3957 -0.8; 4353 -0.8; 4788 -1.1; 5267 -0.6; 5793 -0.5; 6373 -3.3; 7010 -7.1; 7711 -7.6; 8482 -5.3; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.3; 18182 -7.5; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall Major II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall Major II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.33 | -2.4 dB |
| Peaking | 116 Hz  | 1.45 | -2.0 dB |
| Peaking | 625 Hz  | 0.88 | -3.8 dB |
| Peaking | 2720 Hz | 2.07 | 4.7 dB  |
| Peaking | 4805 Hz | 2.29 | 4.6 dB  |
| Peaking | 264 Hz  | 3.76 | 1.3 dB  |
| Peaking | 466 Hz  | 5.26 | -1.0 dB |
| Peaking | 5785 Hz | 8.23 | 1.8 dB  |
| Peaking | 6116 Hz | 6.51 | 1.6 dB  |
| Peaking | 7296 Hz | 4.47 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | -3.8 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Marshall%20Major%20II/Marshall%20Major%20II.png)