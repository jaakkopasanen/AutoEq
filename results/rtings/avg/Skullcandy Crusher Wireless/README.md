# Skullcandy Crusher Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.2; 23 -13.8; 25 -13.5; 28 -12.9; 31 -12.3; 34 -11.7; 37 -11.0; 41 -10.0; 45 -9.2; 49 -9.4; 54 -11.1; 60 -10.0; 66 -9.4; 72 -10.0; 79 -10.7; 87 -11.5; 96 -12.0; 106 -12.2; 116 -12.1; 128 -11.8; 141 -11.6; 155 -10.9; 170 -10.2; 187 -9.4; 206 -8.3; 227 -7.2; 249 -6.3; 274 -5.9; 302 -5.3; 332 -4.5; 365 -3.9; 402 -3.3; 442 -3.0; 486 -3.0; 535 -2.8; 588 -2.5; 647 -2.1; 712 -2.0; 783 -3.0; 861 -2.8; 947 -2.2; 1042 -1.9; 1146 -1.5; 1261 -0.9; 1387 -0.6; 1526 -0.5; 1678 -0.7; 1846 -1.3; 2031 -1.8; 2234 -1.7; 2457 -1.5; 2703 -2.5; 2973 -4.0; 3270 -5.2; 3597 -4.8; 3957 -3.5; 4353 -3.0; 4788 -2.7; 5267 -3.3; 5793 -4.8; 6373 -6.4; 7010 -7.7; 7711 -7.7; 8482 -7.8; 9330 -8.4; 10263 -8.1; 11289 -9.0; 12418 -11.8; 13660 -11.0; 15026 -7.4; 16529 -5.8; 18182 -3.4; 20000 -2.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 1.05 | -12.2 dB |
| Peaking | 21 Hz    | 0.38 | -7.6 dB  |
| Peaking | 126 Hz   | 0.79 | -8.8 dB  |
| Peaking | 7577 Hz  | 1.59 | -4.1 dB  |
| Peaking | 13017 Hz | 1.21 | -9.2 dB  |
| Peaking | 427 Hz   | 4.19 | 0.5 dB   |
| Peaking | 1484 Hz  | 2.39 | 1.9 dB   |
| Peaking | 2482 Hz  | 3.92 | 1.1 dB   |
| Peaking | 3279 Hz  | 3.56 | -3.0 dB  |
| Peaking | 4900 Hz  | 5.09 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -9.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.8 dB  |
| Peaking | 16000 Hz | 1.41 | -7.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Crusher%20Wireless/Skullcandy%20Crusher%20Wireless.png)