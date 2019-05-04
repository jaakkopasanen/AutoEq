# Samsung Gear IconX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.0; 31 -1.3; 34 -1.5; 37 -1.8; 41 -2.1; 45 -2.3; 49 -2.5; 54 -2.8; 60 -3.3; 66 -3.7; 72 -4.1; 79 -4.4; 87 -4.9; 96 -5.4; 106 -6.0; 116 -6.5; 128 -7.0; 141 -7.3; 155 -7.6; 170 -7.7; 187 -7.9; 206 -8.0; 227 -7.8; 249 -7.4; 274 -7.0; 302 -6.6; 332 -6.2; 365 -5.9; 402 -5.5; 442 -5.0; 486 -4.6; 535 -4.1; 588 -3.6; 647 -3.1; 712 -2.6; 783 -2.3; 861 -2.7; 947 -3.6; 1042 -4.4; 1146 -5.1; 1261 -5.8; 1387 -6.1; 1526 -6.3; 1678 -6.4; 1846 -6.5; 2031 -6.6; 2234 -6.2; 2457 -5.4; 2703 -4.9; 2973 -4.9; 3270 -5.0; 3597 -5.2; 3957 -4.9; 4353 -4.7; 4788 -4.4; 5267 -3.5; 5793 -2.5; 6373 -2.5; 7010 -4.0; 7711 -5.4; 8482 -6.5; 9330 -7.1; 10263 -6.7; 11289 -5.5; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -8.9; 18182 -11.9; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Gear IconX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Gear IconX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.3  | 5.0 dB  |
| Peaking | 175 Hz   | 0.9  | -3.1 dB |
| Peaking | 727 Hz   | 2.08 | 3.5 dB  |
| Peaking | 5965 Hz  | 3.71 | 3.5 dB  |
| Peaking | 18209 Hz | 1.55 | -7.2 dB |
| Peaking | 907 Hz   | 4.59 | 0.9 dB  |
| Peaking | 1946 Hz  | 1.26 | -2.6 dB |
| Peaking | 2534 Hz  | 1.11 | 1.7 dB  |
| Peaking | 9352 Hz  | 3.75 | -2.0 dB |
| Peaking | 14556 Hz | 2.47 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Gear%20IconX/Samsung%20Gear%20IconX.png)