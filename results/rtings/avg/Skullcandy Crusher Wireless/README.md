# Skullcandy Crusher Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.2; 23 -13.8; 25 -13.5; 28 -12.9; 31 -12.3; 34 -11.7; 37 -11.0; 41 -10.0; 45 -9.2; 49 -9.4; 54 -11.1; 60 -10.0; 66 -9.4; 72 -10.0; 79 -10.7; 87 -11.5; 96 -12.0; 106 -12.2; 116 -12.1; 128 -11.8; 141 -11.6; 155 -10.9; 170 -10.2; 187 -9.4; 206 -8.3; 227 -7.2; 249 -6.3; 274 -5.9; 302 -5.3; 332 -4.5; 365 -3.9; 402 -3.3; 442 -3.0; 486 -3.0; 535 -2.8; 588 -2.5; 647 -2.1; 712 -2.0; 783 -3.0; 861 -2.8; 947 -2.2; 1042 -1.9; 1146 -1.5; 1261 -0.9; 1387 -0.6; 1526 -0.5; 1678 -0.7; 1846 -1.3; 2031 -1.8; 2234 -1.7; 2457 -1.5; 2703 -2.5; 2973 -4.0; 3270 -5.2; 3597 -4.8; 3957 -3.5; 4353 -3.0; 4788 -2.7; 5267 -3.3; 5793 -4.8; 6373 -6.4; 7010 -7.7; 7711 -7.7; 8482 -7.8; 9330 -8.4; 10263 -8.1; 11289 -9.0; 12418 -11.8; 13660 -11.0; 15026 -7.4; 16529 -5.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.81 | -9.3 dB |
| Peaking | 25 Hz    | 0.76 | -4.8 dB |
| Peaking | 121 Hz   | 0.82 | -7.3 dB |
| Peaking | 1139 Hz  | 0.34 | 3.6 dB  |
| Peaking | 12185 Hz | 0.95 | -6.1 dB |
| Peaking | 857 Hz   | 3.97 | -1.6 dB |
| Peaking | 3353 Hz  | 2.36 | -5.1 dB |
| Peaking | 4283 Hz  | 0.69 | 3.7 dB  |
| Peaking | 6909 Hz  | 2.13 | -3.8 dB |
| Peaking | 17402 Hz | 1.94 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Crusher%20Wireless/Skullcandy%20Crusher%20Wireless.png)