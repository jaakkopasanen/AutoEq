# Noble Audio Django
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.8; 25 -6.9; 28 -7.1; 31 -7.3; 34 -7.4; 37 -7.6; 41 -7.7; 45 -7.9; 49 -8.1; 54 -8.3; 60 -8.6; 66 -8.9; 72 -9.3; 79 -9.7; 87 -10.0; 96 -10.6; 106 -10.9; 116 -11.3; 128 -11.6; 141 -11.9; 155 -12.1; 170 -12.3; 187 -12.4; 206 -12.4; 227 -12.4; 249 -12.3; 274 -12.2; 302 -12.0; 332 -11.8; 365 -11.5; 402 -11.2; 442 -10.9; 486 -10.5; 535 -10.0; 588 -9.5; 647 -8.9; 712 -8.2; 783 -7.4; 861 -6.7; 947 -6.2; 1042 -6.0; 1146 -6.1; 1261 -6.1; 1387 -5.7; 1526 -4.5; 1678 -2.9; 1846 -1.1; 2031 -0.5; 2234 -0.5; 2457 -0.7; 2703 -1.6; 2973 -1.5; 3270 -1.0; 3597 -1.1; 3957 -1.7; 4353 -0.7; 4788 -0.5; 5267 -1.6; 5793 -4.5; 6373 -3.7; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.0; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio Django GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio Django ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 0.66 | -1.6 dB |
| Peaking | 220 Hz  | 0.57 | -5.1 dB |
| Peaking | 460 Hz  | 1.46 | -1.6 dB |
| Peaking | 2185 Hz | 1.5  | 5.8 dB  |
| Peaking | 4442 Hz | 1.61 | 5.2 dB  |
| Peaking | 979 Hz  | 3.35 | 1.0 dB  |
| Peaking | 1332 Hz | 2.11 | -1.0 dB |
| Peaking | 1796 Hz | 5.81 | 1.0 dB  |
| Peaking | 6771 Hz | 8.7  | 2.1 dB  |
| Peaking | 8006 Hz | 1.84 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Noble%20Audio%20Django/Noble%20Audio%20Django.png)