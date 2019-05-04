# AKG K712 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.8; 34 -1.1; 37 -1.4; 41 -1.7; 45 -2.0; 49 -2.2; 54 -2.5; 60 -2.9; 66 -3.2; 72 -3.5; 79 -3.9; 87 -4.3; 96 -4.8; 106 -5.2; 116 -5.6; 128 -6.1; 141 -6.4; 155 -6.7; 170 -6.9; 187 -7.0; 206 -7.1; 227 -7.1; 249 -7.2; 274 -7.3; 302 -7.3; 332 -7.4; 365 -7.4; 402 -7.4; 442 -7.5; 486 -7.4; 535 -6.9; 588 -6.8; 647 -6.8; 712 -6.3; 783 -5.6; 861 -4.4; 947 -3.5; 1042 -3.0; 1146 -3.2; 1261 -3.7; 1387 -4.3; 1526 -5.3; 1678 -6.9; 1846 -9.0; 2031 -10.5; 2234 -10.6; 2457 -8.5; 2703 -5.6; 2973 -3.3; 3270 -4.1; 3597 -6.0; 3957 -7.1; 4353 -7.0; 4788 -6.1; 5267 -5.6; 5793 -6.2; 6373 -6.7; 7010 -8.4; 7711 -10.3; 8482 -9.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.4; 18182 -14.5; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.9  | 6.1 dB  |
| Peaking | 59 Hz    | 1.54 | 2.3 dB  |
| Peaking | 1119 Hz  | 2.3  | 3.9 dB  |
| Peaking | 2084 Hz  | 4.91 | -5.4 dB |
| Peaking | 18861 Hz | 1.34 | -9.3 dB |
| Peaking | 340 Hz   | 0.88 | -1.2 dB |
| Peaking | 3049 Hz  | 6.79 | 4.0 dB  |
| Peaking | 5380 Hz  | 6.27 | 1.2 dB  |
| Peaking | 7880 Hz  | 4.67 | -4.4 dB |
| Peaking | 14765 Hz | 1.78 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K712%20PRO/AKG%20K712%20PRO.png)