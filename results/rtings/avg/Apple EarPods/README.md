# Apple EarPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.9; 60 -2.3; 66 -3.6; 72 -4.7; 79 -5.7; 87 -6.5; 96 -7.1; 106 -7.5; 116 -7.7; 128 -7.7; 141 -7.5; 155 -7.4; 170 -7.2; 187 -7.0; 206 -6.7; 227 -6.5; 249 -6.3; 274 -6.2; 302 -6.0; 332 -6.0; 365 -5.9; 402 -5.9; 442 -5.7; 486 -5.6; 535 -5.5; 588 -5.3; 647 -4.9; 712 -4.2; 783 -3.5; 861 -3.2; 947 -3.3; 1042 -3.8; 1146 -4.5; 1261 -5.4; 1387 -6.6; 1526 -7.7; 1678 -8.5; 1846 -8.9; 2031 -8.9; 2234 -8.2; 2457 -7.3; 2703 -6.5; 2973 -5.8; 3270 -5.0; 3597 -4.8; 3957 -5.0; 4353 -6.1; 4788 -7.1; 5267 -9.0; 5793 -11.4; 6373 -11.4; 7010 -9.2; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.5; 15026 -7.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 1.03 | 7.2 dB  |
| Peaking | 921 Hz   | 1.46 | 3.8 dB  |
| Peaking | 1870 Hz  | 1.65 | -3.5 dB |
| Peaking | 3581 Hz  | 1.76 | 2.6 dB  |
| Peaking | 6039 Hz  | 3.22 | -6.0 dB |
| Peaking | 34 Hz    | 3.39 | -1.7 dB |
| Peaking | 53 Hz    | 2.02 | 2.7 dB  |
| Peaking | 108 Hz   | 1.33 | -2.2 dB |
| Peaking | 13100 Hz | 0.97 | 0.7 dB  |
| Peaking | 14190 Hz | 3.72 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Apple%20EarPods/Apple%20EarPods.png)