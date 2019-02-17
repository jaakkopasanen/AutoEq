# Akai MPC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.1; 25 -3.2; 28 -3.3; 31 -3.4; 34 -3.5; 37 -3.5; 41 -3.6; 45 -3.6; 49 -3.6; 54 -3.6; 60 -3.9; 66 -4.2; 72 -4.3; 79 -4.4; 87 -4.4; 96 -5.1; 106 -6.3; 116 -6.1; 128 -6.1; 141 -6.7; 155 -7.1; 170 -6.0; 187 -6.7; 206 -6.3; 227 -6.3; 249 -5.7; 274 -5.2; 302 -5.0; 332 -5.0; 365 -5.0; 402 -4.9; 442 -5.0; 486 -5.3; 535 -5.2; 588 -5.0; 647 -5.0; 712 -5.4; 783 -5.4; 861 -5.9; 947 -6.3; 1042 -6.6; 1146 -6.7; 1261 -6.9; 1387 -7.7; 1526 -7.1; 1678 -7.7; 1846 -6.0; 2031 -4.6; 2234 -4.8; 2457 -5.0; 2703 -3.8; 2973 -2.8; 3270 -5.0; 3597 -5.7; 3957 -4.1; 4353 -3.1; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Akai MPC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Akai MPC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.81 | 3.3 dB  |
| Peaking | 60 Hz   | 1.49 | 2.0 dB  |
| Peaking | 432 Hz  | 1.22 | 1.7 dB  |
| Peaking | 2834 Hz | 4.56 | 3.1 dB  |
| Peaking | 5458 Hz | 2.33 | 6.8 dB  |
| Peaking | 704 Hz  | 3.41 | 0.7 dB  |
| Peaking | 1715 Hz | 1.8  | -2.2 dB |
| Peaking | 2028 Hz | 4.24 | 3.2 dB  |
| Peaking | 7865 Hz | 7.18 | -1.2 dB |
| Peaking | 9652 Hz | 3.91 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Akai%20MPC/Akai%20MPC.png)