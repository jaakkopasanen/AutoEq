# XFYRO xS2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.0; 25 -4.3; 28 -4.8; 31 -5.2; 34 -5.5; 37 -5.8; 41 -6.2; 45 -6.5; 49 -6.9; 54 -7.2; 60 -7.6; 66 -8.0; 72 -8.4; 79 -8.8; 87 -9.2; 96 -9.7; 106 -10.0; 116 -10.3; 128 -10.6; 141 -10.7; 155 -10.8; 170 -11.0; 187 -11.1; 206 -11.1; 227 -10.9; 249 -10.7; 274 -10.4; 302 -10.0; 332 -9.6; 365 -9.1; 402 -8.6; 442 -8.0; 486 -7.3; 535 -6.5; 588 -5.7; 647 -4.9; 712 -4.2; 783 -3.6; 861 -3.2; 947 -3.3; 1042 -3.6; 1146 -3.9; 1261 -3.3; 1387 -3.1; 1526 -2.9; 1678 -2.6; 1846 -2.2; 2031 -1.8; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.6; 3270 -2.2; 3597 -4.2; 3957 -6.0; 4353 -7.8; 4788 -10.1; 5267 -12.3; 5793 -11.8; 6373 -7.9; 7010 -5.6; 7711 -6.2; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -11.1; 16529 -17.6; 18182 -16.3; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`XFYRO xS2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `XFYRO xS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 195 Hz   | 0.56 | -4.9 dB  |
| Peaking | 768 Hz   | 1.99 | 2.4 dB   |
| Peaking | 3975 Hz  | 0.44 | 9.8 dB   |
| Peaking | 5176 Hz  | 1.46 | -14.7 dB |
| Peaking | 17432 Hz | 1.21 | -12.8 dB |
| Peaking | 21 Hz    | 1.33 | 3.0 dB   |
| Peaking | 2753 Hz  | 3.48 | 1.5 dB   |
| Peaking | 6917 Hz  | 5.72 | 2.4 dB   |
| Peaking | 13208 Hz | 0.13 | -0.9 dB  |
| Peaking | 13762 Hz | 3.42 | 3.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -9.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/XFYRO%20xS2/XFYRO%20xS2.png)