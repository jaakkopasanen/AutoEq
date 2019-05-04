# Skullcandy Crusher Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -13.4; 25 -13.0; 28 -12.5; 31 -11.9; 34 -11.2; 37 -10.5; 41 -9.5; 45 -9.0; 49 -9.4; 54 -10.3; 60 -9.8; 66 -9.0; 72 -9.5; 79 -10.3; 87 -11.0; 96 -11.6; 106 -11.7; 116 -11.6; 128 -11.4; 141 -11.1; 155 -10.5; 170 -9.7; 187 -8.9; 206 -7.9; 227 -6.8; 249 -6.0; 274 -5.5; 302 -4.9; 332 -4.3; 365 -3.6; 402 -3.0; 442 -2.8; 486 -2.9; 535 -2.7; 588 -2.3; 647 -1.9; 712 -2.0; 783 -2.9; 861 -2.7; 947 -2.1; 1042 -1.8; 1146 -1.4; 1261 -0.9; 1387 -0.5; 1526 -0.5; 1678 -0.7; 1846 -1.3; 2031 -2.0; 2234 -2.2; 2457 -2.2; 2703 -2.8; 2973 -4.0; 3270 -4.7; 3597 -4.2; 3957 -2.9; 4353 -2.4; 4788 -2.8; 5267 -3.6; 5793 -4.6; 6373 -5.4; 7010 -7.5; 7711 -8.2; 8482 -7.3; 9330 -6.6; 10263 -7.3; 11289 -9.7; 12418 -11.8; 13660 -9.9; 15026 -6.5; 16529 -5.3; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.76 | -9.0 dB |
| Peaking | 25 Hz    | 0.78 | -4.5 dB |
| Peaking | 121 Hz   | 0.81 | -7.1 dB |
| Peaking | 1022 Hz  | 0.34 | 3.4 dB  |
| Peaking | 12269 Hz | 1.3  | -6.6 dB |
| Peaking | 844 Hz   | 4.18 | -1.4 dB |
| Peaking | 1501 Hz  | 3.13 | 1.2 dB  |
| Peaking | 3306 Hz  | 2.87 | -3.4 dB |
| Peaking | 4112 Hz  | 1.48 | 2.5 dB  |
| Peaking | 7399 Hz  | 4.48 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Crusher%20Wireless/Skullcandy%20Crusher%20Wireless.png)