# V-MODA Crossfade II Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.1; 25 -8.3; 28 -8.7; 31 -9.1; 34 -9.3; 37 -9.4; 41 -9.6; 45 -9.8; 49 -10.0; 54 -10.2; 60 -10.4; 66 -10.7; 72 -11.0; 79 -11.3; 87 -11.6; 96 -11.9; 106 -12.2; 116 -12.4; 128 -12.4; 141 -12.3; 155 -12.2; 170 -12.0; 187 -11.5; 206 -10.9; 227 -10.2; 249 -9.4; 274 -7.7; 302 -6.8; 332 -6.4; 365 -5.6; 402 -5.1; 442 -5.4; 486 -5.4; 535 -5.5; 588 -5.7; 647 -5.9; 712 -6.3; 783 -6.6; 861 -6.9; 947 -7.2; 1042 -7.4; 1146 -7.3; 1261 -7.0; 1387 -6.7; 1526 -6.1; 1678 -5.9; 1846 -5.7; 2031 -5.7; 2234 -5.6; 2457 -6.1; 2703 -6.1; 2973 -7.0; 3270 -7.7; 3597 -9.0; 3957 -8.0; 4353 -4.6; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -7.8; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-MODA Crossfade II Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-MODA Crossfade II Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 122 Hz  | 0.19 | -2.8 dB |
| Peaking | 169 Hz  | 0.54 | -4.5 dB |
| Peaking | 372 Hz  | 0.89 | 5.7 dB  |
| Peaking | 3726 Hz | 4.28 | -4.5 dB |
| Peaking | 5367 Hz | 2.24 | 7.3 dB  |
| Peaking | 1084 Hz | 3.07 | -0.9 dB |
| Peaking | 1935 Hz | 2.2  | 1.0 dB  |
| Peaking | 6463 Hz | 7.77 | 2.4 dB  |
| Peaking | 9199 Hz | 1.27 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/V-MODA%20Crossfade%20II%20Wireless/V-MODA%20Crossfade%20II%20Wireless.png)