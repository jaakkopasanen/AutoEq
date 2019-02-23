# Sony WI-SP600N
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.8; 25 -10.0; 28 -10.2; 31 -10.3; 34 -10.4; 37 -10.4; 41 -10.4; 45 -10.3; 49 -10.1; 54 -10.0; 60 -10.0; 66 -10.0; 72 -9.9; 79 -9.8; 87 -9.7; 96 -9.7; 106 -9.7; 116 -9.7; 128 -9.7; 141 -9.6; 155 -9.4; 170 -9.2; 187 -9.0; 206 -8.8; 227 -8.4; 249 -8.0; 274 -7.4; 302 -6.8; 332 -6.3; 365 -5.8; 402 -5.3; 442 -4.8; 486 -4.3; 535 -3.8; 588 -3.2; 647 -2.5; 712 -1.9; 783 -1.3; 861 -1.0; 947 -0.8; 1042 -0.8; 1146 -1.8; 1261 -2.9; 1387 -3.5; 1526 -3.6; 1678 -3.6; 1846 -3.6; 2031 -3.4; 2234 -2.6; 2457 -1.7; 2703 -1.6; 2973 -2.3; 3270 -3.1; 3597 -3.3; 3957 -2.4; 4353 -1.5; 4788 -0.8; 5267 -0.5; 5793 -2.3; 6373 -8.2; 7010 -3.0; 7711 -3.8; 8482 -4.0; 9330 -4.0; 10263 -8.0; 11289 -11.9; 12418 -7.7; 13660 -4.1; 15026 -4.1; 16529 -5.6; 18182 -11.4; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-SP600N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-SP600N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.23 | -6.1 dB |
| Peaking | 216 Hz   | 0.79 | -3.6 dB |
| Peaking | 1097 Hz  | 0.15 | 2.1 dB  |
| Peaking | 11250 Hz | 4.45 | -8.9 dB |
| Peaking | 18643 Hz | 1.65 | -8.4 dB |
| Peaking | 960 Hz   | 2.22 | 2.6 dB  |
| Peaking | 1499 Hz  | 1.57 | -2.1 dB |
| Peaking | 5271 Hz  | 3.42 | 2.9 dB  |
| Peaking | 6377 Hz  | 9.48 | -6.4 dB |
| Peaking | 14998 Hz | 2.75 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-SP600N/Sony%20WI-SP600N.png)