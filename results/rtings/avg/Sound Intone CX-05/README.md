# Sound Intone CX-05
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.3; 25 -6.5; 28 -6.9; 31 -7.3; 34 -7.6; 37 -7.8; 41 -8.0; 45 -8.2; 49 -8.4; 54 -8.7; 60 -8.9; 66 -9.0; 72 -9.0; 79 -9.0; 87 -9.0; 96 -9.0; 106 -9.1; 116 -9.1; 128 -9.1; 141 -9.1; 155 -9.1; 170 -8.9; 187 -9.2; 206 -9.4; 227 -9.4; 249 -9.4; 274 -10.3; 302 -11.2; 332 -11.6; 365 -12.4; 402 -12.5; 442 -12.4; 486 -12.0; 535 -11.5; 588 -11.1; 647 -10.7; 712 -10.4; 783 -9.8; 861 -9.4; 947 -9.3; 1042 -9.1; 1146 -8.8; 1261 -8.3; 1387 -7.4; 1526 -7.0; 1678 -6.4; 1846 -5.8; 2031 -5.1; 2234 -3.5; 2457 -2.4; 2703 -2.0; 2973 -2.5; 3270 -1.7; 3597 -1.8; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -2.4; 5793 -1.2; 6373 -1.1; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sound Intone CX-05 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sound Intone CX-05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.36 | 1.1 dB  |
| Peaking | 69 Hz   | 0.66 | -2.3 dB |
| Peaking | 470 Hz  | 0.59 | -5.6 dB |
| Peaking | 3963 Hz | 0.9  | 6.3 dB  |
| Peaking | 1204 Hz | 4.45 | -0.9 dB |
| Peaking | 2460 Hz | 5.25 | 1.6 dB  |
| Peaking | 3532 Hz | 4.03 | -0.8 dB |
| Peaking | 6277 Hz | 5.67 | 3.5 dB  |
| Peaking | 8120 Hz | 1.65 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -5.3 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sound%20Intone%20CX-05/Sound%20Intone%20CX-05.png)