# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.9; 25 -5.0; 28 -5.1; 31 -5.2; 34 -5.2; 37 -5.3; 41 -5.5; 45 -5.7; 49 -5.9; 54 -6.1; 60 -6.3; 66 -6.7; 72 -7.1; 79 -7.4; 87 -7.9; 96 -8.4; 106 -8.8; 116 -9.2; 128 -9.6; 141 -10.0; 155 -10.3; 170 -10.5; 187 -10.7; 206 -10.8; 227 -10.9; 249 -11.0; 274 -11.0; 302 -10.9; 332 -10.7; 365 -10.5; 402 -10.4; 442 -10.3; 486 -10.1; 535 -9.8; 588 -9.5; 647 -9.1; 712 -8.7; 783 -8.2; 861 -7.8; 947 -7.5; 1042 -7.5; 1146 -7.8; 1261 -7.9; 1387 -7.7; 1526 -6.9; 1678 -6.0; 1846 -5.3; 2031 -4.6; 2234 -3.7; 2457 -2.1; 2703 -1.1; 2973 -1.2; 3270 -1.8; 3597 -1.7; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.6; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.2; 15026 -17.4; 16529 -14.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.37 | 2.3 dB   |
| Peaking | 223 Hz   | 0.34 | -4.9 dB  |
| Peaking | 2752 Hz  | 2.07 | 4.4 dB   |
| Peaking | 4994 Hz  | 1.45 | 6.2 dB   |
| Peaking | 15563 Hz | 3.04 | -13.0 dB |
| Peaking | 899 Hz   | 3.35 | 0.7 dB   |
| Peaking | 1305 Hz  | 4.42 | -1.1 dB  |
| Peaking | 6468 Hz  | 5.35 | 3.1 dB   |
| Peaking | 7481 Hz  | 2.33 | -2.1 dB  |
| Peaking | 13164 Hz | 6    | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -8.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shure%20SE535/Shure%20SE535.png)