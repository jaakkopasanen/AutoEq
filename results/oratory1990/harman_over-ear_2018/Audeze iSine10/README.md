# Audeze iSine10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.7; 116 -1.1; 128 -1.4; 141 -1.7; 155 -1.9; 170 -2.1; 187 -2.3; 206 -2.5; 227 -2.6; 249 -2.6; 274 -2.6; 302 -2.6; 332 -2.5; 365 -2.5; 402 -2.6; 442 -2.8; 486 -3.1; 535 -3.3; 588 -3.6; 647 -4.0; 712 -4.5; 783 -5.0; 861 -5.6; 947 -6.1; 1042 -6.7; 1146 -7.2; 1261 -7.4; 1387 -7.9; 1526 -7.1; 1678 -4.6; 1846 -1.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.19 | 6.2 dB  |
| Peaking | 435 Hz  | 1.03 | 2.3 dB  |
| Peaking | 1405 Hz | 1.48 | -7.3 dB |
| Peaking | 2106 Hz | 0.84 | 8.5 dB  |
| Peaking | 5159 Hz | 1.81 | 4.8 dB  |
| Peaking | 945 Hz  | 4.46 | -0.5 dB |
| Peaking | 1539 Hz | 6.99 | -0.7 dB |
| Peaking | 2916 Hz | 0.34 | 0.3 dB  |
| Peaking | 6443 Hz | 4.5  | 3.7 dB  |
| Peaking | 7303 Hz | 1.47 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 4.0 dB  |
| Peaking | 250 Hz   | 1.41 | 2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20iSine10/Audeze%20iSine10.png)