# Sony WH-CH500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.2; 34 -2.7; 37 -4.5; 41 -6.5; 45 -8.0; 49 -9.2; 54 -10.4; 60 -11.3; 66 -12.0; 72 -12.3; 79 -12.2; 87 -12.0; 96 -11.5; 106 -11.0; 116 -10.4; 128 -9.8; 141 -9.1; 155 -8.5; 170 -7.9; 187 -7.4; 206 -6.9; 227 -6.6; 249 -6.3; 274 -6.2; 302 -6.1; 332 -6.1; 365 -5.9; 402 -5.4; 442 -5.5; 486 -6.0; 535 -6.5; 588 -6.6; 647 -6.3; 712 -6.1; 783 -6.2; 861 -6.3; 947 -6.7; 1042 -6.7; 1146 -6.7; 1261 -7.1; 1387 -7.2; 1526 -7.2; 1678 -7.1; 1846 -6.9; 2031 -6.6; 2234 -5.7; 2457 -5.3; 2703 -5.7; 2973 -6.7; 3270 -6.9; 3597 -6.6; 3957 -4.1; 4353 -1.1; 4788 -0.5; 5267 -2.0; 5793 -1.3; 6373 -3.9; 7010 -6.2; 7711 -8.9; 8482 -10.7; 9330 -12.3; 10263 -10.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-CH500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-CH500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.22 | 7.8 dB  |
| Peaking | 73 Hz   | 0.97 | -7.0 dB |
| Peaking | 5079 Hz | 2.32 | 6.5 dB  |
| Peaking | 8219 Hz | 3.97 | -3.5 dB |
| Peaking | 9572 Hz | 4.79 | -5.7 dB |
| Peaking | 366 Hz  | 1.34 | 1.1 dB  |
| Peaking | 1565 Hz | 1.86 | -0.9 dB |
| Peaking | 2459 Hz | 3.99 | 1.5 dB  |
| Peaking | 3413 Hz | 2.81 | -2.1 dB |
| Peaking | 4320 Hz | 6.92 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -7.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-CH500/Sony%20WH-CH500.png)