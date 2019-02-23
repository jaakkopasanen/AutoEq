# Beats Executive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.9; 45 -3.3; 49 -4.4; 54 -5.7; 60 -6.9; 66 -8.0; 72 -8.9; 79 -9.7; 87 -10.6; 96 -11.4; 106 -12.1; 116 -12.7; 128 -13.2; 141 -13.5; 155 -13.6; 170 -13.6; 187 -13.4; 206 -12.8; 227 -12.0; 249 -10.9; 274 -9.5; 302 -7.6; 332 -5.6; 365 -3.4; 402 -1.7; 442 -1.0; 486 -1.4; 535 -1.1; 588 -0.8; 647 -0.8; 712 -0.7; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -1.2; 1261 -1.4; 1387 -3.2; 1526 -4.2; 1678 -4.9; 1846 -6.5; 2031 -7.5; 2234 -8.0; 2457 -8.2; 2703 -8.4; 2973 -9.5; 3270 -13.1; 3597 -10.1; 3957 -4.3; 4353 -5.5; 4788 -8.7; 5267 -6.0; 5793 -4.5; 6373 -5.1; 7010 -5.1; 7711 -8.0; 8482 -9.5; 9330 -9.1; 10263 -8.1; 11289 -6.6; 12418 -6.5; 13660 -8.3; 15026 -11.8; 16529 -10.9; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Executive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Executive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 33 Hz    |  0.5  | 10.1 dB  |
| Peaking | 271 Hz   |  0.21 | -15.0 dB |
| Peaking | 431 Hz   |  0.78 | 16.3 dB  |
| Peaking | 964 Hz   |  0.89 | 10.2 dB  |
| Peaking | 3280 Hz  |  7.49 | -6.8 dB  |
| Peaking | 2358 Hz  |  2.59 | -1.3 dB  |
| Peaking | 4023 Hz  | 10.34 | 4.1 dB   |
| Peaking | 5995 Hz  |  5.65 | 2.6 dB   |
| Peaking | 15541 Hz |  1.98 | -6.0 dB  |
| Peaking | 22050 Hz |  1.51 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | 6.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -5.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Executive/Beats%20Executive.png)