# Sony WI-SP600N
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.8; 25 -10.1; 28 -10.3; 31 -10.4; 34 -10.5; 37 -10.5; 41 -10.5; 45 -10.4; 49 -10.2; 54 -10.1; 60 -10.1; 66 -10.1; 72 -10.0; 79 -9.9; 87 -9.8; 96 -9.8; 106 -9.8; 116 -9.8; 128 -9.8; 141 -9.6; 155 -9.4; 170 -9.3; 187 -9.1; 206 -8.9; 227 -8.5; 249 -8.1; 274 -7.5; 302 -6.9; 332 -6.4; 365 -5.8; 402 -5.4; 442 -4.9; 486 -4.4; 535 -3.9; 588 -3.3; 647 -2.6; 712 -2.0; 783 -1.4; 861 -1.0; 947 -0.9; 1042 -0.9; 1146 -1.9; 1261 -3.0; 1387 -3.6; 1526 -3.7; 1678 -3.7; 1846 -3.6; 2031 -3.5; 2234 -2.7; 2457 -1.8; 2703 -1.7; 2973 -2.4; 3270 -3.2; 3597 -3.4; 3957 -2.5; 4353 -1.6; 4788 -0.9; 5267 -0.6; 5793 -2.3; 6373 -8.2; 7010 -3.0; 7711 -0.5; 8482 -0.8; 9330 -1.0; 10263 -8.1; 11289 -12.0; 12418 -7.8; 13660 -1.5; 15026 -0.8; 16529 -5.5; 18182 -11.5; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-SP600N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-SP600N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.2  | -9.3 dB  |
| Peaking | 223 Hz   | 0.69 | -4.2 dB  |
| Peaking | 2430 Hz  | 0.63 | -2.0 dB  |
| Peaking | 11260 Hz | 4.21 | -11.8 dB |
| Peaking | 18699 Hz | 1.38 | -12.1 dB |
| Peaking | 909 Hz   | 4.06 | 1.8 dB   |
| Peaking | 5351 Hz  | 3.95 | 2.4 dB   |
| Peaking | 6398 Hz  | 5.93 | -8.3 dB  |
| Peaking | 7839 Hz  | 2.58 | 2.8 dB   |
| Peaking | 17348 Hz | 6.81 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-SP600N/Sony%20WI-SP600N.png)