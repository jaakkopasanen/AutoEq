# Pioneer Monitor 10 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -10.9; 25 -11.0; 28 -11.0; 31 -11.1; 34 -11.1; 37 -11.1; 41 -11.1; 45 -11.2; 49 -11.3; 54 -11.4; 60 -11.4; 66 -11.4; 72 -11.4; 79 -11.3; 87 -11.2; 96 -11.1; 106 -11.5; 116 -11.5; 128 -10.4; 141 -9.4; 155 -12.9; 170 -10.6; 187 -10.8; 206 -12.0; 227 -12.6; 249 -12.9; 274 -12.9; 302 -12.2; 332 -12.0; 365 -10.9; 402 -9.7; 442 -8.2; 486 -7.1; 535 -5.5; 588 -3.7; 647 -2.7; 712 -2.4; 783 -3.3; 861 -4.9; 947 -6.4; 1042 -6.2; 1146 -6.6; 1261 -7.8; 1387 -10.7; 1526 -14.0; 1678 -15.7; 1846 -14.0; 2031 -10.3; 2234 -7.1; 2457 -6.2; 2703 -6.7; 2973 -4.2; 3270 -2.8; 3597 -3.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer Monitor 10 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.4  | -4.6 dB  |
| Peaking | 125 Hz  | 0.93 | -2.4 dB  |
| Peaking | 269 Hz  | 2.06 | -5.9 dB  |
| Peaking | 1698 Hz | 3.71 | -10.8 dB |
| Peaking | 4658 Hz | 1.29 | 6.6 dB   |
| Peaking | 375 Hz  | 3.48 | -2.0 dB  |
| Peaking | 637 Hz  | 2.89 | 3.9 dB   |
| Peaking | 762 Hz  | 4.29 | 2.5 dB   |
| Peaking | 6352 Hz | 3.81 | 4.7 dB   |
| Peaking | 7128 Hz | 1.48 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20Monitor%2010%20II/Pioneer%20Monitor%2010%20II.png)