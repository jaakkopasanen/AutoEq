# AKG K712 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.0; 34 -1.4; 37 -1.6; 41 -1.9; 45 -2.2; 49 -2.4; 54 -2.7; 60 -3.0; 66 -3.4; 72 -3.8; 79 -4.2; 87 -4.6; 96 -5.0; 106 -5.5; 116 -5.9; 128 -6.3; 141 -6.7; 155 -7.0; 170 -7.1; 187 -7.2; 206 -7.3; 227 -7.3; 249 -7.3; 274 -7.4; 302 -7.4; 332 -7.4; 365 -7.4; 402 -7.4; 442 -7.5; 486 -7.4; 535 -6.9; 588 -6.7; 647 -6.7; 712 -6.2; 783 -5.4; 861 -4.3; 947 -3.4; 1042 -2.8; 1146 -3.1; 1261 -3.5; 1387 -4.1; 1526 -5.1; 1678 -6.6; 1846 -8.6; 2031 -10.0; 2234 -9.8; 2457 -7.5; 2703 -5.1; 2973 -3.2; 3270 -4.3; 3597 -6.3; 3957 -7.4; 4353 -7.4; 4788 -5.8; 5267 -5.1; 5793 -6.2; 6373 -7.6; 7010 -8.3; 7711 -9.4; 8482 -10.2; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.4; 18182 -14.6; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.98 | 6.1 dB  |
| Peaking | 58 Hz    | 1.62 | 2.5 dB  |
| Peaking | 1123 Hz  | 2.19 | 4.1 dB  |
| Peaking | 2057 Hz  | 5.3  | -4.7 dB |
| Peaking | 18896 Hz | 1.32 | -9.5 dB |
| Peaking | 303 Hz   | 0.87 | -1.2 dB |
| Peaking | 3024 Hz  | 4.91 | 4.8 dB  |
| Peaking | 5478 Hz  | 2.56 | 4.7 dB  |
| Peaking | 7716 Hz  | 0.72 | -6.6 dB |
| Peaking | 10680 Hz | 0.79 | 4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K712%20PRO/AKG%20K712%20PRO.png)