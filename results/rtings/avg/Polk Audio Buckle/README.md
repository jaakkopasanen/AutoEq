# Polk Audio Buckle
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.3; 25 -11.5; 28 -11.8; 31 -11.9; 34 -11.9; 37 -11.8; 41 -11.6; 45 -11.3; 49 -11.1; 54 -10.7; 60 -10.4; 66 -10.2; 72 -10.0; 79 -9.8; 87 -9.8; 96 -9.7; 106 -9.7; 116 -9.6; 128 -9.5; 141 -9.4; 155 -9.2; 170 -9.2; 187 -9.2; 206 -9.2; 227 -9.1; 249 -8.8; 274 -9.2; 302 -10.0; 332 -10.1; 365 -9.5; 402 -8.5; 442 -8.0; 486 -8.6; 535 -9.2; 588 -9.1; 647 -8.9; 712 -10.0; 783 -10.9; 861 -10.7; 947 -10.2; 1042 -9.4; 1146 -8.7; 1261 -8.0; 1387 -7.3; 1526 -6.7; 1678 -6.1; 1846 -5.8; 2031 -5.6; 2234 -4.9; 2457 -4.1; 2703 -4.2; 2973 -4.9; 3270 -5.3; 3597 -4.5; 3957 -2.8; 4353 -1.6; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio Buckle GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio Buckle ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.56 | -5.2 dB |
| Peaking | 146 Hz  | 0.57 | -2.1 dB |
| Peaking | 327 Hz  | 2.58 | -2.1 dB |
| Peaking | 831 Hz  | 1.82 | -4.3 dB |
| Peaking | 5115 Hz | 1.59 | 6.5 dB  |
| Peaking | 1157 Hz | 3.88 | -0.7 dB |
| Peaking | 2686 Hz | 1.57 | 2.3 dB  |
| Peaking | 3263 Hz | 3.57 | -2.1 dB |
| Peaking | 6468 Hz | 4.18 | 3.9 dB  |
| Peaking | 7095 Hz | 1.53 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Polk%20Audio%20Buckle/Polk%20Audio%20Buckle.png)