# Sound Intone CX-05
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.6; 25 -3.9; 28 -4.2; 31 -4.6; 34 -4.9; 37 -5.2; 41 -5.4; 45 -5.6; 49 -5.8; 54 -6.0; 60 -6.2; 66 -6.3; 72 -6.3; 79 -6.3; 87 -6.3; 96 -6.4; 106 -6.4; 116 -6.5; 128 -6.4; 141 -6.5; 155 -6.4; 170 -6.2; 187 -6.5; 206 -6.7; 227 -6.8; 249 -6.7; 274 -7.7; 302 -8.5; 332 -8.9; 365 -9.8; 402 -9.8; 442 -9.7; 486 -9.4; 535 -8.9; 588 -8.5; 647 -8.1; 712 -7.7; 783 -7.2; 861 -6.7; 947 -6.6; 1042 -6.4; 1146 -6.2; 1261 -5.7; 1387 -4.7; 1526 -4.3; 1678 -3.7; 1846 -3.1; 2031 -2.4; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sound Intone CX-05 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sound Intone CX-05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.73 | 3.5 dB  |
| Peaking | 440 Hz  | 1.3  | -3.6 dB |
| Peaking | 2840 Hz | 1.03 | 6.2 dB  |
| Peaking | 5428 Hz | 2.26 | 4.7 dB  |
| Peaking | 200 Hz  | 2.22 | 0.5 dB  |
| Peaking | 1168 Hz | 1.77 | -1.0 dB |
| Peaking | 1388 Hz | 1.43 | 0.7 dB  |
| Peaking | 6455 Hz | 6.01 | 2.6 dB  |
| Peaking | 7799 Hz | 1.96 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sound%20Intone%20CX-05/Sound%20Intone%20CX-05.png)