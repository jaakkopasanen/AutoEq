# Sony WI-SP500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.2; 60 -2.3; 66 -3.4; 72 -4.4; 79 -5.4; 87 -6.4; 96 -7.2; 106 -7.8; 116 -8.2; 128 -8.5; 141 -8.7; 155 -8.7; 170 -8.7; 187 -8.7; 206 -8.6; 227 -8.6; 249 -8.7; 274 -8.8; 302 -8.9; 332 -9.0; 365 -9.2; 402 -9.3; 442 -9.3; 486 -9.2; 535 -9.0; 588 -8.6; 647 -7.8; 712 -6.7; 783 -5.5; 861 -4.6; 947 -4.3; 1042 -4.5; 1146 -4.6; 1261 -4.5; 1387 -4.1; 1526 -3.7; 1678 -3.6; 1846 -4.1; 2031 -5.0; 2234 -5.8; 2457 -5.8; 2703 -4.6; 2973 -2.5; 3270 -1.1; 3597 -0.8; 3957 -1.5; 4353 -3.3; 4788 -7.0; 5267 -11.7; 5793 -10.3; 6373 -5.4; 7010 -4.7; 7711 -7.0; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -7.0; 12418 -7.2; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-SP500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-SP500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.61 | 8.5 dB  |
| Peaking | 330 Hz  | 0.13 | -3.8 dB |
| Peaking | 1192 Hz | 0.83 | 5.7 dB  |
| Peaking | 3640 Hz | 2.06 | 6.7 dB  |
| Peaking | 5390 Hz | 6.19 | -7.7 dB |
| Peaking | 878 Hz  | 2.9  | 2.4 dB  |
| Peaking | 1142 Hz | 0.84 | -1.7 dB |
| Peaking | 1643 Hz | 3.25 | 2.1 dB  |
| Peaking | 6842 Hz | 5.04 | 4.2 dB  |
| Peaking | 7298 Hz | 2.07 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-SP500/Sony%20WI-SP500.png)