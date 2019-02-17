# Sony WI-SP500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.4; 72 -2.5; 79 -3.8; 87 -5.1; 96 -6.2; 106 -7.3; 116 -8.2; 128 -9.0; 141 -9.6; 155 -10.0; 170 -10.3; 187 -10.6; 206 -10.7; 227 -10.9; 249 -11.0; 274 -11.1; 302 -11.2; 332 -11.3; 365 -11.5; 402 -11.6; 442 -11.6; 486 -11.4; 535 -11.2; 588 -10.7; 647 -10.0; 712 -8.9; 783 -7.7; 861 -6.7; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -6.6; 1387 -6.2; 1526 -5.7; 1678 -5.6; 1846 -6.0; 2031 -6.7; 2234 -7.2; 2457 -7.2; 2703 -6.4; 2973 -4.8; 3270 -3.6; 3597 -3.4; 3957 -4.0; 4353 -5.8; 4788 -8.7; 5267 -13.4; 5793 -12.8; 6373 -8.6; 7010 -6.9; 7711 -8.4; 8482 -10.1; 9330 -8.1; 10263 -6.5; 11289 -7.9; 12418 -9.0; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-SP500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-SP500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.42 | 9.7 dB  |
| Peaking | 170 Hz   | 0.35 | -7.7 dB |
| Peaking | 3648 Hz  | 2.44 | 4.0 dB  |
| Peaking | 5465 Hz  | 4.78 | -8.9 dB |
| Peaking | 8516 Hz  | 5.31 | -3.6 dB |
| Peaking | 541 Hz   | 2.21 | -1.8 dB |
| Peaking | 887 Hz   | 3.42 | 1.7 dB  |
| Peaking | 1855 Hz  | 1.18 | 2.1 dB  |
| Peaking | 2263 Hz  | 2.45 | -2.6 dB |
| Peaking | 12121 Hz | 7.21 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -4.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-SP500/Sony%20WI-SP500.png)