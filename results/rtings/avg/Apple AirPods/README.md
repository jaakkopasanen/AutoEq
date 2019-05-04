# Apple AirPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.2; 54 -2.5; 60 -3.7; 66 -4.6; 72 -5.2; 79 -5.6; 87 -5.9; 96 -6.1; 106 -6.2; 116 -6.1; 128 -6.1; 141 -5.9; 155 -5.8; 170 -5.6; 187 -5.5; 206 -5.3; 227 -5.2; 249 -5.1; 274 -5.0; 302 -5.0; 332 -4.9; 365 -4.9; 402 -4.9; 442 -4.9; 486 -4.8; 535 -4.7; 588 -4.5; 647 -4.2; 712 -3.8; 783 -3.4; 861 -3.1; 947 -3.2; 1042 -3.7; 1146 -4.3; 1261 -5.4; 1387 -6.7; 1526 -8.2; 1678 -9.6; 1846 -10.6; 2031 -11.0; 2234 -10.6; 2457 -9.7; 2703 -8.9; 2973 -8.1; 3270 -7.2; 3597 -7.1; 3957 -7.4; 4353 -7.9; 4788 -8.8; 5267 -9.4; 5793 -8.9; 6373 -7.0; 7010 -7.5; 7711 -8.7; 8482 -8.8; 9330 -8.0; 10263 -7.2; 11289 -6.5; 12418 -7.8; 13660 -10.5; 15026 -9.1; 16529 -6.5; 18182 -6.5; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple AirPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple AirPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.88 | 6.9 dB  |
| Peaking | 1461 Hz  | 0.44 | 6.1 dB  |
| Peaking | 1933 Hz  | 1.23 | -9.9 dB |
| Peaking | 5608 Hz  | 0.88 | -2.8 dB |
| Peaking | 14049 Hz | 3.7  | -4.5 dB |
| Peaking | 48 Hz    | 4.22 | 1.8 dB  |
| Peaking | 87 Hz    | 2.26 | -0.9 dB |
| Peaking | 5483 Hz  | 3.08 | -3.1 dB |
| Peaking | 6651 Hz  | 1.48 | 3.8 dB  |
| Peaking | 7970 Hz  | 2.8  | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Apple%20AirPods/Apple%20AirPods.png)