# Audeze iSine20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -4.7; 25 -4.6; 28 -4.6; 31 -4.6; 34 -4.6; 37 -4.7; 41 -4.7; 45 -4.8; 49 -4.8; 54 -4.9; 60 -5.1; 66 -5.3; 72 -5.5; 79 -5.8; 87 -6.1; 96 -6.5; 106 -6.9; 116 -7.2; 128 -7.6; 141 -7.9; 155 -8.1; 170 -8.3; 187 -8.5; 206 -8.7; 227 -8.8; 249 -8.8; 274 -8.8; 302 -8.8; 332 -8.7; 365 -8.7; 402 -8.9; 442 -9.1; 486 -9.3; 535 -9.6; 588 -9.9; 647 -10.4; 712 -11.0; 783 -11.4; 861 -11.6; 947 -12.4; 1042 -13.2; 1146 -13.4; 1261 -13.8; 1387 -14.3; 1526 -13.0; 1678 -10.6; 1846 -8.0; 2031 -5.1; 2234 -1.2; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.9; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -10.2; 10263 -11.4; 11289 -7.4; 12418 -6.7; 13660 -10.2; 15026 -11.4; 16529 -7.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 992 Hz   | 0.25 | -4.3 dB  |
| Peaking | 1460 Hz  | 0.76 | -18.9 dB |
| Peaking | 2266 Hz  | 0.44 | 19.8 dB  |
| Peaking | 9720 Hz  | 2.51 | -8.1 dB  |
| Peaking | 14673 Hz | 2.62 | -6.4 dB  |
| Peaking | 55 Hz    | 0.19 | 2.2 dB   |
| Peaking | 157 Hz   | 0.76 | -2.5 dB  |
| Peaking | 3571 Hz  | 2.55 | -0.8 dB  |
| Peaking | 6745 Hz  | 1.41 | 2.1 dB   |
| Peaking | 7341 Hz  | 4.02 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -8.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20iSine20/Audeze%20iSine20.png)