# Samsung Level Over Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.5; 25 -2.8; 28 -3.2; 31 -3.5; 34 -3.8; 37 -4.1; 41 -4.4; 45 -4.8; 49 -5.1; 54 -5.5; 60 -5.9; 66 -6.4; 72 -6.8; 79 -7.2; 87 -7.7; 96 -8.1; 106 -8.5; 116 -8.8; 128 -9.0; 141 -9.1; 155 -9.0; 170 -8.8; 187 -8.5; 206 -7.9; 227 -7.6; 249 -8.1; 274 -9.5; 302 -10.2; 332 -9.5; 365 -8.8; 402 -8.0; 442 -7.4; 486 -7.1; 535 -7.1; 588 -7.2; 647 -7.4; 712 -7.0; 783 -6.6; 861 -6.8; 947 -5.3; 1042 -5.2; 1146 -5.3; 1261 -5.2; 1387 -5.9; 1526 -5.7; 1678 -4.7; 1846 -3.5; 2031 -3.8; 2234 -4.6; 2457 -2.0; 2703 -0.5; 2973 -0.5; 3270 -2.0; 3597 -6.2; 3957 -9.4; 4353 -9.1; 4788 -6.7; 5267 -5.4; 5793 -4.9; 6373 -5.7; 7010 -5.9; 7711 -6.2; 8482 -6.5; 9330 -9.1; 10263 -7.2; 11289 -6.5; 12418 -8.0; 13660 -9.9; 15026 -9.9; 16529 -8.3; 18182 -8.2; 20000 -14.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level Over Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level Over Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 17 Hz    |  0.29 | 4.7 dB   |
| Peaking | 137 Hz   |  0.35 | -3.1 dB  |
| Peaking | 3332 Hz  |  1.14 | 9.2 dB   |
| Peaking | 3972 Hz  |  2.92 | -10.9 dB |
| Peaking | 20902 Hz |  0.09 | -3.6 dB  |
| Peaking | 229 Hz   |  4.04 | 1.7 dB   |
| Peaking | 302 Hz   |  3.88 | -2.2 dB  |
| Peaking | 1217 Hz  |  0.33 | 0.3 dB   |
| Peaking | 2219 Hz  | 10.67 | -2.3 dB  |
| Peaking | 12970 Hz |  5.75 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20Over%20Wireless/Samsung%20Level%20Over%20Wireless.png)