# Audeze LCD-2 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.2; 34 -1.7; 37 -2.0; 41 -2.3; 45 -2.4; 49 -2.5; 54 -2.6; 60 -2.7; 66 -2.9; 72 -3.1; 79 -3.4; 87 -3.7; 96 -4.1; 106 -4.5; 116 -4.8; 128 -5.2; 141 -5.5; 155 -5.7; 170 -5.8; 187 -5.8; 206 -5.8; 227 -5.9; 249 -6.0; 274 -6.2; 302 -6.4; 332 -6.5; 365 -6.6; 402 -6.7; 442 -6.7; 486 -6.4; 535 -6.4; 588 -6.9; 647 -7.4; 712 -7.7; 783 -8.2; 861 -8.5; 947 -7.3; 1042 -6.7; 1146 -7.0; 1261 -6.6; 1387 -6.2; 1526 -4.7; 1678 -5.2; 1846 -4.9; 2031 -5.2; 2234 -3.4; 2457 -3.9; 2703 -2.3; 2973 -2.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -1.0; 5793 -3.6; 6373 -5.6; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.4; 18182 -9.0; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.76 | 5.7 dB  |
| Peaking | 68 Hz    | 0.85 | 2.5 dB  |
| Peaking | 815 Hz   | 2.71 | -2.2 dB |
| Peaking | 3486 Hz  | 1.36 | 5.9 dB  |
| Peaking | 5028 Hz  | 4.14 | 3.3 dB  |
| Peaking | 1353 Hz  | 4.75 | -0.9 dB |
| Peaking | 1525 Hz  | 5.99 | 1.5 dB  |
| Peaking | 19626 Hz | 0.89 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)