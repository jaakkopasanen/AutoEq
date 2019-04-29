# Jomo Trinity
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.3; 25 -5.5; 28 -5.7; 31 -5.8; 34 -5.9; 37 -6.0; 41 -6.0; 45 -6.1; 49 -6.1; 54 -6.2; 60 -6.3; 66 -6.3; 72 -6.4; 79 -6.5; 87 -6.6; 96 -6.7; 106 -6.8; 116 -6.7; 128 -6.6; 141 -6.5; 155 -6.3; 170 -6.0; 187 -5.7; 206 -5.3; 227 -4.9; 249 -4.5; 274 -4.0; 302 -3.5; 332 -3.1; 365 -2.6; 402 -2.3; 442 -1.9; 486 -1.6; 535 -1.2; 588 -1.0; 647 -0.8; 712 -0.6; 783 -0.5; 861 -0.6; 947 -1.0; 1042 -1.9; 1146 -3.2; 1261 -4.7; 1387 -5.9; 1526 -6.7; 1678 -6.8; 1846 -6.5; 2031 -6.6; 2234 -6.7; 2457 -6.1; 2703 -5.4; 2973 -5.2; 3270 -5.3; 3597 -6.1; 3957 -7.2; 4353 -7.5; 4788 -5.8; 5267 -3.4; 5793 -2.1; 6373 -1.7; 7010 -3.7; 7711 -5.1; 8482 -4.1; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Trinity GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Trinity ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 98 Hz   | 0.37 | -2.8 dB |
| Peaking | 935 Hz  | 0.55 | 7.0 dB  |
| Peaking | 1563 Hz | 0.91 | -7.5 dB |
| Peaking | 4243 Hz | 3.59 | -3.6 dB |
| Peaking | 5963 Hz | 4.21 | 3.3 dB  |
| Peaking | 979 Hz  | 6.93 | 0.4 dB  |
| Peaking | 7602 Hz | 9.69 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Trinity/Jomo%20Trinity.png)