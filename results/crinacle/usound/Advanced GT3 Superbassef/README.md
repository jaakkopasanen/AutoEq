# Advanced GT3 Superbassef
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.1; 25 -10.2; 28 -10.2; 31 -10.2; 34 -10.1; 37 -10.0; 41 -9.9; 45 -9.8; 49 -9.7; 54 -9.6; 60 -9.5; 66 -9.5; 72 -9.5; 79 -9.6; 87 -9.7; 96 -9.9; 106 -10.0; 116 -10.2; 128 -10.3; 141 -10.4; 155 -10.6; 170 -10.6; 187 -10.7; 206 -10.7; 227 -10.7; 249 -10.7; 274 -10.6; 302 -10.5; 332 -10.5; 365 -10.4; 402 -10.3; 442 -10.1; 486 -9.8; 535 -9.9; 588 -9.6; 647 -9.1; 712 -8.6; 783 -8.1; 861 -7.7; 947 -7.4; 1042 -7.3; 1146 -7.5; 1261 -7.6; 1387 -7.4; 1526 -6.7; 1678 -5.6; 1846 -4.4; 2031 -3.3; 2234 -2.5; 2457 -2.0; 2703 -1.9; 2973 -2.3; 3270 -3.2; 3597 -4.5; 3957 -6.0; 4353 -6.5; 4788 -4.1; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.8; 16529 -12.5; 18182 -15.0; 20000 -15.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3 Superbassef GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3 Superbassef ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.59 | -3.4 dB  |
| Peaking | 243 Hz   | 0.33 | -4.2 dB  |
| Peaking | 2504 Hz  | 1.93 | 5.3 dB   |
| Peaking | 5881 Hz  | 3.26 | 6.7 dB   |
| Peaking | 19072 Hz | 0.76 | -10.3 dB |
| Peaking | 927 Hz   | 3.83 | 0.7 dB   |
| Peaking | 1342 Hz  | 4.68 | -0.9 dB  |
| Peaking | 4228 Hz  | 4.59 | -4.2 dB  |
| Peaking | 4259 Hz  | 2    | 2.0 dB   |
| Peaking | 13054 Hz | 3.76 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -6.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20GT3%20Superbassef/Advanced%20GT3%20Superbassef.png)