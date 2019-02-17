# Plantronics RIG 800LX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -2.1; 25 -3.0; 28 -4.1; 31 -4.8; 34 -5.2; 37 -5.4; 41 -5.5; 45 -5.4; 49 -5.1; 54 -4.7; 60 -4.3; 66 -4.1; 72 -4.0; 79 -4.0; 87 -4.0; 96 -4.0; 106 -4.0; 116 -4.0; 128 -4.0; 141 -3.9; 155 -3.8; 170 -3.5; 187 -3.0; 206 -2.4; 227 -1.9; 249 -1.5; 274 -1.2; 302 -1.3; 332 -1.3; 365 -1.2; 402 -1.3; 442 -1.3; 486 -1.5; 535 -1.4; 588 -1.3; 647 -1.4; 712 -1.8; 783 -2.0; 861 -2.7; 947 -2.9; 1042 -2.6; 1146 -2.2; 1261 -1.9; 1387 -0.7; 1526 -0.5; 1678 -1.0; 1846 -2.8; 2031 -4.3; 2234 -4.4; 2457 -4.1; 2703 -4.8; 2973 -6.7; 3270 -8.5; 3597 -9.2; 3957 -8.4; 4353 -6.9; 4788 -4.4; 5267 -3.1; 5793 -3.3; 6373 -0.9; 7010 -3.7; 7711 -4.5; 8482 -4.8; 9330 -4.9; 10263 -5.1; 11289 -5.5; 12418 -4.8; 13660 -5.3; 15026 -8.4; 16529 -9.2; 18182 -7.6; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics RIG 800LX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics RIG 800LX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 64 Hz    | 0.46 | -2.4 dB |
| Peaking | 1133 Hz  | 0.09 | 1.4 dB  |
| Peaking | 3512 Hz  | 1.98 | -7.8 dB |
| Peaking | 15929 Hz | 3.22 | -2.8 dB |
| Peaking | 20112 Hz | 0.14 | -5.4 dB |
| Peaking | 37 Hz    | 3.94 | -1.1 dB |
| Peaking | 969 Hz   | 3.33 | -1.5 dB |
| Peaking | 1560 Hz  | 3.53 | 2.0 dB  |
| Peaking | 2067 Hz  | 5.42 | -2.1 dB |
| Peaking | 6388 Hz  | 9.37 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -7.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20RIG%20800LX/Plantronics%20RIG%20800LX.png)