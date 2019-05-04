# Apple EarPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -2.2; 66 -3.4; 72 -4.5; 79 -5.5; 87 -6.3; 96 -6.9; 106 -7.3; 116 -7.5; 128 -7.5; 141 -7.4; 155 -7.2; 170 -7.0; 187 -6.8; 206 -6.6; 227 -6.4; 249 -6.3; 274 -6.1; 302 -6.0; 332 -6.0; 365 -5.9; 402 -5.9; 442 -5.8; 486 -5.7; 535 -5.6; 588 -5.4; 647 -5.0; 712 -4.3; 783 -3.7; 861 -3.3; 947 -3.4; 1042 -4.0; 1146 -4.7; 1261 -5.7; 1387 -6.8; 1526 -8.0; 1678 -8.8; 1846 -9.3; 2031 -9.4; 2234 -9.0; 2457 -8.0; 2703 -6.9; 2973 -5.6; 3270 -4.7; 3597 -4.5; 3957 -4.7; 4353 -5.7; 4788 -7.5; 5267 -9.5; 5793 -11.4; 6373 -10.5; 7010 -9.3; 7711 -8.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -7.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.99 | 7.2 dB  |
| Peaking | 934 Hz   | 1.42 | 4.0 dB  |
| Peaking | 2012 Hz  | 1.21 | -4.7 dB |
| Peaking | 3594 Hz  | 1.17 | 4.2 dB  |
| Peaking | 5854 Hz  | 2.31 | -6.2 dB |
| Peaking | 37 Hz    | 3.28 | -1.8 dB |
| Peaking | 53 Hz    | 2.15 | 2.5 dB  |
| Peaking | 109 Hz   | 1.46 | -2.1 dB |
| Peaking | 8986 Hz  | 5.52 | 0.7 dB  |
| Peaking | 14266 Hz | 6.54 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Apple%20EarPods/Apple%20EarPods.png)