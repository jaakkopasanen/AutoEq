# Audeze LCD2 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.4; 25 -1.6; 28 -2.0; 31 -2.4; 34 -2.8; 37 -3.2; 41 -3.5; 45 -3.7; 49 -3.7; 54 -3.8; 60 -3.9; 66 -4.2; 72 -4.5; 79 -5.0; 87 -5.7; 96 -6.4; 106 -7.1; 116 -7.7; 128 -8.5; 141 -9.2; 155 -9.8; 170 -10.3; 187 -10.7; 206 -11.0; 227 -11.2; 249 -11.4; 274 -11.6; 302 -11.7; 332 -11.8; 365 -11.9; 402 -12.1; 442 -12.1; 486 -11.7; 535 -11.5; 588 -11.8; 647 -11.9; 712 -11.9; 783 -12.0; 861 -12.0; 947 -10.6; 1042 -9.7; 1146 -9.6; 1261 -9.0; 1387 -8.2; 1526 -6.5; 1678 -6.3; 1846 -5.9; 2031 -5.0; 2234 -2.3; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.9; 6373 -3.8; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -11.0; 15026 -13.6; 16529 -16.7; 18182 -19.6; 20000 -22.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD2 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.69 | 5.2 dB   |
| Peaking | 71 Hz    | 0.89 | 2.9 dB   |
| Peaking | 260 Hz   | 0.43 | -5.0 dB  |
| Peaking | 849 Hz   | 0.88 | -3.8 dB  |
| Peaking | 3441 Hz  | 0.92 | 7.4 dB   |
| Peaking | 1942 Hz  | 7.51 | -1.2 dB  |
| Peaking | 2399 Hz  | 6.38 | 1.8 dB   |
| Peaking | 5512 Hz  | 5.46 | 3.0 dB   |
| Peaking | 17235 Hz | 1.03 | -8.0 dB  |
| Peaking | 19779 Hz | 0.91 | -13.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB   |
| Peaking | 62 Hz    | 1.41 | 2.4 dB   |
| Peaking | 125 Hz   | 1.41 | -1.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -12.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audeze%20LCD2%20Classic/Audeze%20LCD2%20Classic.png)