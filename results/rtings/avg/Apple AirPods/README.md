# Apple AirPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.9; 45 -3.3; 49 -4.5; 54 -5.8; 60 -7.0; 66 -7.9; 72 -8.5; 79 -8.9; 87 -9.2; 96 -9.4; 106 -9.5; 116 -9.5; 128 -9.4; 141 -9.3; 155 -9.1; 170 -8.9; 187 -8.8; 206 -8.6; 227 -8.4; 249 -8.3; 274 -8.2; 302 -8.1; 332 -8.1; 365 -8.1; 402 -8.1; 442 -8.0; 486 -7.9; 535 -7.7; 588 -7.6; 647 -7.3; 712 -6.8; 783 -6.4; 861 -6.2; 947 -6.3; 1042 -6.7; 1146 -7.3; 1261 -8.3; 1387 -9.6; 1526 -11.2; 1678 -12.4; 1846 -13.3; 2031 -13.6; 2234 -12.8; 2457 -11.8; 2703 -11.5; 2973 -11.1; 3270 -10.6; 3597 -10.5; 3957 -10.8; 4353 -11.4; 4788 -11.5; 5267 -12.0; 5793 -12.2; 6373 -11.1; 7010 -10.5; 7711 -11.0; 8482 -12.3; 9330 -12.9; 10263 -11.0; 11289 -8.8; 12418 -10.7; 13660 -14.3; 15026 -12.6; 16529 -6.9; 18182 -6.5; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple AirPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple AirPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 1.92 | 7.4 dB  |
| Peaking | 1940 Hz  | 1.94 | -5.9 dB |
| Peaking | 6417 Hz  | 0.49 | -5.1 dB |
| Peaking | 14131 Hz | 3.24 | -7.0 dB |
| Peaking | 20026 Hz | 3.43 | -4.0 dB |
| Peaking | 42 Hz    | 1.97 | 4.4 dB  |
| Peaking | 104 Hz   | 0.37 | -3.2 dB |
| Peaking | 934 Hz   | 2.92 | 1.7 dB  |
| Peaking | 7062 Hz  | 5.95 | 1.5 dB  |
| Peaking | 9171 Hz  | 6.54 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.8 dB |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Apple%20AirPods/Apple%20AirPods.png)