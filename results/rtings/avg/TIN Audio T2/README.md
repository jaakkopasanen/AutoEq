# TIN Audio T2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 -1.6; 23 -1.7; 25 -1.7; 28 -1.6; 31 -1.6; 34 -1.6; 37 -1.5; 41 -1.4; 45 -1.3; 49 -1.3; 54 -1.2; 60 -1.5; 66 -1.7; 72 -1.9; 79 -2.0; 87 -2.3; 96 -2.6; 106 -3.0; 116 -3.4; 128 -3.7; 141 -4.0; 155 -4.1; 170 -4.2; 187 -4.1; 206 -4.1; 227 -4.0; 249 -3.8; 274 -3.5; 302 -3.2; 332 -2.8; 365 -2.5; 402 -2.1; 442 -1.7; 486 -1.3; 535 -0.8; 588 -0.3; 647 0.1; 712 0.4; 783 0.7; 861 0.7; 947 0.4; 1042 -0.3; 1146 -0.8; 1261 -0.5; 1387 -0.2; 1526 -0.2; 1678 -0.3; 1846 -0.4; 2031 -0.6; 2234 -0.1; 2457 0.4; 2703 1.3; 2973 2.9; 3270 4.2; 3597 4.0; 3957 2.6; 4353 1.3; 4788 -0.5; 5267 -0.1; 5793 2.8; 6373 3.4; 7010 2.1; 7711 -0.2; 8482 -0.7; 9330 -0.5; 10263 -2.6; 11289 -5.3; 12418 -5.4; 13660 -2.7; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TIN Audio T2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TIN Audio T2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 21 Hz    |  0.56 | -1.5 dB |
| Peaking | 181 Hz   |  0.68 | -4.3 dB |
| Peaking | 3389 Hz  |  3.57 | 4.7 dB  |
| Peaking | 6355 Hz  |  5    | 4.0 dB  |
| Peaking | 11920 Hz |  2.55 | -6.3 dB |
| Peaking | 389 Hz   |  1.93 | -0.6 dB |
| Peaking | 845 Hz   |  1.47 | 2.5 dB  |
| Peaking | 1051 Hz  |  1.26 | -1.8 dB |
| Peaking | 4958 Hz  | 11.32 | -1.8 dB |
| Peaking | 15102 Hz |  5.09 | 1.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/TIN%20Audio%20T2/TIN%20Audio%20T2.png)