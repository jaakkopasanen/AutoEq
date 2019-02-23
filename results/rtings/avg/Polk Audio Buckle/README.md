# Polk Audio Buckle
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.5; 25 -11.7; 28 -12.0; 31 -12.1; 34 -12.1; 37 -12.0; 41 -11.7; 45 -11.5; 49 -11.2; 54 -10.9; 60 -10.6; 66 -10.4; 72 -10.1; 79 -10.0; 87 -9.9; 96 -9.9; 106 -9.9; 116 -9.8; 128 -9.8; 141 -9.6; 155 -9.4; 170 -9.4; 187 -9.4; 206 -9.4; 227 -9.1; 249 -8.8; 274 -9.2; 302 -10.1; 332 -10.1; 365 -9.6; 402 -8.5; 442 -8.0; 486 -8.6; 535 -9.1; 588 -9.0; 647 -8.8; 712 -9.9; 783 -10.8; 861 -10.6; 947 -10.0; 1042 -9.3; 1146 -8.6; 1261 -7.8; 1387 -7.2; 1526 -6.5; 1678 -5.8; 1846 -5.4; 2031 -5.1; 2234 -4.1; 2457 -3.2; 2703 -3.6; 2973 -4.8; 3270 -5.5; 3597 -4.8; 3957 -3.1; 4353 -2.0; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio Buckle GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio Buckle ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.46 | -5.3 dB |
| Peaking | 237 Hz  | 0.43 | -2.5 dB |
| Peaking | 861 Hz  | 2.03 | -3.6 dB |
| Peaking | 2395 Hz | 2.77 | 3.0 dB  |
| Peaking | 5304 Hz | 2.04 | 6.7 dB  |
| Peaking | 324 Hz  | 3.46 | -3.1 dB |
| Peaking | 327 Hz  | 1.73 | 1.9 dB  |
| Peaking | 3264 Hz | 9.86 | -0.9 dB |
| Peaking | 6511 Hz | 6.28 | 2.6 dB  |
| Peaking | 7777 Hz | 2.19 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Polk%20Audio%20Buckle/Polk%20Audio%20Buckle.png)