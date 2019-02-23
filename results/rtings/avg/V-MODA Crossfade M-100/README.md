# V-MODA Crossfade M-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.5; 25 -8.7; 28 -8.9; 31 -9.0; 34 -9.0; 37 -9.0; 41 -9.0; 45 -9.0; 49 -9.1; 54 -9.1; 60 -9.2; 66 -9.4; 72 -9.6; 79 -9.9; 87 -10.2; 96 -10.4; 106 -10.8; 116 -11.1; 128 -11.4; 141 -11.6; 155 -11.6; 170 -11.4; 187 -10.9; 206 -10.2; 227 -9.2; 249 -8.2; 274 -7.2; 302 -5.7; 332 -3.1; 365 -3.2; 402 -2.9; 442 -3.2; 486 -2.9; 535 -2.8; 588 -3.1; 647 -3.7; 712 -4.6; 783 -5.5; 861 -6.3; 947 -7.0; 1042 -7.7; 1146 -8.0; 1261 -8.3; 1387 -8.6; 1526 -8.5; 1678 -8.7; 1846 -9.3; 2031 -9.5; 2234 -9.0; 2457 -8.2; 2703 -7.6; 2973 -8.7; 3270 -8.4; 3597 -7.2; 3957 -5.2; 4353 -2.7; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -8.0; 10263 -7.7; 11289 -7.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-MODA Crossfade M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-MODA Crossfade M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.19 | -2.0 dB |
| Peaking | 184 Hz   | 0.75 | -6.3 dB |
| Peaking | 422 Hz   | 0.66 | 8.0 dB  |
| Peaking | 2726 Hz  | 0.22 | -4.3 dB |
| Peaking | 5405 Hz  | 1.53 | 10.5 dB |
| Peaking | 2650 Hz  | 6.92 | 2.0 dB  |
| Peaking | 3041 Hz  | 2.9  | -1.3 dB |
| Peaking | 9440 Hz  | 1.48 | -2.8 dB |
| Peaking | 10273 Hz | 0.64 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 5.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/V-MODA%20Crossfade%20M-100/V-MODA%20Crossfade%20M-100.png)