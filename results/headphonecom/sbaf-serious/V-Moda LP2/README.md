# V-Moda LP2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.4; 25 -9.8; 28 -10.2; 31 -10.5; 34 -10.8; 37 -10.9; 41 -11.1; 45 -11.3; 49 -11.4; 54 -11.5; 60 -11.6; 66 -11.8; 72 -11.7; 79 -11.3; 87 -11.4; 96 -12.7; 106 -13.3; 116 -13.4; 128 -13.3; 141 -13.5; 155 -13.4; 170 -12.9; 187 -13.0; 206 -12.3; 227 -11.4; 249 -10.0; 274 -9.2; 302 -7.4; 332 -5.3; 365 -3.9; 402 -2.9; 442 -2.1; 486 -1.4; 535 -1.2; 588 -1.8; 647 -3.1; 712 -4.7; 783 -5.9; 861 -6.4; 947 -6.5; 1042 -6.5; 1146 -6.5; 1261 -6.4; 1387 -6.8; 1526 -6.7; 1678 -6.5; 1846 -5.8; 2031 -5.3; 2234 -5.9; 2457 -7.3; 2703 -7.7; 2973 -8.7; 3270 -7.3; 3597 -5.1; 3957 -3.1; 4353 -1.8; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda LP2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda LP2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.65 | -3.6 dB |
| Peaking | 158 Hz  | 0.64 | -7.0 dB |
| Peaking | 462 Hz  | 1.46 | 7.4 dB  |
| Peaking | 5320 Hz | 2.34 | 7.1 dB  |
| Peaking | 595 Hz  | 5.38 | 1.6 dB  |
| Peaking | 869 Hz  | 1.98 | -1.0 dB |
| Peaking | 3000 Hz | 4.63 | -3.3 dB |
| Peaking | 4143 Hz | 4.43 | 1.9 dB  |
| Peaking | 9828 Hz | 3.36 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 7.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20LP2/V-Moda%20LP2.png)