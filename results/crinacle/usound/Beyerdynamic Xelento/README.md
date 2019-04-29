# Beyerdynamic Xelento
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.1; 25 -11.1; 28 -11.2; 31 -11.2; 34 -11.2; 37 -11.2; 41 -11.2; 45 -11.1; 49 -11.1; 54 -11.2; 60 -11.2; 66 -11.3; 72 -11.4; 79 -11.5; 87 -11.5; 96 -11.7; 106 -11.8; 116 -11.7; 128 -11.6; 141 -11.5; 155 -11.3; 170 -11.0; 187 -10.7; 206 -10.3; 227 -9.9; 249 -9.4; 274 -8.9; 302 -8.3; 332 -7.8; 365 -7.2; 402 -6.7; 442 -6.2; 486 -5.6; 535 -5.1; 588 -4.5; 647 -4.0; 712 -3.4; 783 -2.8; 861 -2.4; 947 -2.3; 1042 -2.6; 1146 -3.2; 1261 -3.9; 1387 -4.2; 1526 -4.2; 1678 -3.9; 1846 -3.6; 2031 -3.3; 2234 -3.2; 2457 -3.0; 2703 -2.6; 2973 -2.0; 3270 -1.6; 3597 -1.5; 3957 -2.1; 4353 -4.0; 4788 -7.4; 5267 -7.0; 5793 -0.8; 6373 -0.5; 7010 -3.9; 7711 -7.6; 8482 -6.8; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Xelento GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Xelento ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 69 Hz   | 0.18 | -6.2 dB  |
| Peaking | 778 Hz  | 0.82 | 3.9 dB   |
| Peaking | 3920 Hz | 1.2  | 9.6 dB   |
| Peaking | 5150 Hz | 1.4  | -12.4 dB |
| Peaking | 6037 Hz | 3.91 | 12.0 dB  |
| Peaking | 44 Hz   | 0.42 | -1.4 dB  |
| Peaking | 51 Hz   | 0.87 | 2.0 dB   |
| Peaking | 2106 Hz | 5.05 | 0.3 dB   |
| Peaking | 7993 Hz | 6.09 | -3.7 dB  |
| Peaking | 8326 Hz | 1.94 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Beyerdynamic%20Xelento/Beyerdynamic%20Xelento.png)