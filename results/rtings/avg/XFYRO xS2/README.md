# XFYRO xS2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.7; 31 -2.1; 34 -2.5; 37 -2.7; 41 -3.1; 45 -3.4; 49 -3.7; 54 -4.2; 60 -4.9; 66 -5.6; 72 -6.2; 79 -6.8; 87 -7.5; 96 -8.3; 106 -9.1; 116 -9.9; 128 -10.6; 141 -11.2; 155 -11.7; 170 -12.2; 187 -12.5; 206 -12.8; 227 -12.8; 249 -12.5; 274 -12.2; 302 -11.8; 332 -11.4; 365 -11.0; 402 -10.4; 442 -9.8; 486 -9.1; 535 -8.2; 588 -7.4; 647 -6.6; 712 -5.8; 783 -5.3; 861 -4.9; 947 -5.0; 1042 -5.2; 1146 -5.6; 1261 -4.9; 1387 -4.7; 1526 -4.5; 1678 -4.1; 1846 -3.7; 2031 -3.2; 2234 -2.1; 2457 -1.0; 2703 -1.0; 2973 -2.2; 3270 -4.2; 3597 -6.3; 3957 -8.1; 4353 -10.0; 4788 -11.5; 5267 -13.7; 5793 -13.7; 6373 -10.7; 7010 -7.3; 7711 -6.3; 8482 -8.8; 9330 -9.5; 10263 -5.6; 11289 -5.1; 12418 -5.1; 13660 -5.5; 15026 -13.6; 16529 -19.5; 18182 -18.1; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`XFYRO xS2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `XFYRO xS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.4  | 4.9 dB   |
| Peaking | 210 Hz   | 0.62 | -8.1 dB  |
| Peaking | 2554 Hz  | 1.8  | 5.2 dB   |
| Peaking | 5293 Hz  | 2.17 | -9.2 dB  |
| Peaking | 17569 Hz | 1.25 | -16.3 dB |
| Peaking | 833 Hz   | 3.27 | 1.6 dB   |
| Peaking | 7425 Hz  | 5.85 | 2.7 dB   |
| Peaking | 9024 Hz  | 6.47 | -3.4 dB  |
| Peaking | 12455 Hz | 1.77 | 5.6 dB   |
| Peaking | 18580 Hz | 0.16 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB   |
| Peaking | 62 Hz    | 1.41 | 0.4 dB   |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -7.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -12.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/XFYRO%20xS2/XFYRO%20xS2.png)