# Spiral Ears SE5U
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.3; 25 -3.9; 28 -4.7; 31 -5.3; 34 -5.8; 37 -6.2; 41 -6.7; 45 -7.2; 49 -7.7; 54 -8.2; 60 -8.6; 66 -9.0; 72 -9.5; 79 -9.9; 87 -10.4; 96 -10.8; 106 -11.3; 116 -11.6; 128 -11.9; 141 -12.1; 155 -12.1; 170 -12.2; 187 -12.2; 206 -12.2; 227 -12.0; 249 -11.7; 274 -11.5; 302 -11.1; 332 -10.6; 365 -10.1; 402 -9.6; 442 -9.2; 486 -8.7; 535 -8.2; 588 -7.6; 647 -7.2; 712 -6.6; 783 -6.2; 861 -5.9; 947 -6.0; 1042 -6.5; 1146 -7.5; 1261 -8.6; 1387 -9.6; 1526 -10.8; 1678 -12.2; 1846 -12.8; 2031 -11.8; 2234 -8.9; 2457 -6.4; 2703 -5.4; 2973 -5.9; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.9; 12418 -10.5; 13660 -19.1; 15026 -27.9; 16529 -29.3; 18182 -22.0; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Spiral Ears SE5U GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spiral Ears SE5U ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.79 | 5.5 dB   |
| Peaking | 192 Hz   | 0.38 | -6.3 dB  |
| Peaking | 1848 Hz  | 1.12 | -15.4 dB |
| Peaking | 4564 Hz  | 0.18 | 12.2 dB  |
| Peaking | 16001 Hz | 0.84 | -30.7 dB |
| Peaking | 2994 Hz  | 7.32 | -4.5 dB  |
| Peaking | 3286 Hz  | 3.2  | 2.6 dB   |
| Peaking | 7920 Hz  | 4.15 | -3.4 dB  |
| Peaking | 11724 Hz | 2.73 | 4.3 dB   |
| Peaking | 14393 Hz | 4.08 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB   |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 16000 Hz | 1.41 | -27.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Spiral%20Ears%20SE5U/Spiral%20Ears%20SE5U.png)