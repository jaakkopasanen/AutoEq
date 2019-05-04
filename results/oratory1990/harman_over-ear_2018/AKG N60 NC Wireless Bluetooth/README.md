# AKG N60 NC Wireless Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.9; 37 -1.6; 41 -2.5; 45 -3.4; 49 -4.1; 54 -5.0; 60 -5.9; 66 -6.8; 72 -7.4; 79 -8.0; 87 -8.5; 96 -9.0; 106 -9.3; 116 -9.6; 128 -9.8; 141 -9.8; 155 -9.8; 170 -9.6; 187 -9.4; 206 -9.1; 227 -9.0; 249 -8.6; 274 -8.0; 302 -7.4; 332 -6.8; 365 -6.4; 402 -6.3; 442 -5.7; 486 -5.1; 535 -4.9; 588 -4.9; 647 -5.0; 712 -5.2; 783 -5.3; 861 -5.6; 947 -6.2; 1042 -6.5; 1146 -6.5; 1261 -6.4; 1387 -6.0; 1526 -5.4; 1678 -5.1; 1846 -5.0; 2031 -5.0; 2234 -5.6; 2457 -6.5; 2703 -7.8; 2973 -9.7; 3270 -11.5; 3597 -12.9; 3957 -12.5; 4353 -10.2; 4788 -9.8; 5267 -13.5; 5793 -12.8; 6373 -7.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.9; 16529 -9.3; 18182 -11.7; 20000 -13.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N60 NC Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N60 NC Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.76 | 6.9 dB  |
| Peaking | 136 Hz  |  0.61 | -4.8 dB |
| Peaking | 1103 Hz |  0.13 | 1.6 dB  |
| Peaking | 3622 Hz |  2.47 | -7.9 dB |
| Peaking | 5498 Hz |  5.78 | -8.0 dB |
| Peaking | 247 Hz  |  4.08 | -0.7 dB |
| Peaking | 555 Hz  |  1.86 | 1.0 dB  |
| Peaking | 1123 Hz |  2.1  | -1.6 dB |
| Peaking | 1931 Hz |  3.49 | 1.1 dB  |
| Peaking | 6850 Hz | 11.72 | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.3 dB |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20N60%20NC%20Wireless%20Bluetooth/AKG%20N60%20NC%20Wireless%20Bluetooth.png)