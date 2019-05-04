# Marshall MID ANC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -4.8; 25 -4.6; 28 -4.5; 31 -4.5; 34 -4.5; 37 -4.5; 41 -4.6; 45 -4.7; 49 -4.8; 54 -4.9; 60 -5.0; 66 -5.0; 72 -5.1; 79 -5.2; 87 -5.2; 96 -5.2; 106 -5.1; 116 -5.0; 128 -4.8; 141 -4.6; 155 -4.3; 170 -4.0; 187 -3.7; 206 -3.4; 227 -3.0; 249 -2.7; 274 -2.6; 302 -2.3; 332 -1.9; 365 -1.8; 402 -1.6; 442 -1.6; 486 -1.7; 535 -1.7; 588 -1.8; 647 -1.8; 712 -1.7; 783 -1.8; 861 -1.7; 947 -1.6; 1042 -1.5; 1146 -1.6; 1261 -2.2; 1387 -2.6; 1526 -2.6; 1678 -3.5; 1846 -3.9; 2031 -4.3; 2234 -4.3; 2457 -4.3; 2703 -4.9; 2973 -6.2; 3270 -7.8; 3597 -8.1; 3957 -9.5; 4353 -9.0; 4788 -5.2; 5267 -1.9; 5793 -0.5; 6373 -4.2; 7010 -9.6; 7711 -11.1; 8482 -5.2; 9330 -3.6; 10263 -3.6; 11289 -8.4; 12418 -13.7; 13660 -13.8; 15026 -10.8; 16529 -6.0; 18182 -3.6; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall MID ANC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall MID ANC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 680 Hz   | 0.69 | 2.3 dB  |
| Peaking | 3767 Hz  | 2.55 | -5.8 dB |
| Peaking | 12589 Hz | 3.87 | -6.4 dB |
| Peaking | 14284 Hz | 1.67 | -8.1 dB |
| Peaking | 17615 Hz | 1.79 | 1.4 dB  |
| Peaking | 17 Hz    | 0.34 | -1.1 dB |
| Peaking | 95 Hz    | 1.28 | -1.5 dB |
| Peaking | 5774 Hz  | 4.35 | 7.1 dB  |
| Peaking | 7539 Hz  | 2.58 | -9.9 dB |
| Peaking | 9158 Hz  | 2.47 | 5.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -7.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Marshall%20MID%20ANC/Marshall%20MID%20ANC.png)