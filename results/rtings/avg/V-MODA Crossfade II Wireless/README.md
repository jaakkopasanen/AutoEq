# V-MODA Crossfade II Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.9; 25 -8.2; 28 -8.5; 31 -8.8; 34 -9.1; 37 -9.2; 41 -9.4; 45 -9.6; 49 -9.8; 54 -10.0; 60 -10.3; 66 -10.6; 72 -10.8; 79 -11.1; 87 -11.4; 96 -11.7; 106 -11.9; 116 -12.1; 128 -12.2; 141 -12.1; 155 -12.0; 170 -11.8; 187 -11.4; 206 -10.8; 227 -10.1; 249 -9.3; 274 -7.6; 302 -6.6; 332 -6.4; 365 -5.5; 402 -5.1; 442 -5.3; 486 -5.5; 535 -5.6; 588 -5.8; 647 -6.1; 712 -6.4; 783 -6.8; 861 -7.0; 947 -7.3; 1042 -7.5; 1146 -7.5; 1261 -7.2; 1387 -6.8; 1526 -6.4; 1678 -6.1; 1846 -6.0; 2031 -6.1; 2234 -6.5; 2457 -7.0; 2703 -6.7; 2973 -7.0; 3270 -7.5; 3597 -8.7; 3957 -7.6; 4353 -4.2; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.3; 11289 -8.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 79 Hz   | 0.26 | -1.8 dB |
| Peaking | 236 Hz  | 0.37 | -6.9 dB |
| Peaking | 374 Hz  | 0.8  | 8.1 dB  |
| Peaking | 3701 Hz | 4.02 | -4.0 dB |
| Peaking | 5375 Hz | 2.26 | 7.3 dB  |
| Peaking | 647 Hz  | 3.62 | 0.5 dB  |
| Peaking | 1092 Hz | 2.29 | -0.7 dB |
| Peaking | 1718 Hz | 3.19 | 0.9 dB  |
| Peaking | 6469 Hz | 8.42 | 2.3 dB  |
| Peaking | 9739 Hz | 1.16 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/V-MODA%20Crossfade%20II%20Wireless/V-MODA%20Crossfade%20II%20Wireless.png)