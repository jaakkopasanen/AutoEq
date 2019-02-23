# Apple AirPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.4; 54 -2.6; 60 -3.9; 66 -4.8; 72 -5.3; 79 -5.8; 87 -6.1; 96 -6.3; 106 -6.4; 116 -6.4; 128 -6.3; 141 -6.1; 155 -6.0; 170 -5.8; 187 -5.6; 206 -5.5; 227 -5.3; 249 -5.2; 274 -5.1; 302 -5.0; 332 -5.0; 365 -5.0; 402 -5.0; 442 -4.9; 486 -4.8; 535 -4.6; 588 -4.5; 647 -4.1; 712 -3.7; 783 -3.3; 861 -3.0; 947 -3.1; 1042 -3.5; 1146 -4.2; 1261 -5.2; 1387 -6.5; 1526 -8.1; 1678 -9.3; 1846 -10.2; 2031 -10.5; 2234 -9.7; 2457 -8.7; 2703 -8.3; 2973 -8.0; 3270 -7.5; 3597 -7.4; 3957 -7.7; 4353 -8.3; 4788 -8.3; 5267 -8.9; 5793 -9.1; 6373 -8.0; 7010 -7.4; 7711 -7.9; 8482 -9.2; 9330 -9.8; 10263 -7.9; 11289 -6.5; 12418 -7.6; 13660 -11.2; 15026 -9.4; 16529 -6.5; 18182 -6.5; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple AirPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple AirPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.93 | 6.9 dB  |
| Peaking | 1221 Hz  | 0.53 | 5.2 dB  |
| Peaking | 1810 Hz  | 1.44 | -7.3 dB |
| Peaking | 8499 Hz  | 0.28 | -2.2 dB |
| Peaking | 22050 Hz | 1.7  | -2.4 dB |
| Peaking | 96 Hz    | 2.55 | -1.0 dB |
| Peaking | 10909 Hz | 6.5  | 2.4 dB  |
| Peaking | 12162 Hz | 3.82 | 4.1 dB  |
| Peaking | 13972 Hz | 1.37 | -6.1 dB |
| Peaking | 15993 Hz | 1.36 | 4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Apple%20AirPods/Apple%20AirPods.png)