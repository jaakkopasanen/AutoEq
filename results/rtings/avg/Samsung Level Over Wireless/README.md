# Samsung Level Over Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.9; 25 -4.1; 28 -4.5; 31 -4.8; 34 -5.1; 37 -5.4; 41 -5.8; 45 -6.1; 49 -6.5; 54 -6.8; 60 -7.3; 66 -7.8; 72 -8.2; 79 -8.6; 87 -9.0; 96 -9.5; 106 -9.9; 116 -10.2; 128 -10.4; 141 -10.4; 155 -10.4; 170 -10.2; 187 -9.8; 206 -9.3; 227 -8.9; 249 -9.4; 274 -10.8; 302 -11.6; 332 -10.8; 365 -10.2; 402 -9.3; 442 -8.7; 486 -8.5; 535 -8.4; 588 -8.6; 647 -8.7; 712 -8.3; 783 -7.9; 861 -8.1; 947 -6.6; 1042 -6.6; 1146 -6.6; 1261 -6.6; 1387 -7.3; 1526 -7.1; 1678 -6.1; 1846 -4.9; 2031 -5.1; 2234 -6.0; 2457 -3.3; 2703 -0.5; 2973 -1.0; 3270 -3.4; 3597 -7.6; 3957 -10.8; 4353 -10.4; 4788 -8.1; 5267 -6.7; 5793 -6.2; 6373 -7.0; 7010 -7.2; 7711 -6.0; 8482 -7.2; 9330 -10.5; 10263 -8.6; 11289 -7.1; 12418 -9.4; 13660 -11.2; 15026 -11.3; 16529 -9.6; 18182 -9.5; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level Over Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level Over Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 119 Hz   | 1.27 | -3.3 dB |
| Peaking | 330 Hz   | 0.74 | -3.7 dB |
| Peaking | 2851 Hz  | 3.3  | 6.9 dB  |
| Peaking | 4067 Hz  | 4.41 | -5.9 dB |
| Peaking | 19468 Hz | 0.23 | -5.3 dB |
| Peaking | 22 Hz    | 1.46 | 2.7 dB  |
| Peaking | 449 Hz   | 6.59 | 0.9 dB  |
| Peaking | 14493 Hz | 2.34 | -2.9 dB |
| Peaking | 17964 Hz | 0.81 | 3.1 dB  |
| Peaking | 20081 Hz | 1.35 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20Over%20Wireless/Samsung%20Level%20Over%20Wireless.png)