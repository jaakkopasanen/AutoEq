# Marshall Major II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.6; 25 -6.5; 28 -6.5; 31 -6.4; 34 -6.3; 37 -6.1; 41 -5.9; 45 -5.7; 49 -5.7; 54 -5.7; 60 -5.8; 66 -6.0; 72 -6.1; 79 -6.2; 87 -6.4; 96 -6.4; 106 -6.6; 116 -6.7; 128 -6.6; 141 -6.5; 155 -6.4; 170 -6.2; 187 -5.8; 206 -5.3; 227 -4.7; 249 -4.5; 274 -4.6; 302 -5.2; 332 -5.7; 365 -6.2; 402 -7.0; 442 -7.9; 486 -8.3; 535 -8.4; 588 -8.2; 647 -7.8; 712 -7.3; 783 -6.9; 861 -6.7; 947 -6.6; 1042 -6.4; 1146 -5.8; 1261 -5.9; 1387 -5.7; 1526 -4.9; 1678 -4.3; 1846 -3.7; 2031 -3.0; 2234 -1.3; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.3; 7010 -6.2; 7711 -6.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall Major II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall Major II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 2.05 | 0.9 dB  |
| Peaking | 269 Hz  | 1.44 | 3.9 dB  |
| Peaking | 438 Hz  | 0.65 | -2.8 dB |
| Peaking | 3436 Hz | 0.79 | 6.9 dB  |
| Peaking | 375 Hz  | 7.09 | 0.7 dB  |
| Peaking | 2368 Hz | 6.16 | 1.5 dB  |
| Peaking | 3454 Hz | 3.07 | -1.1 dB |
| Peaking | 6031 Hz | 2.48 | 6.0 dB  |
| Peaking | 6950 Hz | 1.75 | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Marshall%20Major%20II/Marshall%20Major%20II.png)