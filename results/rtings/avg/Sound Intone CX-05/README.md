# Sound Intone CX-05
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.1; 25 -6.3; 28 -6.7; 31 -7.1; 34 -7.4; 37 -7.7; 41 -7.9; 45 -8.1; 49 -8.3; 54 -8.5; 60 -8.7; 66 -8.8; 72 -8.8; 79 -8.8; 87 -8.8; 96 -8.8; 106 -8.9; 116 -8.9; 128 -8.9; 141 -8.9; 155 -8.9; 170 -8.8; 187 -9.0; 206 -9.3; 227 -9.3; 249 -9.3; 274 -10.3; 302 -11.2; 332 -11.6; 365 -12.4; 402 -12.5; 442 -12.4; 486 -12.1; 535 -11.6; 588 -11.2; 647 -10.9; 712 -10.5; 783 -10.0; 861 -9.5; 947 -9.4; 1042 -9.2; 1146 -9.0; 1261 -8.5; 1387 -7.6; 1526 -7.3; 1678 -6.6; 1846 -6.1; 2031 -5.5; 2234 -4.4; 2457 -3.3; 2703 -2.7; 2973 -2.6; 3270 -1.4; 3597 -1.5; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -2.3; 5793 -1.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sound Intone CX-05 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sound Intone CX-05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.4  | 1.3 dB  |
| Peaking | 66 Hz   | 0.68 | -2.1 dB |
| Peaking | 471 Hz  | 0.61 | -5.6 dB |
| Peaking | 3840 Hz | 1.16 | 6.3 dB  |
| Peaking | 6194 Hz | 6.05 | 3.7 dB  |
| Peaking | 1189 Hz | 5.04 | -0.8 dB |
| Peaking | 2487 Hz | 5.46 | 1.1 dB  |
| Peaking | 3661 Hz | 7.04 | -1.0 dB |
| Peaking | 4828 Hz | 7.65 | 1.5 dB  |
| Peaking | 8495 Hz | 2.52 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -5.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sound%20Intone%20CX-05/Sound%20Intone%20CX-05.png)