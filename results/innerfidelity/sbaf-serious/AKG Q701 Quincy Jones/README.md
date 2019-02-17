# AKG Q701 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.1; 37 -1.6; 41 -2.3; 45 -2.8; 49 -3.2; 54 -3.8; 60 -4.3; 66 -4.8; 72 -4.9; 79 -4.9; 87 -5.2; 96 -6.1; 106 -6.5; 116 -6.9; 128 -7.5; 141 -7.8; 155 -8.1; 170 -8.0; 187 -8.2; 206 -8.3; 227 -8.3; 249 -8.3; 274 -8.3; 302 -8.0; 332 -8.0; 365 -7.8; 402 -7.7; 442 -7.4; 486 -7.3; 535 -7.0; 588 -5.5; 647 -5.8; 712 -5.8; 783 -5.5; 861 -6.0; 947 -6.4; 1042 -6.5; 1146 -6.9; 1261 -7.5; 1387 -8.4; 1526 -9.7; 1678 -10.8; 1846 -11.7; 2031 -12.0; 2234 -11.7; 2457 -10.4; 2703 -8.8; 2973 -7.7; 3270 -6.5; 3597 -6.1; 3957 -7.0; 4353 -9.0; 4788 -8.4; 5267 -8.5; 5793 -10.1; 6373 -11.3; 7010 -11.0; 7711 -11.3; 8482 -12.0; 9330 -9.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.9; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.46 | 6.2 dB  |
| Peaking | 216 Hz   | 0.55 | -2.3 dB |
| Peaking | 729 Hz   | 1.52 | 1.8 dB  |
| Peaking | 1959 Hz  | 2.1  | -5.9 dB |
| Peaking | 7366 Hz  | 1.76 | -5.4 dB |
| Peaking | 2442 Hz  | 6.11 | -1.0 dB |
| Peaking | 3578 Hz  | 3.66 | 2.2 dB  |
| Peaking | 4409 Hz  | 5.59 | -1.7 dB |
| Peaking | 10845 Hz | 4.62 | 1.5 dB  |
| Peaking | 19473 Hz | 1.6  | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20Q701%20Quincy%20Jones/AKG%20Q701%20Quincy%20Jones.png)